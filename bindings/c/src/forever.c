#define _XOPEN_SOURCE 700
#include "forever.h"
#include "../vendor/cJSON.h"
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif
#include "contracts.inc"
#include "json_lex.h"
typedef struct {
  char *id;
  char *json;
  cJSON *value;
} rec;
struct fw_model {
  char *manifest_json;
  cJSON *manifest;
  rec *records;
  size_t count;
};
static int error(fw_error *e, const char *code, const char *path) {
  if (e) {
    snprintf(e->code, sizeof e->code, "%s", code);
    snprintf(e->message, sizeof e->message, "%s: %.200s", code, path);
  }
  return 0;
}
static const cJSON *get(const cJSON *v, const char *key) {
  const cJSON *item;
  if (!key)
    return NULL;
  cJSON_ArrayForEach(
      item, v) if (item->string && item->string_length == strlen(key) &&
                   !memcmp(item->string, key, item->string_length)) return item;
  return NULL;
}
static const char *str(const cJSON *v) {
  return cJSON_IsString(v) && strlen(v->valuestring) == v->valuestring_length
             ? v->valuestring
             : NULL;
}
static int equal(const char *a, const char *b) {
  return a && b && !strcmp(a, b);
}
static int version(const char *v) {
  if (!v || strncmp(v, "0.", 2) || !v[2])
    return 0;
  for (v += 2; *v; v++)
    if (!isdigit((unsigned char)*v))
      return 0;
  return 1;
}
static int identifier(const char *v) {
  int separator = 0;
  if (!v || *v < 'a' || *v > 'z')
    return 0;
  for (; *v; v++) {
    if ((*v >= 'a' && *v <= 'z') || isdigit((unsigned char)*v))
      separator = 0;
    else if ((*v == '.' || *v == '_' || *v == '-') && !separator)
      separator = 1;
    else
      return 0;
  }
  return !separator;
}
static int extension_key(const char *v) {
  int separator = 0, count = 0;
  if (!v || !*v)
    return 0;
  for (; *v; v++) {
    if ((*v >= 'a' && *v <= 'z') || (*v >= '0' && *v <= '9'))
      separator = 0;
    else if ((*v == '.' || *v == '-') && !separator) {
      separator = 1;
      count++;
    } else
      return 0;
  }
  return count > 0 && !separator;
}
static int pathok(const char *v) {
  const char *p;
  if (!v || !*v || v[0] == '/' || strchr(v, '\\') || strchr(v, ':') ||
      strlen(v) < 6 || strcmp(v + strlen(v) - 5, ".json"))
    return 0;
  for (p = v; *p; p++)
    if ((p == v || p[-1] == '/') && p[0] == '.' && p[1] == '.' &&
        (p[2] == '/' || !p[2]))
      return 0;
  return 1;
}
/* Strict UTF-8, rejecting overlong encodings, surrogate codepoints and embedded
 * NUL. */
static int utf8(const unsigned char *p, size_t n) {
  size_t i = 0;
  while (i < n) {
    unsigned c = p[i++], cp;
    int k, j;
    if (c < 128) {
      if (!c)
        return 0;
      continue;
    }
    if (c >= 194 && c <= 223) {
      k = 1;
      cp = c & 31;
    } else if (c >= 224 && c <= 239) {
      k = 2;
      cp = c & 15;
    } else if (c >= 240 && c <= 244) {
      k = 3;
      cp = c & 7;
    } else
      return 0;
    if (i + (size_t)k > n)
      return 0;
    for (j = 0; j < k; j++) {
      c = p[i++];
      if ((c & 192) != 128)
        return 0;
      cp = (cp << 6) | (c & 63);
    }
    if ((k == 2 && cp < 2048) || (k == 3 && cp < 65536) ||
        (cp >= 0xd800 && cp <= 0xdfff) || cp > 0x10ffff)
      return 0;
  }
  return 1;
}
static int bounded(const cJSON *v, int depth) {
  const cJSON *a, *b;
  if (depth > 64)
    return 0;
  if (cJSON_IsNumber(v) && !isfinite(v->valuedouble))
    return 0;
  cJSON_ArrayForEach(a, v) {
    if (cJSON_IsObject(v))
      for (b = a->next; b; b = b->next)
        if (a->string_length == b->string_length &&
            !memcmp(a->string, b->string, a->string_length))
          return 0;
    if (!bounded(a, depth + 1))
      return 0;
  }
  return 1;
}
static char *real_target(const char *path) {
#ifdef _WIN32
  HANDLE h = CreateFileA(path, 0,
                         FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE,
                         NULL, OPEN_EXISTING, FILE_FLAG_BACKUP_SEMANTICS, NULL);
  char buf[32768];
  DWORD n;
  char *out;
  if (h == INVALID_HANDLE_VALUE)
    return NULL;
  n = GetFinalPathNameByHandleA(h, buf, sizeof buf, FILE_NAME_NORMALIZED);
  CloseHandle(h);
  if (!n || n >= sizeof buf)
    return NULL;
  out = malloc(n + 1);
  if (out)
    memcpy(out, buf, n + 1);
  return out;
#else
  return realpath(path, NULL);
#endif
}
static cJSON *readjson(const char *root, const char *path, size_t *total,
                       char **raw, fw_error *e) {
  char *target = real_target(path), *data;
  FILE *f;
  long n;
  cJSON *v;
  struct stat st;
  size_t length = strlen(root);
  if (!target) {
    error(e, "io", path);
    return NULL;
  }
  if (strncmp(target, root, length) ||
      (target[length] != '/' && target[length] != '\\')) {
    free(target);
    error(e, "path-escape", path);
    return NULL;
  }
  if (stat(target, &st) || !S_ISREG(st.st_mode)) {
    free(target);
    error(e, "invalid-path", path);
    return NULL;
  }
  f = fopen(target, "rb");
  free(target);
  if (!f) {
    error(e, "io", path);
    return NULL;
  }
  if (fseek(f, 0, SEEK_END) || (n = ftell(f)) < 0 || n > 1048576 ||
      *total + (size_t)n > 16777216) {
    fclose(f);
    error(e, "resource-limit", path);
    return NULL;
  }
  rewind(f);
  data = malloc((size_t)n + 1);
  if (!data) {
    fclose(f);
    error(e, "allocation", path);
    return NULL;
  }
  if (fread(data, 1, (size_t)n, f) != (size_t)n) {
    fclose(f);
    free(data);
    error(e, "io", path);
    return NULL;
  }
  fclose(f);
  *total += (size_t)n;
  data[n] = 0;
  if (!utf8((unsigned char *)data, (size_t)n)) {
    free(data);
    error(e, "invalid-utf8", path);
    return NULL;
  }
  if (!fw_json_syntax((unsigned char *)data, (size_t)n)) {
    free(data);
    error(e, "invalid-json", path);
    return NULL;
  }
  v = cJSON_ParseWithLengthOpts(data, (size_t)n + 1, NULL, 1);
  if (!v || !bounded(v, 0)) {
    free(data);
    cJSON_Delete(v);
    error(e, "invalid-json", path);
    return NULL;
  }
  if (raw)
    *raw = data;
  else
    free(data);
  return v;
}
static const cJSON *schema_ref(const cJSON *schemas, const char *ref) {
  char buf[160], *hash, *p;
  const cJSON *s;
  if (strlen(ref) >= sizeof buf)
    return NULL;
  strcpy(buf, ref);
  hash = strchr(buf, '#');
  if (hash)
    *hash++ = 0;
  s = get(schemas, buf);
  if (hash) {
    p = strtok(hash, "/");
    while (p && s) {
      s = get(s, p);
      p = strtok(NULL, "/");
    }
  }
  return s;
}
static int same_json(const cJSON *a, const cJSON *b) {
  if (cJSON_IsString(a) && cJSON_IsString(b))
    return a->valuestring_length == b->valuestring_length &&
           !memcmp(a->valuestring, b->valuestring, a->valuestring_length);
  return cJSON_Compare(a, b, 1);
}
static int structure(const cJSON *v, const cJSON *s, const cJSON *schemas,
                     const char *path, fw_error *e) {
  const cJSON *a, *b, *properties;
  const char *type, *pattern, *reference;
  if (!s)
    return error(e, "invalid-schema", path);
  reference = str(get(s, "$ref"));
  if (reference)
    s = schema_ref(schemas, reference);
  if (!s)
    return error(e, "invalid-schema", path);
  type = str(get(s, "type"));
  if (type && !((equal(type, "object") && cJSON_IsObject(v)) ||
                (equal(type, "array") && cJSON_IsArray(v)) ||
                (equal(type, "string") && cJSON_IsString(v)) ||
                (equal(type, "number") && cJSON_IsNumber(v))))
    return error(e, "invalid-type", path);
  a = get(s, "const");
  if (a && (!str(v) || !str(a) || !equal(str(v), str(a))))
    return error(e, "invalid-value", path);
  a = get(s, "enum");
  if (a) {
    int found = 0;
    cJSON_ArrayForEach(b, a) if (str(v) && str(b) && equal(str(v), str(b)))
        found = 1;
    if (!found)
      return error(e, "invalid-value", path);
  }
  if (cJSON_IsNumber(v)) {
    a = get(s, "minimum");
    b = get(s, "maximum");
    if (!isfinite(v->valuedouble) || (a && v->valuedouble < a->valuedouble) ||
        (b && v->valuedouble > b->valuedouble))
      return error(e, "invalid-value", path);
  }
  pattern = str(get(s, "pattern"));
  if (pattern && cJSON_IsString(v)) {
    int ok;
    if (strstr(pattern, "a-z][a-z0-9]"))
      ok = identifier(str(v));
    else if (strstr(pattern, "a-z0-9]+(?:"))
      ok = extension_key(str(v));
    else if (strstr(pattern, "?!/"))
      ok = pathok(str(v));
    else
      ok = version(str(v));
    if (!ok)
      return error(e, "invalid-value", path);
  }
  if (cJSON_IsObject(v)) {
    cJSON_ArrayForEach(a, get(s, "required")) if (!get(v, str(a))) return error(
        e, "missing-required", path);
    properties = get(s, "properties");
    cJSON_ArrayForEach(a, v) {
      char nested[256];
      snprintf(nested, sizeof nested, "%.150s.%.80s", path, a->string);
      b = strlen(a->string) == a->string_length ? get(properties, a->string)
                                                : NULL;
      if (b && !structure(a, b, schemas, nested, e))
        return 0;
      if (!b && cJSON_IsFalse(get(s, "additionalProperties")))
        return error(e, "unknown-field", nested);
      b = get(s, "propertyNames");
      if (b) {
        cJSON *key;
        int ok;
        if (strlen(a->string) != a->string_length)
          return error(e, "invalid-value", nested);
        key = cJSON_CreateString(a->string);
        if (key)
          key->valuestring_length = strlen(key->valuestring);
        ok = key && structure(key, b, schemas, nested, e);
        cJSON_Delete(key);
        if (!ok)
          return 0;
      }
    }
  }
  if (cJSON_IsArray(v)) {
    cJSON_ArrayForEach(a, v) {
      b = get(s, "items");
      if (b && !structure(a, b, schemas, path, e))
        return 0;
      if (cJSON_IsTrue(get(s, "uniqueItems")))
        for (b = a->next; b; b = b->next)
          if (same_json(a, b))
            return error(e, "duplicate-value", path);
    }
  }
  return 1;
}
fw_model *fw_load(const char *dir, fw_error *e) {
  char path[32768], *root = real_target(dir);
  size_t total = 0;
  const cJSON *groups, *paths, *entry;
  fw_model *m = calloc(1, sizeof *m);
  cJSON *schemas = cJSON_Parse((const char *)contract_json);
  if (!m || !root || !schemas) {
    error(e, "io", "model root");
    goto fail;
  }
  if (snprintf(path, sizeof path, "%s/manifest.json", dir) >=
      (int)sizeof path) {
    error(e, "resource-limit", "path");
    goto fail;
  }
  m->manifest = readjson(root, path, &total, &m->manifest_json, e);
  if (!m->manifest ||
      !structure(m->manifest, get(schemas, "manifest.schema.json"), schemas,
                 "manifest", e))
    goto fail;
  if (!version(str(get(m->manifest, "foreverVersion")))) {
    error(e, "unsupported-version", "manifest");
    goto fail;
  }
  groups = get(m->manifest, "records");
  cJSON_ArrayForEach(paths, groups) cJSON_ArrayForEach(entry, paths) {
    rec *next;
    const char *rel = str(entry);
    cJSON *v;
    char *raw = NULL;
    size_t i;
    if (!pathok(rel)) {
      error(e, "path-escape", "record path");
      goto fail;
    }
    if (m->count >= 4096 ||
        snprintf(path, sizeof path, "%s/%s", dir, rel) >= (int)sizeof path) {
      error(e, "resource-limit", "record inventory");
      goto fail;
    } /* Duplicate paths are rejected before reading. */
    {
      const cJSON *g, *p;
      size_t occurrences = 0;
      cJSON_ArrayForEach(g, groups)
          cJSON_ArrayForEach(p, g) if (equal(str(p), rel)) occurrences++;
      if (occurrences != 1) {
        error(e, "duplicate-path", rel);
        goto fail;
      }
    }
    v = readjson(root, path, &total, &raw, e);
    if (!v)
      goto fail;
    next = realloc(m->records, (m->count + 1) * sizeof *next);
    if (!next) {
      free(raw);
      cJSON_Delete(v);
      error(e, "allocation", rel);
      goto fail;
    }
    m->records = next;
    i = m->count++;
    m->records[i].value = v;
    m->records[i].id = (char *)str(get(v, "id"));
    m->records[i].json = raw;
    if (!m->records[i].json) {
      error(e, "allocation", rel);
      goto fail;
    }
  }
  free(root);
  cJSON_Delete(schemas);
  return m;
fail:
  free(root);
  cJSON_Delete(schemas);
  fw_free(m);
  return NULL;
}
void fw_free(fw_model *m) {
  size_t i;
  if (!m)
    return;
  for (i = 0; i < m->count; i++) {
    free(m->records[i].json);
    cJSON_Delete(m->records[i].value);
  }
  free(m->records);
  free(m->manifest_json);
  cJSON_Delete(m->manifest);
  free(m);
}
size_t fw_record_count(const fw_model *m) { return m ? m->count : 0; }
const char *fw_get_entity_json(const fw_model *m, const char *id) {
  size_t i;
  if (m)
    for (i = 0; i < m->count; i++)
      if (equal(m->records[i].id, id))
        return m->records[i].json;
  return NULL;
}
static int reference(const fw_model *m, const cJSON *v, fw_error *e,
                     const char *path) {
  if (cJSON_IsString(v) && !fw_get_entity_json(m, str(v)))
    return error(e, "broken-reference", path);
  return 1;
}
int fw_validate(const fw_model *m, fw_error *e) {
  size_t i, j;
  int ok = 1;
  cJSON *schemas = cJSON_Parse((const char *)contract_json);
  const cJSON *schema, *field, *entry, *ev;
  static const char *refs[] = {
      "relatedCapabilities",      "relatedConstraints",
      "relatedInvariants",        "relatedImplementations",
      "requiredCapabilities",     "protectedInvariants",
      "compatibilityObligations", "relatedEntities",
      "preservedCapabilities",    "preservedInvariants",
      "compatibilityImpact",      "satisfiesCapabilities",
      "constrainedByInvariants",  "satisfiesConstraints",
      "compatibilityContracts",   "evidence",
      "sourceImplementation",     "targetImplementation",
      "currentImplementation",    "scope",
      "validationReferences"};
  if (!m || !version(str(get(m->manifest, "foreverVersion")))) {
    cJSON_Delete(schemas);
    return error(e, "unsupported-version", "manifest");
  }
  for (i = 0; i < m->count && ok; i++) {
    const cJSON *v = m->records[i].value;
    schema = NULL;
    cJSON_ArrayForEach(
        field, schemas) if (equal(str(get(get(get(field, "properties"), "kind"),
                                          "const")),
                                  str(get(v, "kind")))) {
      schema = field;
      break;
    }
    if (!schema || !structure(v, schema, schemas, "record", e) ||
        !version(str(get(v, "foreverVersion")))) {
      ok = 0;
      if (!schema)
        error(e, "invalid-kind", "record");
      break;
    }
    for (j = 0; j < i; j++)
      if (equal(m->records[i].id, m->records[j].id)) {
        ok = error(e, "duplicate-id", m->records[i].id);
        break;
      }
    for (j = 0; j < sizeof refs / sizeof refs[0] && ok; j++) {
      if (!get(get(schema, "properties"), refs[j]))
        continue;
      field = get(v, refs[j]);
      if (cJSON_IsArray(field)) {
        cJSON_ArrayForEach(entry, field) if (!reference(m, entry, e, refs[j])) {
          ok = 0;
          break;
        }
      } else
        ok = reference(m, field, e, refs[j]);
    }
    if (get(get(schema, "properties"), "verification"))
      cJSON_ArrayForEach(entry, get(v, "verification")) {
        if (cJSON_IsString(entry)) {
          if (!reference(m, entry, e, "verification"))
            ok = 0;
        } else
          cJSON_ArrayForEach(
              ev,
              get(entry, "evidence")) if (!reference(m, ev, e,
                                                     "verification.evidence"))
              ok = 0;
      }
    if (get(get(schema, "properties"), "claims"))
      cJSON_ArrayForEach(entry, get(v, "claims")) cJSON_ArrayForEach(
          ev, get(entry, "evidence")) if (!reference(m, ev, e,
                                                     "claims.evidence")) ok = 0;
  }
  cJSON_Delete(schemas);
  return ok;
}
static int cmprec(const void *a, const void *b) {
  return strcmp((*(const rec *const *)a)->id, (*(const rec *const *)b)->id);
}
/* Replace the manifest inventory with records, preserving every other input
 * byte. This is deliberately not canonical normalization. */
char *fw_serialize(const fw_model *m) {
  fw_lexer lexer;
  const unsigned char *start, *end, *key_start;
  rec **order;
  char *out, *cursor;
  size_t i, size;
  if (!fw_validate(m, NULL))
    return NULL;
  lexer.p = (const unsigned char *)m->manifest_json;
  lexer.end = lexer.p + strlen(m->manifest_json);
  fw_space(&lexer);
  lexer.p++;
  start = end = NULL;
  while (lexer.p < lexer.end) {
    cJSON *key;
    fw_space(&lexer);
    key_start = lexer.p;
    if (!fw_string(&lexer))
      return NULL;
    key = cJSON_ParseWithLength((const char *)key_start,
                                (size_t)(lexer.p - key_start));
    fw_space(&lexer);
    lexer.p++;
    fw_space(&lexer);
    if (equal(str(key), "records"))
      start = lexer.p;
    if (!fw_value(&lexer, 0)) {
      cJSON_Delete(key);
      return NULL;
    }
    if (start && !end)
      end = lexer.p;
    cJSON_Delete(key);
    fw_space(&lexer);
    if (lexer.p == lexer.end || *lexer.p == '}')
      break;
    lexer.p++;
  }
  if (!start || !end)
    return NULL;
  size = strlen(m->manifest_json) + 8;
  order = malloc((m->count + 1) * sizeof *order);
  if (!order)
    return NULL;
  for (i = 0; i < m->count; i++) {
    order[i] = &m->records[i];
    size += strlen(m->records[i].json) + 2;
  }
  qsort(order, m->count, sizeof *order, cmprec);
  out = malloc(size);
  if (!out) {
    free(order);
    return NULL;
  }
  cursor = out;
  i = (size_t)(start - (const unsigned char *)m->manifest_json);
  memcpy(cursor, m->manifest_json, i);
  cursor += i;
  *cursor++ = '[';
  for (i = 0; i < m->count; i++) {
    size_t length = strlen(order[i]->json);
    if (i)
      *cursor++ = ',';
    memcpy(cursor, order[i]->json, length);
    cursor += length;
  }
  *cursor++ = ']';
  strcpy(cursor, (const char *)end);
  free(order);
  return out;
}

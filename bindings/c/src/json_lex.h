/* Strict JSON lexical preflight for cJSON. Input is bounded before this scan.
 */
typedef struct {
  const unsigned char *p, *end;
} fw_lexer;
static void fw_space(fw_lexer *l) {
  while (l->p < l->end &&
         (*l->p == ' ' || *l->p == '\n' || *l->p == '\r' || *l->p == '\t'))
    l->p++;
}
static int fw_string(fw_lexer *l) {
  if (l->p == l->end || *l->p++ != '"')
    return 0;
  while (l->p < l->end) {
    unsigned c = *l->p++;
    if (c == '"')
      return 1;
    if (c < 32)
      return 0;
    if (c == '\\') {
      unsigned i;
      if (l->p == l->end)
        return 0;
      c = *l->p++;
      if (c == 'u') {
        for (i = 0; i < 4; i++) {
          if (l->p == l->end || !isxdigit(*l->p))
            return 0;
          l->p++;
        }
      } else if (!strchr("\"\\/bfnrt", (int)c))
        return 0;
    }
  }
  return 0;
}
static int fw_value(fw_lexer *l, unsigned depth) {
  unsigned char closing;
  int object;
  if (depth > 64)
    return 0;
  fw_space(l);
  if (l->p == l->end)
    return 0;
  if (*l->p == '"')
    return fw_string(l);
  if (*l->p == '{' || *l->p == '[') {
    object = *l->p++ == '{';
    closing = (unsigned char)(object ? '}' : ']');
    fw_space(l);
    if (l->p < l->end && *l->p == closing) {
      l->p++;
      return 1;
    }
    for (;;) {
      if (object) {
        fw_space(l);
        if (!fw_string(l))
          return 0;
        fw_space(l);
        if (l->p == l->end || *l->p++ != ':')
          return 0;
      }
      if (!fw_value(l, depth + 1))
        return 0;
      fw_space(l);
      if (l->p == l->end)
        return 0;
      if (*l->p == closing) {
        l->p++;
        return 1;
      }
      if (*l->p++ != ',')
        return 0;
    }
  }
  if (*l->p == 't' || *l->p == 'f' || *l->p == 'n') {
    const char *word = *l->p == 't' ? "true" : *l->p == 'f' ? "false" : "null";
    size_t n = strlen(word);
    if ((size_t)(l->end - l->p) < n || memcmp(l->p, word, n))
      return 0;
    l->p += n;
    return 1;
  }
  if (*l->p == '-')
    l->p++;
  if (l->p == l->end)
    return 0;
  if (*l->p == '0')
    l->p++;
  else {
    if (*l->p < '1' || *l->p > '9')
      return 0;
    do {
      l->p++;
    } while (l->p < l->end && isdigit(*l->p));
  }
  if (l->p < l->end && *l->p == '.') {
    l->p++;
    if (l->p == l->end || !isdigit(*l->p))
      return 0;
    do {
      l->p++;
    } while (l->p < l->end && isdigit(*l->p));
  }
  if (l->p < l->end && (*l->p == 'e' || *l->p == 'E')) {
    l->p++;
    if (l->p < l->end && (*l->p == '+' || *l->p == '-'))
      l->p++;
    if (l->p == l->end || !isdigit(*l->p))
      return 0;
    do {
      l->p++;
    } while (l->p < l->end && isdigit(*l->p));
  }
  return 1;
}
static int fw_json_syntax(const unsigned char *data, size_t length) {
  fw_lexer l = {data, data + length};
  if (!fw_value(&l, 0))
    return 0;
  fw_space(&l);
  return l.p == l.end;
}

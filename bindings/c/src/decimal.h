/* Exact bounded decimal comparison. No floating conversion or exponent
 * expansion. */
typedef struct {
  int negative, scale;
  size_t length;
  char digits[4097];
} fw_decimal;
static int decimal_parse(const char *token, fw_decimal *out) {
  const char *p = token;
  size_t n = 0, start = 0;
  int fraction = 0, point = 0, exponent = 0, sign = 1;
  if (!token || strlen(token) > 4096)
    return 0;
  out->negative = *p == '-';
  if (out->negative)
    p++;
  for (; *p && *p != 'e' && *p != 'E'; p++) {
    if (*p == '.') {
      point = 1;
      continue;
    }
    if (*p < '0' || *p > '9')
      return 0;
    out->digits[n++] = *p;
    if (point)
      fraction++;
  }
  if (*p) {
    p++;
    if (*p == '+' || *p == '-') {
      if (*p == '-')
        sign = -1;
      p++;
    }
    for (; *p; p++) {
      if (*p < '0' || *p > '9')
        return 0;
      exponent = exponent * 10 + (*p - '0');
      if (exponent > 1000000)
        return 0;
    }
  }
  if (!n)
    return 0;
  while (start < n && out->digits[start] == '0')
    start++;
  if (start == n) {
    out->length = 1;
    out->digits[0] = '0';
    out->negative = 0;
    out->scale = 0;
    return 1;
  }
  memmove(out->digits, out->digits + start, n - start);
  n -= start;
  out->scale = exponent * sign - fraction;
  while (n > 1 && out->digits[n - 1] == '0') {
    n--;
    out->scale++;
  }
  if (n > 4000 || abs(out->scale + (int)n - 1) > 1000000)
    return 0;
  out->length = n;
  return 1;
}
static int decimal_compare(const fw_decimal *a, const fw_decimal *b) {
  int ae, be, result = 0;
  size_t i, n;
  if (a->negative != b->negative)
    return a->negative ? -1 : 1;
  ae = a->digits[0] == '0' ? -2000000 : a->scale + (int)a->length;
  be = b->digits[0] == '0' ? -2000000 : b->scale + (int)b->length;
  if (ae != be)
    result = ae < be ? -1 : 1;
  else {
    n = a->length > b->length ? a->length : b->length;
    for (i = 0; i < n; i++) {
      char ac = i < a->length ? a->digits[i] : '0',
           bc = i < b->length ? b->digits[i] : '0';
      if (ac != bc) {
        result = ac < bc ? -1 : 1;
        break;
      }
    }
  }
  return a->negative ? -result : result;
}

#include "forever.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _WIN32
#include <fcntl.h>
#include <io.h>
#endif
int main(int argc, char **argv) {
#ifdef _WIN32
  /* The library returns UTF-8 source bytes; CRT text stdout would translate LF.
   */
  if (_setmode(_fileno(stdout), _O_BINARY) == -1)
    return 2;
#endif
  fw_error e = {{0}, {0}};
  fw_model *m;
  int lossless = 0, serialize = 0, i;
  for (i = 2; i < argc; i++) {
    if (!strcmp(argv[i], "lossless"))
      lossless = 1;
    if (!strcmp(argv[i], "serialize"))
      serialize = 1;
  }
  if (argc < 2 || argc > 4)
    return 2;
  m = lossless ? fw_load_lossless(argv[1], &e) : fw_load(argv[1], &e);
  if (!m) {
    printf("{\"loaded\":false,\"valid\":false,\"code\":\"%s\"}\n", e.code);
    return 0;
  }
  if (serialize) {
    char *serialized = fw_serialize(m);
    if (!serialized) {
      fw_free(m);
      return 1;
    }
    puts(serialized);
    free(serialized);
    fw_free(m);
    return 0;
  }
  printf("{\"loaded\":true,\"valid\":%s,\"count\":%zu}",
         fw_validate(m, &e) ? "true" : "false", fw_record_count(m));
  fw_free(m);
  return 0;
}

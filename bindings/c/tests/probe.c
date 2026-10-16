#include "forever.h"
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
  fw_error e = {{0}, {0}};
  fw_model *m;
  if (argc < 2 || argc > 3)
    return 2;
  m = fw_load(argv[1], &e);
  if (!m) {
    printf("{\"loaded\":false,\"valid\":false,\"code\":\"%s\"}\n", e.code);
    return 0;
  }
  if (argc == 3) {
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

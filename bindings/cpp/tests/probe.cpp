#include "forever.hpp"
#include <cstdio>
#include <iostream>
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
  bool lossless = false, serialize = false;
  for (int i = 2; i < argc; i++) {
    if (std::string(argv[i]) == "lossless")
      lossless = true;
    if (std::string(argv[i]) == "serialize")
      serialize = true;
  }
  if (argc < 2 || argc > 4)
    return 2;
  try {
    foreverworks::model m(argv[1], lossless);
    try {
      m.validate();
      if (serialize) {
        std::cout << m.serialize();
        return 0;
      }
      std::cout << "{\"valid\":true,\"count\":" << m.size() << "}";
    } catch (const std::exception &) {
      std::cout << "{\"valid\":false,\"count\":" << m.size() << "}";
    }
  } catch (const std::exception &) {
    std::cout << "{\"valid\":false}";
  }
}

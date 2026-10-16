#include "forever.hpp"
#include <iostream>
int main(int argc, char **argv) {
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

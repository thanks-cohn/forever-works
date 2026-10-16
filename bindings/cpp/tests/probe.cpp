#include "forever.hpp"
#include <iostream>
int main(int argc, char **argv) {
  if (argc < 2 || argc > 3)
    return 2;
  try {
    foreverworks::model m(argv[1]);
    try {
      m.validate();
      if (argc == 3) {
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

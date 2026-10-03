CXX ?= c++
CC ?= cc
CXXFLAGS ?= -std=c++17 -Wall -Wextra -Werror -pedantic -O2
build/forever.o: ../c/src/forever.c ../c/include/forever.h
	mkdir -p build
	$(CC) -std=c11 -Wall -Wextra -Werror -pedantic -O2 -I../c/include -c $< -o $@
build/test: tests/test.cpp include/forever.hpp build/forever.o
	$(CXX) $(CXXFLAGS) -Iinclude -I../c/include tests/test.cpp build/forever.o -o $@
test: build/test
	cd ../.. && bindings/cpp/build/test
clean:
	rm -rf build

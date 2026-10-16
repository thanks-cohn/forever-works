CXX ?= c++
CC ?= cc
CXXFLAGS ?= -std=c++17 -Wall -Wextra -Werror -pedantic -O2
build/forever.o: ../c/src/forever.c ../c/include/forever.h ../c/src/contracts.inc ../c/src/json_lex.h ../c/src/decimal.h ../c/vendor/cJSON.h
	mkdir -p build
	$(CC) -std=c11 -Wall -Wextra -Werror -pedantic -O2 -I../c/include -c $< -o $@
build/cjson.o: ../c/vendor/cJSON.c ../c/vendor/cJSON.h
	mkdir -p build
	$(CC) -std=c11 -DCJSON_NESTING_LIMIT=64 -c $< -o $@
build/test: tests/test.cpp include/forever.hpp build/forever.o build/cjson.o
	$(CXX) $(CXXFLAGS) -Iinclude -I../c/include tests/test.cpp build/forever.o build/cjson.o -o $@
test: build/test
	cd ../.. && bindings/cpp/build/test
clean:
	rm -rf build
build/probe: tests/probe.cpp include/forever.hpp build/forever.o build/cjson.o
	$(CXX) $(CXXFLAGS) -Iinclude -I../c/include tests/probe.cpp build/forever.o build/cjson.o -o $@

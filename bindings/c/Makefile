CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra -Werror -pedantic -O2
build/test: src/forever.c tests/test.c include/forever.h
	mkdir -p build
	$(CC) $(CFLAGS) -Iinclude src/forever.c tests/test.c -o $@
test: build/test
	cd ../.. && bindings/c/build/test
clean:
	rm -rf build

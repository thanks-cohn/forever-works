CC ?= cc
CFLAGS ?= -std=c11 -Wall -Wextra -Werror -pedantic -O2
build/test: src/forever.c tests/test.c include/forever.h src/contracts.inc src/json_lex.h src/decimal.h vendor/cJSON.c vendor/cJSON.h
	mkdir -p build
	$(CC) $(CFLAGS) -DCJSON_NESTING_LIMIT=64 -Iinclude src/forever.c vendor/cJSON.c tests/test.c -lm -o $@
test: build/test
	cd ../.. && bindings/c/build/test
clean:
	rm -rf build
build/probe: src/forever.c vendor/cJSON.c tests/probe.c include/forever.h src/contracts.inc src/json_lex.h src/decimal.h vendor/cJSON.h
	mkdir -p build
	$(CC) $(CFLAGS) -DCJSON_NESTING_LIMIT=64 -Iinclude src/forever.c vendor/cJSON.c tests/probe.c -lm -o $@

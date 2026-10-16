PYTHON ?= python3
.PHONY: test test-python test-javascript test-typescript test-c test-cpp conformance

test: test-python test-javascript test-typescript test-c test-cpp conformance

test-python:
	PYTHONPATH=bindings/python $(PYTHON) -m unittest discover -s bindings/python/tests -v

test-javascript:
	node --test packages/javascript/test/*.test.js

test-typescript:
	npm test

test-c:
	$(MAKE) -C bindings/c clean test

test-cpp:
	$(MAKE) -C bindings/cpp clean test

conformance:
	PYTHONPATH=bindings/python $(PYTHON) scripts/cross_conformance.py

.PHONY: hardening sanitizer
hardening: test-typescript
	$(MAKE) -C bindings/c build/probe
	$(MAKE) -C bindings/cpp build/probe
	$(PYTHON) scripts/check_core_hardening.py

sanitizer:
	$(MAKE) -C bindings/c clean build/probe CFLAGS='-std=c11 -Wall -Wextra -Werror -pedantic -g -O1 -fsanitize=address,undefined -fno-omit-frame-pointer -fno-pie -no-pie'
	$(PYTHON) scripts/check_native_malformed.py

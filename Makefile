.PHONY: test test-python test-typescript test-c test-cpp conformance

test: test-python test-typescript test-c test-cpp conformance

test-python:
	PYTHONPATH=bindings/python python3 -m unittest discover -s bindings/python/tests -v

test-typescript:
	npm test

test-c:
	$(MAKE) -C bindings/c clean test

test-cpp:
	$(MAKE) -C bindings/cpp clean test

conformance:
	PYTHONPATH=bindings/python python3 scripts/cross_conformance.py


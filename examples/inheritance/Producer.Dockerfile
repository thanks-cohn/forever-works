FROM python:3.12-slim@sha256:a6e34c598f2467ed0e9a8d349809fcd8b5c603269512df273a0bb1784edc11b1
WORKDIR /app
COPY --chown=10001:10001 LICENSE /app/LICENSE
COPY --chown=10001:10001 bindings/python/foreverworks /app/foreverworks
COPY --chown=10001:10001 examples/inheritance/shared/runtime.py /app/shared/runtime.py
COPY --chown=10001:10001 examples/inheritance/catalog/server.py /app/catalog/server.py
COPY --chown=10001:10001 examples/inheritance/objects/server.py /app/objects/server.py
RUN mkdir /data && chown 10001:10001 /data
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/app
USER 10001:10001

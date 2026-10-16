FROM python:3.12-slim
WORKDIR /app
COPY LICENSE /app/LICENSE
COPY bindings/python/foreverworks /app/foreverworks
COPY examples/inheritance/shared/runtime.py /app/shared/runtime.py
COPY examples/inheritance/catalog/server.py /app/catalog/server.py
COPY examples/inheritance/objects/server.py /app/objects/server.py
RUN mkdir /data && chown 10001:10001 /data
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/app
USER 10001:10001

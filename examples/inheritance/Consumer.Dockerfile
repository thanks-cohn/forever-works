FROM python:3.12-slim
RUN mkdir /consumer && chown 10001:10001 /consumer
WORKDIR /consumer
USER 10001:10001
CMD ["sleep", "infinity"]

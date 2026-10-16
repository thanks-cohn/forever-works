FROM python:3.12-slim
WORKDIR /app/examples/inheritance
COPY examples/inheritance/run.py /app/examples/inheritance/run.py
COPY examples/inheritance/evaluator/evaluate.py /app/examples/inheritance/evaluator/evaluate.py
RUN mkdir /control && chown 10001:10001 /control
USER 10001:10001
CMD ["sleep", "infinity"]

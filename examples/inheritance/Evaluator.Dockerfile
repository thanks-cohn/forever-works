FROM python:3.12-slim@sha256:a6e34c598f2467ed0e9a8d349809fcd8b5c603269512df273a0bb1784edc11b1
WORKDIR /app/examples/inheritance
COPY --chown=10001:10001 examples/inheritance/run.py /app/examples/inheritance/run.py
COPY --chown=10001:10001 examples/inheritance/evaluator/evaluate.py /app/examples/inheritance/evaluator/evaluate.py
RUN mkdir /control && chown 10001:10001 /control
USER 10001:10001
CMD ["sleep", "infinity"]

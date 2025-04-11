FROM python:latest

WORKDIR /app

RUN pip install mcp


RUN useradd -m appuser
USER appuser

ENTRYPOINT ["python"]
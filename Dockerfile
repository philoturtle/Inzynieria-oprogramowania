FROM python:3.11
WORKDIR /workspace

COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

COPY src/  .
EXPOSE 8000
CMD ["fastapi", "dev", "main.py", "--port", "8000"]
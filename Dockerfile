FROM python:3.11
ARG DEBIAN_FRONTEND=noninteractive

COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt && \
    apt-get update -y && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    apt-get clean && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

WORKDIR /app
COPY src/  .
EXPOSE 8080
CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]
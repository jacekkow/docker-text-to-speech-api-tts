FROM python:3.11

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install -y espeak-ng && apt clean && rm -rf /var/lib/apt/lists/*

RUN addgroup --gid 200 --system app && adduser --uid 200 --gid 200 --home /app app
WORKDIR /app
USER app

COPY --chown=200:200 src/config.py src/download.py src/
RUN python src/download.py

EXPOSE 8000
COPY --chown=200:200 src src
CMD ["python", "src/run.py"]

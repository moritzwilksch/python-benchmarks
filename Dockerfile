FROM python:slim-buster

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

COPY benchmarks.py /app/benchmarks.py

ENTRYPOINT ["python3", "benchmarks.py"]
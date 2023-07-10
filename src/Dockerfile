#syntax=docker/dockerfile:2
#FROM python:3.8-alpine
FROM python:3.10.5

WORKDIR /app
COPY requirements.txt ./app/src2/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./app/src2/requirements.txt

ENV APP=app2

COPY . /app/src2
EXPOSE 8002
CMD ["uvicorn", "src2.main:app","--proxy-headers","--host", "0.0.0.0", "--port", "8002"]
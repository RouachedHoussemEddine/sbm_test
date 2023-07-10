#FROM python:3.8-alpine
FROM python:3.10.5

WORKDIR /app
COPY requirements.txt ./app/src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./app/src/requirements.txt

ENV APP=app

COPY . /app/src
EXPOSE 8000
CMD ["uvicorn", "src2.main:app","--proxy-headers","--host", "0.0.0.0", "--port", "8000"]
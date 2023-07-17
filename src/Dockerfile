#FROM python:3.8-alpine #3.10.5
ARG PARAM1
ARG PARAM2

FROM ${PARAM1}:${PARAM2}

ENV PARAM1=${PARAM1}
ENV PARAM2=${PARAM2}

WORKDIR /app
COPY requirements.txt ./app/src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./app/src/requirements.txt

ENV APP=app

COPY . /app/src
EXPOSE 8000
CMD ["uvicorn", "src.main:app","--proxy-headers","--host", "0.0.0.0", "--port", "8000"]
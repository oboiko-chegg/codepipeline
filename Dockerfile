FROM python:3.6
MAINTAINER Oleg Boiko <oboiko@chegg.com>


RUN apt-get update

COPY . /opt/
RUN pip install -r /opt/requirements.txt

WORKDIR /opt

# CMD ["sh", "-c", "lilbusser sqs_consumer $$INPUT_QUEUE_URL aes.message_bus:message_handler --sqs-endpoint-url $$LILBUSSER_SQS_ENDPOINT"]
CMD ["gunicorn", "--config=gunicorn.conf.py", "app:api"]

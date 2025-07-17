FROM python:3.11-slim

WORKDIR /usr/src/app

COPY . /usr/src/app
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]
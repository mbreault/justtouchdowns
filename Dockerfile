FROM python:2.7
LABEL Mike Breault <mbreault@embersilk.com>
USER root

## update all packages
RUN apt-get update && apt-get install -y 

WORKDIR /root/bin/

COPY src /root/bin/

RUN pip install --upgrade pip

RUN pip install -r /root/bin/requirements.txt

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
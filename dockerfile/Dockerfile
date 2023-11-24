FROM alpine:latest

WORKDIR /usr/src/app

COPY sample.sh /usr/src/app
RUN chmod +x /usr/src/app/sample.sh

ENTRYPOINT ["/usr/src/app/sample.sh"]
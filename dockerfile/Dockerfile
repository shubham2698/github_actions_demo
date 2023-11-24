FROM alpine:latest

WORKDIR /usr/src/app

COPY . .
RUN chmod +x /usr/src/app/sample.sh

ENTRYPOINT ["/usr/src/app/sample.sh"]
FROM alpine:latest

WORKDIR /usr/src/app

COPY . .
RUN chmod +x /usr/src/app/sample.sh

ENTRYPOINT ["node", "/usr/src/app/sample.sh"]
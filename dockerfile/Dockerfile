FROM alpine:latest

WORKDIR /usr/src/app

COPY sample.sh .
RUN ls
RUN tree
RUN chmod +x sample.sh

ENTRYPOINT ["./sample.sh"]
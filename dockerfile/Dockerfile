FROM alpine:latest

WORKDIR /usr/src/app

ENV VARIABLE = ${{ secrets.DOCKERHUB_USERNAME }}

COPY . .
RUN chmod +x /usr/src/app/sample.sh

ENTRYPOINT ["node", "/usr/src/app/sample.sh"]
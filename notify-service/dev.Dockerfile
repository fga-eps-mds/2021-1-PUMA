FROM node:14-alpine

RUN apk update && apk add bash

COPY ./wait-for-it.sh .

WORKDIR /app

COPY ./notify-service/package*.json ./

RUN npm install

COPY ./notify-service .

RUN npm i nodemon -g

CMD ["../wait-for-it.sh", "db:5432", "--", "npm","run","start-dev"]

EXPOSE 3003
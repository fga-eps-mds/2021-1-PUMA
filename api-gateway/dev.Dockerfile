FROM node:14-alpine

RUN apk update && apk add bash

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm i nodemon -g

CMD ["npm","run","start-dev"]

EXPOSE 3004
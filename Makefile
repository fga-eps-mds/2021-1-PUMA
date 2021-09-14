include .env

.PHONY: up-build

up-build:
	chmod +x ./wait-for-it.sh && sudo docker-compose up --build

.PHONY: up

up:
	chmod +x ./wait-for-it.sh && sudo docker-compose up
	

.PHONY: down

down:
	sudo docker-compose down -v

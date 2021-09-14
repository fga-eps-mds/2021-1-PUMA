current_dir := $(shell pwd)
.PHONY: build

build:
	sudo docker build -t frontend -f dev.Dockerfile .

.PHONY: run

run:
	sudo docker run --rm -p 8080:8080 -it -v $(current_dir):/app -v /app/node_modules frontend

.PHONY: dev

dev:
	sudo docker build -t frontend -f dev.Dockerfile . && sudo docker run --rm -p 8080:8080 -it -v $(current_dir):/app -v /app/node_modules frontend
	
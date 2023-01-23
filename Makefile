build:
	docker-compose up --build -d --remove-orphans
up:
	docker-compose up -d
down:
	docker-compose down
logs:
	docker-compose logs
rmi:
	docker rmi $(shell docker images -a -q)
clear:
	docker rm $(shell docker ps -a -q)
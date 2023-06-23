build:
	docker build -t mongo .
run:
	docker run -it -d -p 27017:27017 -v /Users/seop/Documents/GitHub/docker/mongo:/app -v /Users/seop/Documents/GitHub/docker/mongo/data:/data/db --name mongo mongo
exec:
	docker exec -it mongo /bin/bash
logs:
	docker logs mongo
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)

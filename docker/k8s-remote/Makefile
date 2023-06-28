build:
	docker build -t remoteapi .
run:
	docker run -it -d -p 8000:8000 --name remoteapi remoteapi
exec:
	docker exec -it remoteapi /bin/bash
logs:
	docker logs remoteapi
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)

LOG_VAR=DEBUG_DATA_FLOW

DB_NAME=iot

PRJ_NAME=sprc3
YML_NAME=stack.yml

#############################################

config: init deploy
	docker exec influxdb influx -execute "create database ${DB_NAME} with duration inf"
init: 
	docker swarm $@

deploy: ${YML_NAME} ./adaptor/adaptor.py
	docker stack $@ -c ${YML_NAME} ${PRJ_NAME}
ps:
	docker stack $@ ${PRJ_NAME}
ls:
	docker stack $@
services:
	docker stack $@ ${PRJ_NAME}
rm:
	docker stack $@ ${PRJ_NAME}

logs-up:
	export ${LOG_VAR}="true"
logs-down:
	export ${LOG_VAR}="false"


test:
	mosquitto_pub -t "/acasa/el" -f ./tests/test_message
peek:
	docker exec $(shell docker ps -q -f name=influxdb) influx -execute "select * from ${DB_NAME}"
into:
	docker exec -it $(shell docker ps -q -f name=influxdb) influx -precision rfc3339

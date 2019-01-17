LOG_VAR=DEBUG_DATA_FLOW

DB_NAME=iot

#############################################

config: up
	# docker exec influxdb influx -execute "create database ${DB_NAME} with duration inf"
	docker exec influxdb influx -execute "use ${DB_NAME}"

up: docker-compose.yml ./adaptor/adaptor.py
	docker-compose up -d


build:
	docker-compose build

ps:
	docker-compose ps

images:
	docker-compose images

logs:
	docker-compose logs

down:
	docker-compose down


logs-up:
	export ${LOG_VAR}="true"

logs-down:
	export ${LOG_VAR}="false"


test:
	mosquitto_pub -t "/acasa/el" -f ./tests/test_message

peek:
	docker exec influxdb influx -execute "select * from ${DB_NAME}"
	# docker exec -d influxdb influx -execute "use ${DB_NAME}"

into:
	docker exec -it influxdb influx -precision rfc3339

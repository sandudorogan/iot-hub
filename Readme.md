# IoT Hub

A docker swarm-ed Hub for recieving, storing and showing IoT data.
It uses a Mosquitto broker for recieving the messages, InfluxDB for storage and Grafana for showing it. 

All of them are complicent to the SPRC 3rd homework assignment.

## Run
The first run should use:
```bash
make
```
or:
```bash
./run.sh
```

For subsequent runs, use: 
```bash
make deploy
```

To stop the swarm, use:
```bash
make rm
```

## Implementation
* The MQTT broker uses the official Eclipse image. It exposes the default port to all IPs.
* The adaptor/MQTT subscriber is written in Python, and listens at all the topics (#).
* The InfluxDB is just that, the default database. Though at the initial setup, a default database (iot) is created.
* For visualization, Grafana is used. All the neccessarry configurations have been made. 

All is in compliance with the SPRC third assignment. 

Though I'm unclear about the SPRC_DVP variable.

## Author
* Sandu Dorogan
* SPRC team.

## Other
GitHub link: https://github.com/sandudorogan/iot-hub/

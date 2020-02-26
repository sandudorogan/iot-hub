# IoT Hub

A docker swarm-ed Hub for recieving, storing and showing IoT data.
It relies on a Mosquitto broker for recieving the messages, InfluxDB for storage and Grafana for showing it. 

## System requirements
The swarm has been tested on ```Linux``` version of ```Docker 18.01```.

## Run
In a bash, a first run should use:
```bash
make
```
or:
```bash
./run.sh
```
It'll initiate all of the internal assets.

For subsequent runs, use: 
```bash
make deploy
```

To stop the swarm, use:
rand
```bash
make rm
```

## Implementation
* The MQTT broker uses the official Eclipse image. It exposes the default port to all IPs and waits for messages.
* The adaptor/MQTT subscriber is written in Python. It does the subscription and listens to all the topics (#). It is log enabled through an environment variable.
The image was uploaded to DockerHub, for ```docker stach deploy``` command.
* The official InfluxDB docker image is used for data storage. At the initial setup, a default database (called "iot") is created.
* For visual feedback, Grafana is used. All the neccessary configurations have been made and saved in grafana subfolder. It acceses them through a bind mount. Though in future versions the config should be stored as JSON format. 

## Author
* Sandu Dorogan

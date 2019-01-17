import paho.mqtt.client as mqtt
import dateutil.parser
from influxdb import InfluxDBClient

import logging
import json
import os


database = None


def can_log():
    return os.getenv('DEBUG_DATA_FLOW', "false") == "true"

def on_log(client, userdata, level, buf):
    print(userdata)
    print(level)
    print(buf)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if can_log():
        logging.info("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if can_log():
        logging.info("Received a message by topic: " + "[" + msg.topic + "]")

    measurements = json.loads(msg.payload)

    # timestamp = dateutil.parser.parse(measurements['timestamp']) if measurements.get('timestamp') else None
    timestamp = measurements['timestamp'] if measurements.get('timestamp') else None
    location = msg.topic.split("/")[1]
    machine = msg.topic.split("/")[2]

    if can_log():
        info = timestamp if timestamp else "NOW"
        logging.ingo("Data timestamp is: " + info)

    to_send = []
    for key in measurements:
        # delete the useless info
        if not isinstance(measurements[key], str):
            to_send.append({'measurement': key,
                            'tags': {'location': location,
                                        'machine': machine},
                            'fields': {'data': measurements[key]},
                            'time': str(timestamp)}) 
            if can_log():
                logging.info(location + "." + machine + "." + key + " " + measurements[key])

    # send data to database
    try:
        database.write_points(to_send, database="iot", time_precision="u")
        # print(database.write(to_send))
    except Exception as e:
        print("the error is: ")
        print(e)



def main():
    # config the logging
    logging.basicConfig(format='%(asctime)s %(message)s',
                        level=logging.INFO,
                        datefmt='%d-%m-%Y %H:%M:%S')

    # connect to influxdb
    global database
    database = InfluxDBClient(host="influxdb", database="iot")

    # connect and config myself as a mosquitto client
    client = mqtt.Client()
    # client.on_log = on_log
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mosquitto", 1883, 60)

    client.enable_logger(logging)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

    # release the resources
    database.close()


if __name__ == "__main__":
    main()

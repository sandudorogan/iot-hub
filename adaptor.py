import paho.mqtt.client as mqtt
import logging
import os

true = "true"
false = "false"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    logging.info("god a message")
    logging.info(f"The variable is {os.getenv('INTERNAL_DEBUG_DATA_FLOW', false)}")
    if os.getenv('INTERNAL_DEBUG_DATA_FLOW', false) == false:
        logging.info(client)
        logging.info(userdata)
        logging.info(msg.topic + " " + str(msg.payload))


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                        level=logging.INFO,
                        datefmt='%d-%m-%Y %H:%M:%S')

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mosquitto", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()


if __name__ == "__main__":
    main()

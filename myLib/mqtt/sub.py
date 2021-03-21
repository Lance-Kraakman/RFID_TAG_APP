# subscriber
import time

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('mqtt://localhost:9999/')


def on_connect(client, userdata, flags, rc):
    print("Connected to a broker!")
    client.subscribe("test")


def on_message(client, userdata, message):
    print(message.payload.decode())

client.on_connect = on_connect
client.on_message = on_message

while True:
    print(client.is_connected())
    client.loop_start()
    client.on_connect = on_connect
    client.on_message = on_message
    time.sleep(30)
    client.loop_stop()

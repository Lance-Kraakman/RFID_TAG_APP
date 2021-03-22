import paho.mqtt.client as mqtt
from random import randrange
import time


class MqttSubscriber():
    def __init__(self, mqttBroker='localhost', clientName=""):
        self._mqttBroker = mqttBroker
        self._mqttClient = mqtt.Client(clientName)

    def publishMessage(self, topic, data):
        self.getMqttClient().publish(topic, data)
        print("Published: %s, To Topic: %s" % (topic, data))

    # TO-DO
    # Function should start a MDNS service and advertise mqtt service on the network <3
    def advertiseServices(self):
        pass

    def getMqttClient(self):
        return self._mqttClient

    def getMqttBroker(self):
        return self._mqttBroker

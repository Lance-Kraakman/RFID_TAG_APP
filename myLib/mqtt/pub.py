import paho.mqtt.client as mqtt
from random import randrange
import time


class MqttClient:
    def __init__(self, mqttBroker='localhost', clientName=""):
        self._mqttBroker = mqttBroker
        self._mqttClient = mqtt.Client(clientName)
        self.getMqttClient().connect(mqttBroker)

    def publishMessage(self, topic, data):
        ret = self.getMqttClient().publish(topic, data)
        print("Published: %s, To Topic: %s" % (topic, data))
        return ret.is_published()

    def on_message(self, client, userdata, message):
        print("received message: ", str(message.payload.decode("utf-8")))

    def subscribeToTopic(self, topic):
        self.getMqttClient().loop_start()
        res, m_id = self.getMqttClient().subscribe(topic)
        self.getMqttClient().on_message = self.on_message
        self.getMqttClient().loop_stop()
        return res

    # TO-DO
    # Function should start a MDNS service and advertise mqtt service on the network <3
    def advertiseServices(self):
        pass

    def getMqttClient(self):
        return self._mqttClient

    def getMqttBroker(self):
        return self._mqttBroker

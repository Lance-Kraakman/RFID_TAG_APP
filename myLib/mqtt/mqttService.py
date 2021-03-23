import paho.mqtt.client as mqtt
from random import randrange
import time
TOPIC_INDEX = 0
DATA_INDEX = 1


class MqttClient:
    messageList = []

    def __init__(self, mqttBroker='localhost'):
        self._mqttBroker = mqttBroker
        self._mqttClient = mqtt.Client()
        self.getMqttClient().connect(mqttBroker)
        self.getMqttClient().loop_start()

    def publishMessage(self, topic, data):
        ret = self.getMqttClient().publish(topic, data)
        print("Published: %s, To Topic: %s" % (topic, data))
        return ret.is_published()

    def on_message(self, client, userdata, message):
        data = str(message.payload.decode("utf-8"))
        print("received message: ", str(message.payload.decode("utf-8")))
        self.messageList.append(tuple((message.topic, data)))
        print(message.topic)

    def subscribeToTopic(self, topic):
        self.getMqttClient().loop_start()
        res, m_id = self.getMqttClient().subscribe(topic)
        self.getMqttClient().on_message = self.on_message
        return res

    # returns a copy of the messages with a specified topic. Does not remove them from the list
    def getMessageListWithTopic(self, topic):
        returnList = []
        print(returnList)
        messageList = self.getMessageList()
        if messageList is not None:
            for messageDict in self.getMessageList():
                if messageDict[TOPIC_INDEX] == topic:
                    print(returnList)
                    returnList.append(tuple((messageDict[TOPIC_INDEX], messageDict[DATA_INDEX])))
        print(returnList)
        return returnList

    def getMessageList(self):
        return self.messageList

    # TO-DO
    # Function should start a MDNS service and advertise mqtt service on the network <3
    def advertiseServices(self):
        pass

    def getMqttClient(self):
        return self._mqttClient

    def getMqttBroker(self):
        return self._mqttBroker

    def mqttDisconnect(self):
        self.getMqttClient().loop_stop()
        self.getMqttClient().disconnect()
        print("Goodbye, Disconnecting mqtt client :'(")

    # Gets the result of the last message in a topic
    def getLastMessage(self, topic):
        messageList = self.getMessageListWithTopic(topic)
        # Get the Last received desktop-application message
        if messageList is not None:
            lastMessage = messageList[-1]
        else:
            return None
        # Get the state
        return lastMessage

    # Reads a item from the first item list and removes it from the lists
    def readAndRemove(self):
        return self.getMessageList().pop(0)



# Runnning this script will create a mqtt object which when a key is pressed simulates a RFID tag being pressed
#from myLib.mqtt import mqttService
import mqttService
import json
from random import randint

listLength = 8
uuidList = [[99, 2, 23, 2], [4, 345, 23, 23], [3, 345, 8, 23], [5, 33, 33, 23], [45, 345, 34, 23], [99, 2, 23, 2],
            [99, 2, 23, 7], [99, 2, 27, 2]]


def getRandomTag():
    rand = randint(0, listLength - 1)
    return json.dumps({'UUID': uuidList[rand]})


print("Initialize MQTT client")
myMqttClient = mqttService.MqttClient()
myMqttClient.subscribeToTopic("desktop-application")
# myMqttClient.publish("desktop-application", 1)  # This needs to be in desktop-app code not simulator
# Let the ESP32 know that the application is ready to receive messages.
# In practice we will only publish messages if we recieve a 1 from topic desktop-application

desktop_application_connected = 0  # we need to check if the desktop app is subscribed before we send any messages
inputString = ""

while True:
    try:
        inputString = input("Input rfid to generate a dummy tag or quit to quit\n")

        if inputString.lower() == "rfid":
            # generate rfid tag
            randomTag = json.dumps(getRandomTag())
            print("Generated RFID dummy Tag: %s \n" % randomTag.__str__())
        elif inputString.lower() == "quit":
            print("QUITTING RFID TAG SIMULATOR")
            break
        else:
            print("Unrecognised Command")
    except Exception as err:
        print("Exception Occurred")

myMqttClient.mqttDisconnect()

jsonData = json.dumps((['foo', {'bar': ('baz', None, 1.0, 2)}]))
jsonData = json.dumps({'UUID':[345, 345, 23, 23]})


# JSON data format
# {
#         "RFID TAG ARRAY":       [{
#                         "UUID": [136, 4, 145, 11]
#                 }, {
#                         "UUID": [136, 4, 153, 11]
#                 }, {
#                         "UUID": [136, 4, 171, 11]
#                 }, {
#                         "UUID": [136, 4, 171, 11]
#                 }, {
#                         "UUID": [136, 4, 163, 11]
#                 }]
# }
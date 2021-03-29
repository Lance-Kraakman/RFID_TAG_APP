# Runnning this script will create a mqtt object which when a key is pressed simulates a RFID tag being pressed
from myLib.mqtt import mqttService
import json
from random import randint

MAX_NUMBER_OF_TAGS_IN_LIST = 13
listLength = 8
uuidList = [[99, 2, 23, 2], [4, 345, 23, 23], [3, 345, 8, 23], [5, 33, 33, 23], [45, 345, 34, 23], [99, 2, 23, 2],
            [99, 2, 23, 7], [99, 2, 27, 2]]


def getRandomTag():
    rand = randint(0, listLength - 1)
    returnJson = {}
    returnJson["RFID TAG ARRAY"] = []
    UUID_OBJ = {"UUID": uuidList[rand].copy()}
    returnJson["RFID TAG ARRAY"].append(UUID_OBJ)
    print(returnJson['RFID TAG ARRAY'])
    return returnJson


def generateRandomTagList():
    randomTagList = []
    number_of_tags = randint(0, MAX_NUMBER_OF_TAGS_IN_LIST)
    for i in range(0, number_of_tags):
        randomTagList.append(json.dumps(getRandomTag()))
    print(randomTagList)
    return randomTagList


# Gets the result of the last message in a topic
def getLastMessage(topic):
    messageList = myMqttClient.getMessageListWithTopic(topic)
    # Get the Last received desktop-application message
    lastMessage = messageList[len(messageList)]
    return lastMessage[topic]


print("Initialize MQTT client")
myMqttClient = mqttService.MqttClient()
myMqttClient.subscribeToTopic("desktop-application")

# desktop published a notification which we subscribe 'desktop-application'. If we receive a 1 from this topic the
# desktop app is ready to communicate and we then send the rfid tags
desktop_application_connected = 0
inputString = ""

while True:
    try:
        inputString = input("Input rfid to generate a dummy tag or quit to quit\n")
        if inputString.lower() == "rfid":  # generates a list of RFID scan notifications
            print("OK")
            lastMessage = myMqttClient.getLastMessage('desktop-application')
            print(lastMessage)
            print("OK")

            #print("Last messae is %s" % lastMessage[mqttService.DATA_INDEX])
            if lastMessage is not None:
                desktop_application_connected = lastMessage[mqttService.DATA_INDEX]
                print("Last message is %s" % lastMessage[mqttService.DATA_INDEX])

            # Generate and publish RFID tags if the "Desktop Application is connected"
            if int(desktop_application_connected) == 1:  # Now that the desktop application is connected we will send all of the messages
                print("OK")
                randomTagList = generateRandomTagList()
                for tag in randomTagList:
                    print(tag)
                    myMqttClient.publishMessage("rfid", tag)

        elif inputString.lower() == "quit":
            print("QUITTING RFID TAG SIMULATOR")
            break
        else:
            print("Unrecognised Command")
    except Exception as err:
        print(err)
        print("Exception Occurred")

myMqttClient.mqttDisconnect()

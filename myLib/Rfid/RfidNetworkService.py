import json as js
import numpy as np
from myLib.Item import Item as it
from myLib.Rfid.Rfid import *
from myLib.mqtt import mqttService
import time


class RfidNetworkService:
    rfidTagList = []

    def setupNetwork(self):
        self.mqttClient = mqttService.MqttClient()
        self.mqttClient.publishMessage("desktop-application", 1)
        self.mqttClient.subscribeToTopic("rfid")

    # Network Loop Method runs forever and updates the database.
    # Must be run in a thread
    def runNetworkLoop(self):
        self.setupNetwork()

        interrupted = False
        while not interrupted:
            try:
                # Do stuff
                time.sleep(2)
                # Check if we have received messages over mqtt
                messagesReceived = []
                messagesReceived = self.mqttClient.getAndRemoveMessageList()
                if messagesReceived is not None:
                    for message in messagesReceived:
                        print(message[mqttService.DATA_INDEX])  # Print the UUID for every received message
                        # update the database
                        self.processRfidTagInputs(message[mqttService.DATA_INDEX])


            except Exception as err:
                interrupted = True
                print(err)

        self.mqttClient.mqttDisconnect()

    def getRfidTagsFromDB(self):
        rfidItemList = it.Item.getItemsFromDatabase()  # Gets all of the items from the database
        # print(rfidItemList)
        updatedRfidList = []
        for itm in rfidItemList:
            updatedRfidList.append(
                rf.RfidTag(name=itm.getName(), uuid=int(itm.getUUID()), status=itm.getTagStatus()))
        return updatedRfidList

    def setRfidTagsFromJson(self, string_input):
        rfidListInput = self.getRfidTagsFromJsonString(string_input)
        self.setRfidTagList(rfidListInput)

    # Updates the database from JSON input string of RFID tags
    # IF the RFID tags are already in the database
    def processRfidTagInputs(self, string_input):

        rfidInputList = self.getRfidTagsFromJsonString(string_input)  # Get Rfid List From json string
        rfidInputListDatabase = self.getRfidTagsFromDB()  # Gets all of the rfid Lists From the Database

        print("Input List" + rfidInputList.__str__())
        print("rfidInputListDatabase List" + rfidInputListDatabase[0].__str__())

        itemInDb = False
        for rfidTag in rfidInputList:
            for dbTag in rfidInputListDatabase:
                if rfidTag.getUUID() == dbTag.getUUID():
                    try:
                        dbTag.setTagStatus(int(not dbTag.getTagStatus()))
                        dbTag.updateDatabaseTag()  # Function Edits Tag In Database
                    except Exception as err:
                        print(err)
                    itemInDb = True
                    break

            if not itemInDb:
                try:
                    rfidTag.addToDatabase()  # Function adds httpTag to Database
                except Exception as err:
                    print(err)
            itemInDb = False  # Set Flag To False no matter what

    def getRfidTagsFromJsonString(self, string_input):
        rfidTagList = []
        try:
            string_input = string_input.replace("'", "\"") # Make sure it is a 'proper' JSON string
            rfid_tag_array = js.loads(string_input)

            if rfid_tag_array.get('RFID TAG ARRAY') is not None:
                rfid_tag_array = rfid_tag_array['RFID TAG ARRAY']

            for rfid in rfid_tag_array:
                uuidInts = rfid['UUID']
                uuidInt = 0
                uuidIntLength = len(uuidInts)
                for i in range(0, uuidIntLength):
                    uuidInt += (uuidInts[i]) << (i * 8)
                    print(i * 8)

                rfidTagList.append(RfidTag(uuid=uuidInt, status=TAGGED_IN))

        except Exception as ex:
            print(ex.__str__())
            print("Recieved %s" % string_input)
        finally:
            return rfidTagList

    def setRfidTagList(self, listToAppend):
        self.rfidTagList.clear()
        for item in listToAppend:
            if isinstance(item, RfidTag):
                self.getRfidTagList().append(item)

    def getRfidTagList(self):
        return self.rfidTagList

    def getItemCount(self):
        return len(self.rfidTagList)

    def getRfidList(self):
        return self.rfidTagList

    def printRfidTags(self):
        printString = "RFID ITEMS:\n"
        for itm in self.rfidTagList:
            printString = printString + itm.__str__() + " :\n"
        print(printString)



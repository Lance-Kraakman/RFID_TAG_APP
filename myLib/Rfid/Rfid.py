import json as js
import numpy as np
from myLib.Item import Item as it
from myLib.Rfid import Rfid as rf

TAGGED_IN = 0
TAGGED_OUT = 1


class RfidTag:
    compartmentID = 0
    UUID = 0
    name = ""
    status = TAGGED_IN

    def __init__(self, name="", uuid=0, status=0, compartmentID=0):
        self.UUID = uuid
        self.name = name
        self.status = status

    def updateDatabaseTag(self):  # Edits the parsed tag in the database
        # Create Generic ITEM object from RFID
        updateItem = it.Item(self.getName(), self.getUUID(), self.getTagStatus(), self.getCompartmentID())
        # Update Item From DB
        updateItem.updateDbItemByUUID()

    def addToDatabase(self):
        tagItem = it.Item(Name=self.getName(), UUID=self.getUUID(), TagStatus=(self.getTagStatus()))
        it.Item.insertItemIntoDatabase(tagItem)

    def __str__(self):
        return "UUID %d: Name %s: Status %d" % (self.UUID, self.name, self.status)  # Make this fixed length for display

    def getUUID(self):
        return self.UUID

    def getTagStatus(self):
        return self.status

    def setTagStatus(self, status):
        self.status = status

    def getName(self):
        return self.name

    def getCompartmentID(self):
        return self.compartmentID

    def setCompartmentID(self, compartmentID):
        self.compartmentID = compartmentID


class RfidTagList:
    rfidTagList = []

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

    def getRfidTagsFromDB(self):
        rfidItemList = it.Item.getItemsFromDatabase()  # Gets all of the items from the database
        #print(rfidItemList)
        updatedRfidList = []
        for itm in rfidItemList:
            updatedRfidList.append(
                rf.RfidTag(name=itm.getName(), uuid=int(itm.getUUID()), status=itm.getTagStatus()))
        return updatedRfidList

    def setRfidTagsFromHttpJson(self, string_input):
        rfidListInput = self.getRfidTagsFromJsonString(string_input)
        self.setRfidTagList(rfidListInput)

    # Updates the database from JSON input string of RFID tags
    # IF the RFID tags are already in the database
    def processRfidTagInputs(self, string_input):
        rfidInputListHttp = self.getRfidTagsFromJsonString(string_input)  # Get Rfid List From Http Response
        rfidInputListDatabase = self.getRfidTagsFromDB()  # Gets all of the rfid Lists From the Database
        itemInDb = False
        for httpTag in rfidInputListHttp:
            for dbTag in rfidInputListDatabase:
                if httpTag.getUUID() == dbTag.getUUID():
                    try:
                        dbTag.setTagStatus(int(not dbTag.getTagStatus()))
                        dbTag.updateDatabaseTag()  # Function Edits Tag In Database
                    except Exception as err:
                        print(err)
                    itemInDb = True
                    break

            if not itemInDb:
                try:
                    httpTag.addToDatabase()  # Function adds httpTag to Database
                except Exception as err:
                    print(err)
            itemInDb = False  # Set Flag To False no matter what

    def getRfidTagsFromJsonString(self, string_input):
        rfidTagList = []
        try:
            rfid_tag_array = js.loads(string_input)
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

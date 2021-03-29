import json as js
import numpy as np
from myLib.Item import Item as it
from myLib.Rfid import Rfid as rf
from myLib.mqtt import mqttService

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



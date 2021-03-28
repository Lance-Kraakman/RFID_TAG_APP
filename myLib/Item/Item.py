from myLib.Database import databaseAbstraction as db


class Item:
    __UUID = 0
    __name = ""
    __TagStatus = 0
    __CompartmentID = 0
    __databaseObject = db.databaseAbstraction("/home/lance/PycharmProjects/RFID_TAG_APP/databases/tag_database.db", "",
                                              "")

    def __init__(self, Name="", UUID=0, TagStatus=0, CompartmentID=0):
        self.setName(Name)
        self.setUUID(UUID)
        self.setTagStatus(TagStatus)
        self.setCompartmentID(CompartmentID)

    @classmethod
    def getItemsFromDatabase(cls):  # gets all Compartments From Database
        compartmentList = cls.__databaseObject.selectAllFromTable("ITEM_LIST")
        return cls.createObjectList(compartmentList)

    # Parse in Item ID
    @classmethod
    def getItemFromUUID(cls, itemsUUID):  # gets all Compartments From Database
        itm = cls.__databaseObject.selectFromTableWhereFieldEqualsValue("ITEM_LIST", "UUID", itemsUUID)[0]
        print("Length of item: " + len(itm).__str__())
        print(itm.__str__())
        print(itm[0].__str__())
        print(itm[1].__str__())
        # for i in range(0,4):
        return Item(itm[0], itm[1], itm[2], itm[3])

    @classmethod
    def getItemsFromCompartmentID(cls, compartmentID):  # gets all Compartments From Database
        itms = cls.__databaseObject.selectFromTableWhereFieldEqualsValue("ITEM_LIST", "COMPARTMENT_ID", compartmentID)
        return cls.createObjectList(itms)

    def deleteItemFromDatabase(self):
        try:
            self.__databaseObject.deleteFromTableWhereFieldEqualsValue("ITEM_LIST", "UUID", self.getUUID())
            print("DELETING FROM DATA BASE")
        except Exception as err:
            print("Deleting Item from database failed")

    def updateDbItemByUUID(self):
        print("Update Item in the database")
        try:
            self.__databaseObject.updateFromTableWhereFieldNameEqualsAndValueNameEqualsValue(
                tableName='ITEM_LIST', fieldEquals=self.getUUID(), fieldName='UUID', valueName='TAG_STATUS', valueEquals=self.getTagStatus())
        except Exception as err:
            print(err.__str__())
            print("Exception Occured")

    def deleteItemsFromDatabase(self, itemList):
        for item in itemList:
            try:
                self.__databaseObject.deleteFromTableWhereFieldEqualsValue("ITEM_LIST", "UUID", item.getUUID)
            except Exception as err:
                print("Deleting Item from database failed")

    @classmethod
    def insertItemIntoDatabase(cls, itemToInsert):
        if isinstance(itemToInsert, Item):
            Cols = ["NAME", "UUID", "TAG_STATUS", "COMPARTMENT_ID"]
            Values = [itemToInsert.getName(), itemToInsert.getUUID(), itemToInsert.getTagStatus(),
                      itemToInsert.getCompartmentID()]
            cls.__databaseObject.insertIntoTableWhereColNamesEqualWhereValuesEqual("ITEM_LIST", Cols, Values)
        else:
            print("Not of type item")

    @classmethod
    def createObjectList(cls, dataList):
        objectList = []
        for itm in dataList:
            objectList.append(Item(itm[0], itm[1], itm[2], itm[3]))
        return objectList

    # Getters and Setters
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setUUID(self, UUID):
        self.__UUID = UUID

    def getUUID(self):
        return self.__UUID

    def setTagStatus(self, TagStatus):
        self.__TagStatus = TagStatus

    def getTagStatus(self):
        return self.__TagStatus

    def setCompartmentID(self, CompartmentID):
        self.__CompartmentID = CompartmentID

    def getCompartmentID(self):
        return self.__CompartmentID

    def __str__(self):
        return ("Name : %s, UUID : %s, TagStatus : %s" % (self.__name, self.__UUID, self.__TagStatus))

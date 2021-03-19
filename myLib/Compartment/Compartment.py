from myLib.Item import Item
from myLib.Database import databaseAbstraction as db
from myLib.Item import Item as it


class Compartment:
    __ItemList = []  # List of items in compartment
    __LedNumber = -1  # number of compartment for GPIO
    __CompartmentID = -1
    __StorageSectionID = -1
    __CompartmentName = ""

    __databaseObject = db.databaseAbstraction("/home/lance/PycharmProjects/RFID_TAG_APP/databases/tag_database.db", "", "")

    def __init__(self, StorageSectionID=-1, ledNumber=-1, CompartmentID=-1, compartmentName=""):
        self.setLedNumber(ledNumber)
        self.setCompartmentID(CompartmentID)
        self.setStorageSectionID(StorageSectionID)
        self.setCompartmentName(compartmentName)

    @classmethod
    def getCompartmentsFromDatabase(cls):  # Should return a list of compartment objects with there list of items in
        # each compartment
        compartmentList = cls.createObjectList(cls, cls.__databaseObject.selectAllFromTable("COMPARTMENT"))
        for cmp in compartmentList:
            itemList = it.Item().getItemsFromCompartmentID(cmp.getCompartmentID())
            print("ITEM LIST : " + itemList.__str__())
            cmp.setItemList(itemList)
        return compartmentList

    @classmethod
    def getCompartmentsFromDatabaseWhereStorageSectionIdEquals(cls, sectionID):  # Should return a list of compartment objects with there list of items in
        # each compartment
        compartmentList = cls.createObjectList(cls, cls.__databaseObject.selectFromTableWhereFieldEqualsValue("COMPARTMENT", "SECTION_ID", sectionID))
        for cmp in compartmentList:
            itemList = it.Item().getItemsFromCompartmentID(cmp.getCompartmentID())
            print("ITEM LIST : " + itemList.__str__())
            cmp.setItemList(itemList)
        return compartmentList

    def deleteCompartmentFromDatabase(self):  # delete Compartment and child items from compartment
        itemsToDelete = self.getItemList()
        print("items to delete: " + itemsToDelete.__str__())
        try:
            self.__databaseObject.deleteFromTableWhereFieldEqualsValue("COMPARTMENT", "COMPARTMENT_ID",
                                                                       self.getCompartmentID())
        except Exception as err:
            print("Deleting Compartment from database failed")

        for item in itemsToDelete:
            try:
                item.deleteItemFromDatabase()
                print(item)
            except Exception as err:
                print("Deleting Item from database failed")

    def insertCompartmentIntoDatabase(self):  # Insert Compartment and child items from compartment
        try:
            if isinstance(self, Compartment):
                Cols = ["SECTION_ID", "LED_IO_NUMBER", "COMPARTMENT_ID", "COMPARTMENT_NAME"]
                Values = [self.getStorageSectionID(), self.getLedNumber(), self.getCompartmentID(),
                          self.getCompartmentName()]
                self.__databaseObject.insertIntoTableWhereColNamesEqualWhereValuesEqual("COMPARTMENT", Cols, Values)
                for item in self.getItemList():
                    it.Item().insertItemIntoDatabase(item)
            else:
                print("Not of type compartment")
        except Exception as err:
            print("Inserting Compartment to database failed")

    def setItemList(self, itemlistToAppend):
        itemsCorrectObjectType = True  # Only set items list equal if all items in list are of correct type
        for itm in itemlistToAppend:
            if not isinstance(itm, it.Item):
                itemsCorrectObjectType = False
                break
        if itemsCorrectObjectType:
            self.__ItemList = list(itemlistToAppend)

    def appendItemToItemList(self, itemToAppend):
        itemToAppend.setCompartmentID(self.getCompartmentID())
        print(itemToAppend)
        if isinstance(itemToAppend, type(it.Item())):  # Check if we are appending the right type of object first
            print("appendeded")
            self.getItemList().append(itemToAppend)
        print("maybe ?")

    # Getters and Setters
    def setLedNumber(self, LedNumber):
        self.__LedNumber = LedNumber

    def getLedNumber(self):
        return self.__LedNumber

    def getItemList(self):
        return self.__ItemList

    def setStorageSectionID(self, StorageSectionID):
        self.__StorageSectionID = StorageSectionID

    def getStorageSectionID(self):
        return self.__StorageSectionID

    def setCompartmentID(self, CompartmentID):
        self.__CompartmentID = CompartmentID

    def getCompartmentID(self):
        return self.__CompartmentID

    def setCompartmentName(self, CompartmentName):
        self.__CompartmentName = CompartmentName

    def getCompartmentName(self):
        return self.__CompartmentName

    def __str__(self):
        return ("Compartment ID: " + self.getCompartmentID().__str__())

    def createObjectList(self, dataList):
        objectList = []
        for itm in dataList:
            objectList.append(Compartment(itm[0], itm[1], itm[2], itm[3]))
        return objectList

from myLib.Compartment import Compartment as cp
from myLib.Database import databaseAbstraction as db


class StorageSection:
    __CompartmentList = []
    __StorageSectionID = -1
    __Name = ""
    __databaseObject = db.databaseAbstraction("databases/tag_database.db", "", "")

    def __init__(self, name="", compartmentList=[], storageSectionID=-1):
        self.__Name = name
        self.setCompartmentList(compartmentList)
        self.setStorageSectionID(storageSectionID)

    # def getStorageSectionsFromDatabase(self):  # gets all Compartments From Database
    #     StorageSectionList = self.__databaseObject.selectAllFromTable("STORAGE_SECTION")
    #     return StorageSectionList

    # Parse in Compartment ID
    @classmethod
    def getStorageSectionListFromDatabase(cls):  # gets all Compartments From Database
        StorageSectionList = cls.createObjectList(cls, cls.__databaseObject.selectAllFromTable("STORAGE_SECTION"))
        for storageSection in StorageSectionList:
            compartments = cp.Compartment().getCompartmentsFromDatabaseWhereStorageSectionIdEquals(storageSection.getStorageSectionID())
            storageSection.setCompartmentList(compartments)
        return StorageSectionList

    @classmethod
    def getStorageSectionFromDatabaseWhereSectionIdEquals(cls, sectionID):  # gets all Compartments From Database
        StorageSectionList = cls.createObjectList(cls, cls.__databaseObject.selectFromTableWhereFieldEqualsValue("STORAGE_SECTION", "SECTION_ID", sectionID))
        for storageSection in StorageSectionList:
            compartments = cp.Compartment().getCompartmentsFromDatabaseWhereStorageSectionIdEquals(
                storageSection.getStorageSectionID())
            storageSection.setCompartmentList(compartments)
        return StorageSectionList

    def deleteStorageSectionFromDatabase(self):
        compartmentsToDelete = self.getCompartmentList()
        try:
            self.__databaseObject.deleteFromTableWhereFieldEqualsValue("STORAGE_SECTION", "SECTION_ID",
                                                                       self.getStorageSectionID())
        except Exception as err:
            print("Deleting STORAGE_SECTION from database failed")
        for compartment in compartmentsToDelete:
            try:
                compartment.deleteCompartmentFromDatabase()
                print(compartment)
            except Exception as err:
                print("Deleting Item from database failed")

    def insertStorageSectionIntoDatabase(self, storageSectionToInsert): # THIS  NEEDS TO BE UPDATED !!!
        if isinstance(storageSectionToInsert, StorageSection):
            Cols = ["SECTION_ID", "NAME"]
            Values = [storageSectionToInsert.getStorageSectionID(), storageSectionToInsert.getName()]
            self.__databaseObject.insertIntoTableWhereColNamesEqualWhereValuesEqual("STORAGE_SECTION", Cols, Values)
        else:
            print("Not of type storageSectionToInsert")

    # Getters and Setters
    def setCompartmentList(self, compartmentlistToAppend):
        correctObjectType = True  # Only set list equal if all items in list are of correct type
        for cmprtmnt in compartmentlistToAppend:
            if not isinstance(cmprtmnt, cp.Compartment):
                correctObjectType = False
                break
        if correctObjectType:
            self.__CompartmentList = compartmentlistToAppend

    def appendCompartmentList(self, itemToAppend):
        if isinstance(itemToAppend, cp.Compartment):  # Check if we are appending the right type of object first
            self.__CompartmentList.append(itemToAppend)

    def setName(self, Name):
        self.__Name = Name

    def getName(self):
        return self.__Name

    def setStorageSectionID(self, StorageSectionID):
        self.__StorageSectionID = StorageSectionID

    def getStorageSectionID(self):
        return self.__StorageSectionID

    def getCompartmentList(self):
        return self.__CompartmentList

    def createObjectList(self, dataList):
        objectList = []
        for itm in dataList:
            objectList.append(StorageSection(storageSectionID=itm[0], name=itm[1]))
        return objectList

    def __str__(self):
        return "Name: %s SectionID: %s" % (self.getName(), self.getStorageSectionID())

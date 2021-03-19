# This is a sample Python script.
from myLib.webClient import httpsClient
# Press Shift+F10 to execute it or replace it with your code.
# Press Doub8le Shift to search everywhere for classes, files, tool windows, actions, and settings.from'==
from myLib.Item import Item as it
from myLib.Database import databaseAbstraction as db
from myLib.Compartment import Compartment as cp
from myLib.Compartment import *
from myLib.Rfid import Rfid

from myLib.StorageSection import StorageSection as ss
from myLib.Controller import MainController as mc
from myLib.Controller import MainController
import sqlite3 as sq

myApp = MainController.MainController()


def app():
    print("-------------------------APP--START----------------------------")

    # mainController = mc.MainController()
    compartment = cp.Compartment(1, 91, 9, "Book Case 1")
    dummyItem = it.Item("Dummy Item", "aasdsd", 0)
    compartment.appendItemToItemList(dummyItem)
    compartment.insertCompartmentIntoDatabase()

    storageSections = ss.StorageSection().getStorageSectionFromDatabaseWhereSectionIdEquals(1)
    print("~~~~~~~")
    for storageSect in storageSections:
        print("ok" + storageSect.__str__())

        storageSect.deleteStorageSectionFromDatabase()

    for storageSect in storageSections:
        print("ok" + storageSect.__str__())
    print("~~~~~~~")

    compartmentList = cp.Compartment().getCompartmentsFromDatabaseWhereStorageSectionIdEquals(1)
    print(compartmentList)
    compartmentList[0].deleteCompartmentFromDatabase()

    print("-------------------------------------------------------------------------------------")

    rfidTag = Rfid.RfidTag()

    webClientTest = httpsClient.HttpsClient()
    uuidString = webClientTest.test_request()

    Rfid.uuidListFromString(uuidString)

    print("-------------------------------------------------------------------------------------")


# compartmentList = compartment.getCompartmentsFromDatabase()
#  print(compartmentList)

# singleCompartment = compartment.getCompartmentFromDatabase(0)
# print(singleCompartment)

# compartment.insertCompartmentIntoDatabase(compartment)
# compartment.insertCompartmentIntoDatabase(":(")

# New Compartment Object
#  bookCompartement = cp.Compartment()

# Item database Test
#  myItem = it.Item("Pencil","ox24",1,5)
# myItem.insertItemIntoDatabase(myItem)
#  myItem.getItemsFromDatabase()


# myStorageSection = ss.StorageSection("CabinetOne", [], 9)
#  myStorageSection.insertStorageSectionIntoDatabase(myStorageSection)


app()

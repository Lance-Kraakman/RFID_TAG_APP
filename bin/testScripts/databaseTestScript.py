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


def app():
    print("HI X")

    itemList = it.Item.getItemsFromDatabase()

    for item in itemList:
        print(item)

    newItem = it.Item("sdfh","Fucjdf",5,5)
    it.Item.insertItemIntoDatabase(newItem)

    print("-------------------------------------------------------------------------------------")


app()

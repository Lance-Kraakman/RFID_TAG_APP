from myLib.Item import Item
from myLib.Database import databaseAbstraction
from myLib.StorageSection import StorageSection
from myLib.Compartment import Compartment


class MainController:

    # Single StorageSection
    CabinetNineByNine = StorageSection.StorageSection("Cabinet One", [], 0)
    StorageSectionList = [CabinetNineByNine] # by default we have a single storage section with nothing in it

    def __init__(self):
        print("")

    # we need to make functions that...
    # add cabinets and items to database
    # read cabinets and items from database

    # Function returns a storage section with all of the elements in it from the database
    def readStorageSectionFromDatabase(self, storageSectionID):
        print("PAPI STOP")


    # Three views

    # TO-DO

import _thread as th
import time
from myLib.Item import Item as it
from myLib.webClient import httpsClient as http
from myLib.Rfid import Rfid

from myLib.Controller import MainController


# Using threads. One Thread is dedicated too GUI/Database
# One Thread is dedicated to HTTP/Database
# May need to consider Semaphore for database access multiple access/datasharing issues
# But that is a massive ceebs right now and i will do that later <3
# XOXOXOXO


def GUI_THREAD(threadName, delay):
    myApp = MainController.MainController()


def HTTP_THREAD(threadName, delay):
    print("HTTP STUFF :O")
    httpClient = http.HttpsClient()
    rfidTagsScanned = Rfid.RfidTagList()
    while True:
        print("HTTP REQUEST - > UPDATE DATABASE")
        uuidList = []
        try:
            print("- Http Request Start -")
            httpData = httpClient.test_request()

            rfidTagsScanned.processRfidTagInputs(httpData)
        except Exception as err:
            print(":( Couldnt Make HTTP Request\n")
            print(err)
        finally:
            print(rfidTagsScanned.getRfidTagList())


print("Hookay")
th.start_new_thread(GUI_THREAD, ("", 3))
th.start_new_thread(HTTP_THREAD, ("dsf", 5))
print("Hookay")

while 1:
    pass



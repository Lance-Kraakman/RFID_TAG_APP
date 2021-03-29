import _thread as th
import time
from myLib.Item import Item as it
from myLib.webClient import httpsClient as http
from myLib.Rfid import Rfid, RfidNetworkService
from myLib.Controller import MainController
from multiprocessing import Process


def gui_process(threadName, nothing):
    myApp = MainController.MainController()


def mqtt_process(threadName, nothing):
    time.sleep(2)
    rfidNetworkService = RfidNetworkService.RfidNetworkService()
    rfidNetworkService.runNetworkLoop()


def start_process():
    mqttProcess = Process(target=mqtt_process, args=("", ""))
    guiProcess = Process(target=gui_process, args=("", ""))

    mqttProcess.start()
    guiProcess.start()

    mqttProcess.join()
    guiProcess.join()




if __name__ == '__main__':
    start_process()


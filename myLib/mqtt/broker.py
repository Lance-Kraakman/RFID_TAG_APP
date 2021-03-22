import os


# This Class should handle the mosquiito broker. mosquitto is a mqtt command line tool. available on linux and windows
# This Class should handle the different installations and configurations based on what os is being used
# This is a TODO for automatic configuration for end-user deployment
class Broker:
    def __init__(self):
        self._broker_os = os.name

    def getOperatingSystem(self):
        return self._broker_os

    def printBrokerDetails(self):
        print("Broker running on %s" % self.getOperatingSystem())

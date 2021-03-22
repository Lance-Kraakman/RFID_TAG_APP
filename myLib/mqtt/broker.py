import os
from zeroconf import ServiceInfo
from myLib.mDNS import mDNS
import socket


# This Class should handle the mosquiito broker. mosquitto is a mqtt command line tool. available on linux and windows
# This Class should handle the different installations and configurations based on what os is being used
# This is a TODO for automatic configuration for end-user deployment
class Broker:
    def __init__(self):
        self._broker_os = os.name
        self._mdnsService = mDNS.MdnsService()  # Broker has an mDNS service for advertisement

    def getOperatingSystem(self):
        return self._broker_os

    def printBrokerDetails(self):
        print("MDNs advertisement running on %s" % self.getOperatingSystem())
        print("Broker running on %s" % self.getOperatingSystem())

    def getMdnsService(self):
        return self._mdnsService

    # Function registers Mdns service for broker
    def registerMdnsService(self, brokerAddress='localhost', mqttName="_my-def._mqtt._tcp.local."):
        # Register Dummy Service for now



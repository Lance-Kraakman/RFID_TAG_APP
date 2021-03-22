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
        self._mdnsService = mDNS.Mdns()  # Broker has an mDNS service for advertisement

    def getOperatingSystem(self):
        return self._broker_os

    def printBrokerDetails(self):
        print("MDNs advertisement running on %s" % self.getOperatingSystem())
        print("Broker running on %s" % self.getOperatingSystem())

    def getMdnsService(self):
        return self._mdnsService

    # Function registers Mdns service for broker
    def registerMdnsService(self, brokerAddress='localhost', mqttName="_my-def._mqtt._tcp.local."):
        # desc = {'version': '0.10', 'a': 'test value', 'b': 'another value'}
        # info = ServiceInfo(
        #     "_http._tcp.local.", "_my-serv._http._tcp.local.",
        #     socket.inet_aton("0.0.0.0"), 1234, 0, 0, desc
        # )

        #info = ServiceInfo(info, "_my-serv._http._tcp.local.")
        addresses = [socket.inet_aton("127.0.0.1")]
        info = ServiceInfo("_mqtt._tcp.local.", mqttName, 1883, addresses=addresses)
        print(info)
        return self.getMdnsService().register_service(info)


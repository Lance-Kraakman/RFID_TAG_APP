import socket

from zeroconf import ServiceBrowser, Zeroconf, ServiceInfo, IPVersion, InterfaceChoice


# https://github.com/jstasiak/python-zeroconf/blob/master/examples/registration.py
class MdnsService:
    infoDict = {} # Dict of information to keep track of mdns services
    zeroconf = Zeroconf(ip_version=IPVersion.All, interfaces=InterfaceChoice.All)

    def __init__(self):
        ip_version = IPVersion.All
        self.zeroconf = Zeroconf(ip_version=ip_version, interfaces=InterfaceChoice.All)

    def get_service_info(self, type, name):
        info = self.zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))

    def register_service(self, info, serviceKey):
        self.addServiceInfo(serviceKey, info)  # Adds the service info to the MDNS class
        self.zeroConfigInit()  # Re-inits state before calls. Sometimes needed. Wary of options
        self.zeroconf.register_service(info)
        self.zeroconf.update_service(info)
        print(info)

    def register_dummy_service(self):
        desc = {}
        info = ServiceInfo(
            "_coap._udp.local.",
            "_light._coap._udp.local.",
            addresses=[socket.inet_aton("127.0.0.1")],
            port=5683,
            properties=desc,
            server="ash-2.local.",
        )

        self.register_service(info=info, serviceKey="dummyService")  # Registers the dummy MDNS service

    def unregister_mdns_service(self, serviceKey):
        desc = {}
        info = ServiceInfo(
            "_coap._udp.local.",
            "_light._coap._udp.local.",
            addresses=[socket.inet_aton("127.0.0.1")],
            port=5683,
            properties=desc,
            server="ash-2.local.",
        )
        self.zeroconf.unregister_service(info)
        #self.zeroconf.unregister_service(self.getServiceInfo(serviceKey))
        self.zeroconf.close()

    # Function adds a service info item to the service info list
    def addServiceInfo(self, serviceKey, info):
        self.infoDict[serviceKey] = info

    def removeServiceInfo(self, serviceKey):
        self.infoDict.pop(serviceKey)

    # Function gets the service info from the service key
    def getServiceInfo(self, serviceKey):
        print(self.infoDict[serviceKey])
        return self.infoDict[serviceKey]

    # Function prints the servicesKeys of all the running services
    def printServiceInfoKeys(self):
        for key, value in self.infoDict:
            print(key)

    def zeroConfigInit(self):
        self.zeroconf = Zeroconf(ip_version=IPVersion.All, interfaces=InterfaceChoice.All)




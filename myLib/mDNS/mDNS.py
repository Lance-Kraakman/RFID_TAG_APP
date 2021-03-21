from zeroconf import ServiceBrowser, Zeroconf, ServiceInfo


class Mdns:
    zeroconf = Zeroconf()

    #
    # https://python-zeroconf.readthedocs.io/en/latest/api.html?highlight=register_service#zeroconf.Zeroconf.register_service
    # https://www.programcreek.com/python/example/98431/zeroconf.Zeroconf
    def register_service(self, info):
        self.zeroconf.register_service(info)

    def get_service_info(self, type, name):
        info = self.zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))





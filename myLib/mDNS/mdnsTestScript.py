import mDNS
import time

myMdns = mDNS.MdnsService()
myMdns.register_dummy_service()


time.sleep(5)

print("Unregistering...")

#myMdns.unregister_mdns_service('dummyService')

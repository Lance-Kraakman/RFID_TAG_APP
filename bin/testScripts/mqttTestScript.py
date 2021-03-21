from myLib.mqtt import broker
from myLib.mDNS import mDNS
from zeroconf import ServiceInfo

def app():
    print("Startin MDNS advertisement service")
    #myMdns = mDNS.Mdns() # Creates mDNS advertisement service

    # This should work when we have actual service information <3
    # https://www.programcreek.com/python/?code=blinker-iot%2Fblinker-py%2Fblinker-py-master%2FBlinkerAdapters%2FBlinkerLinuxWS.py
    #info = ServiceInfo("_my-dummy._tcp.local.", "_my-dummy._tcp.local.")
    #myMdns.register_service(info)

    print("Starting MQTT broker")
    broker.runBroker()


app()


from myLib.mqtt import mqttService
from myLib.mDNS import mDNS
from zeroconf import ServiceInfo, InterfaceChoice
import time


def app():
    print("Starting MQTT")
    desktopMqttClient = mqttService.MqttClient()
    time.sleep(2)
    desktopMqttClient.publishMessage("desktop-application", 1)
    time.sleep(5)
    desktopMqttClient.mqttDisconnect()


print(__name__)

app()

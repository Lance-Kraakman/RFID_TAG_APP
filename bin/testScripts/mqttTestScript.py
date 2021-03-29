from myLib.mqtt import mqttService
from myLib.mDNS import mDNS
from zeroconf import ServiceInfo, InterfaceChoice
import time


def app():
    print("Starting Desktop MQTT Client")
    desktopMqttClient = mqttService.MqttClient()
    time.sleep(2)
    desktopMqttClient.publishMessage("desktop-application", 1)
    desktopMqttClient.subscribeToTopic("rfid")
    time.sleep(2)

    interrupted = False
    while not interrupted:
        try:
            # Do stuff
            time.sleep(2)
            # Check if we have received messages over mqtt
            messagesReceived = desktopMqttClient.getAndRemoveMessageList()
            if messagesReceived is not None:
                for message in messagesReceived:
                    print(message[mqttService.DATA_INDEX])  # Print the UUID for every received message
            messagesReceived = []
        except Exception as err:
            interrupted = True
            print(err)
            print("EXCEPTION")

    desktopMqttClient.mqttDisconnect()


if __name__ == "__main__":
    app()

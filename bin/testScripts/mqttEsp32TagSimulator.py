# Runnning this script will create a mqtt object which when a key is pressed simulates a RFID tag being pressed
from myLib.mqtt import mqttService

print("Initilize MQTT client")
myMqttClient = mqttService.MqttClient("esp32-simulator")

# Run RFID tag simulator.
inputString = ""

while True:
    try:
        inputString = input("Input rfid to generate a dummy tag or quit to quit\n")

        if inputString.lower() == "rfid":
            # generate rfid tag
            print("Generate RFID dummy Tag\n")
        elif inputString.lower() == "quit":
            print("QUITTING RFID TAG SIMULATOR")
            break
        else:
            print("Unrecognised Command")
    except Exception as err:
        print("Exception Occurred")
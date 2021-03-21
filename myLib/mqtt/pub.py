# publisher
# import paho.mqtt.client as mqtt
#
#
# client = mqtt.Client()
# client.connect('localhost', 9999)
# client.subscribe("test")
#
#
# print(client.is_connected())
#
# while True:
#     client.publish("test", input('Message : '))
#     print(client.is_connected())
#
#     DELETE EVERYTHING AND FOLLOW THIS TUTORIAL HBMQTT https://www.emqx.io/blog/comparision-of-python-mqtt-client
#
#     .LY THE HBMQTT LIBRARY AS WE CAN JUSTUSE IT FOR EVERYTHOING INST
import logging
import asyncio
import time
from hbmqtt.client import MQTTClient
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2


async def test_coro():
    C = MQTTClient()
    await  C.connect('mqtt://localhost:9999/')
    tasks = [
        asyncio.ensure_future(C.publish('test', b'TEST MESSAGE WITH QOS_0', qos=QOS_0)),
        asyncio.ensure_future(C.publish('test', b'TEST MESSAGE WITH QOS_1', qos=QOS_1)),
        asyncio.ensure_future(C.publish('test', b'TEST MESSAGE WITH QOS_2', qos=QOS_2)),
    ]
    await asyncio.wait(tasks)
    logging.info("messages published")


formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=formatter)
asyncio.get_event_loop().run_until_complete(test_coro())

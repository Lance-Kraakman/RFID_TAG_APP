import logging
import asyncio
from hbmqtt.broker import Broker
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1
import time

logger = logging.getLogger(__name__)
# https://github.com/LintangWisesa/HBMQTT_Paho_MySQL_MongoDB/blob/master/broker.py

myConfig = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': 'localhost:9999'    # 0.0.0.0:1883
        }
    },
    'keep-alive': 50,
    'auto_reconnect': True,
    'sys_interval': 1,
    'topic-check': {
        'enabled': False
    }
}


def broker_coro():
    broker = Broker(config=myConfig)
    yield from broker.start()


def brokerGetMessage():
    C = MQTTClient()
    yield from C.connect('mqtt://localhost:9999/')
    yield from C.subscribe([
        ("test", QOS_1)
    ])
    logger.info('Subscribed!')
    try:
        for i in range(1, 100):
            print("---------------------")
            message = yield from C.deliver_message()
            packet = message.publish_packet()
            print(f"{i}:  {packet.variable_header.topic_name} => {packet.payload.data}")
            print(packet.payload.data.decode('utf-8'))
    except ClientException as ce:
        logger.error("Client exception : %s" % ce)


def runBroker():
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(broker_coro())
    asyncio.get_event_loop().run_until_complete(brokerGetMessage())
    asyncio.get_event_loop().run_forever()

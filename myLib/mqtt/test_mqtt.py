import unittest
import publisher
import paho.mqtt.client as mqtt


class TestMqtt(unittest.TestCase):

    def setUp(self):
        self.testTopic = "test"
        self.queryHost = 'localhost'
        self.publisher = publisher.MqttClient()

    def tearDown(self):
        pass

    def test_localHost(self):
        self.assertIsNotNone(self.publisher.getMqttClient())

    def test_publisherQuery(self):
        self.assertEqual(self.publisher.publishMessage(self.testTopic, "TEST MESSGAGE X"), True)

    def test_subscriber(self):
        self.assertEqual(self.publisher.subscribeToTopic(self.testTopic), mqtt.MQTT_ERR_SUCCESS)



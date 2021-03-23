import unittest
import publisher
import broker as brk


class TestMqttBroker(unittest.TestCase):

    def setUp(self):
        self.testBroker = brk.Broker()

    def tearDown(self):
        pass

    def test_register_mdns(self):
        self.testBroker.registerMdnsService()
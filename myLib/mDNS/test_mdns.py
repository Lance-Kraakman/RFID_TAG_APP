import unittest
import mDNS


# TODO -> Create tests and make mDNS class 'testable'
class TestMqtt(unittest.TestCase):

    def setUp(self):
        self.myMdns = mDNS.MdnsService()

    def tearDown(self):
        pass

    # No asserts because zeroconf functions return None :( -> TODO -> Provide return values based on succesfully config
    def test_register_unregister_mdns(self):
        self.myMdns.register_dummy_service()
        self.myMdns.unregister_mdns_service('dummyService')

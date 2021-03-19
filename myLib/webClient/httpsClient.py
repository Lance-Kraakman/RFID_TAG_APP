import requests as req


cacertPath = "/home/lance/eclipse-workspace/rfidProjectApplication/files/certs/cacert.pem"
prvtKeyPath = "/home/lance/eclipse-workspace/rfidProjectApplication/files/certs/prvtkey.pem"
verifyPath = "/home/lance/eclipse-workspace/rfidProjectApplication/files/certs/"


class HttpsClient:
    def test_request(self):
        print("---------Testing Request----------")

        # USe https, because my server is configured for it. (HTTPS uses port 443 by defualt)
        x = req.get("https://my-esp32.local/getTags", verify=False, timeout=1000)
        #x = req.get("https://192.168.1.73:443/getTags", verify=False)

        return x.text


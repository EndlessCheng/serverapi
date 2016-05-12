import unittest
import urllib2
import json


class TestHeatProducts(unittest.TestCase):
    def setUp(self):
        self.requrl = 'http://api.shundaoer.net.cn/v1/heatproducts/'

    def testHeatProducts(self):
        self.req = urllib2.Request(self.requrl)
        self.response = urllib2.urlopen(self.req)
        self.response = json.loads(self.response.read())
        self.assertIsNotNone(self.response[0]['picture'])
        self.assertIsNotNone(self.response[0]['description'])
        self.assertIsNotNone(self.response[0]['price'])
        self.assertIsNotNone(self.response[0]['score'])
        self.assertIsNotNone(self.response[0]['sold_num'])
        self.assertIsNotNone(self.response[0]['category_id'])
        self.assertIsNotNone(self.response[0]['id'])
        self.assertIsNotNone(self.response[0]['unit'])
        self.assertIsNotNone(self.response[0]['name'])
        self.assertIsNotNone(self.response[1]['picture'])
        self.assertIsNotNone(self.response[1]['description'])
        self.assertIsNotNone(self.response[1]['price'])
        self.assertIsNotNone(self.response[1]['score'])
        self.assertIsNotNone(self.response[1]['sold_num'])
        self.assertIsNotNone(self.response[1]['category_id'])
        self.assertIsNotNone(self.response[1]['id'])
        self.assertIsNotNone(self.response[1]['unit'])
        self.assertIsNotNone(self.response[1]['name'])

if __name__ == '__main__':
    unittest.main()

import unittest
import urllib2
import json


class TestCanteens(unittest.TestCase):
    def setUp(self):
        self.requrlhome = 'http://api.shundaoer.net.cn/v1/home/'
        self.requrlbyid = 'http://api.shundaoer.net.cn/v1/canteens/1/'
        self.requrlcanteens = 'http://api.shundaoer.net.cn/v1/canteens/'

    def testCanteens(self):
        self.req = urllib2.Request(self.requrlhome)
        self.response = urllib2.urlopen(self.req)
        self.response = json.loads(self.response.read())
        self.assertIsNotNone(self.response['status'])
        self.assertIsNotNone(self.response['picture'])
        self.assertIsNotNone(self.response['description'])
        self.assertIsNotNone(self.response['phone'])
        self.assertIsNotNone(self.response['address'])
        self.assertIsNotNone(self.response['id'])
        for self.i in range(len(self.response['windows_data'])):
            self.assertIsNotNone(self.response['windows_data'][self.i]['picture'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['name'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['score'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['sold_num'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['canteen_id'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['id'])
        self.assertIsNotNone(self.response['name'])

        self.req = urllib2.Request(self.requrlbyid)
        self.response = urllib2.urlopen(self.req)
        self.response = json.loads(self.response.read())
        self.assertIsNotNone(self.response['status'])
        self.assertIsNotNone(self.response['picture'])
        self.assertIsNotNone(self.response['description'])
        self.assertIsNotNone(self.response['phone'])
        self.assertIsNotNone(self.response['address'])
        self.assertIsNotNone(self.response['id'])
        for self.i in range(len(self.response['windows_data'])):
            self.assertIsNotNone(self.response['windows_data'][self.i]['picture'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['name'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['score'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['sold_num'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['canteen_id'])
            self.assertIsNotNone(self.response['windows_data'][self.i]['id'])
        self.assertIsNotNone(self.response['name'])

        self.req = urllib2.Request(self.requrlcanteens)
        self.response = urllib2.urlopen(self.req)
        self.response = json.loads(self.response.read())

        for self.i in range(len(self.response)):
            self.assertIsNotNone(self.response[self.i]['status'])
            self.assertIsNotNone(self.response[self.i]['picture'])
            self.assertIsNotNone(self.response[self.i]['description'])
            self.assertIsNotNone(self.response[self.i]['phone'])
            self.assertIsNotNone(self.response[self.i]['address'])
            self.assertIsNotNone(self.response[self.i]['id'])
            self.assertIsNotNone(self.response[self.i]['name'])


if __name__ == '__main__':
    unittest.main()

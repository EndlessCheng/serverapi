# -*- coding: utf-8 -*-
import unittest
import urllib2
import json


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.requrl = 'http://api.shundaoer.net.cn/v1/search/?query_param=米'

    def testSearch(self):
        self.req = urllib2.Request(self.requrl)
        self.response = urllib2.urlopen(self.req)
        self.response = json.loads(self.response.read())

        for self.i in range(len(self.response['windows'])):
            self.assertIsNotNone(self.response['windows'][self.i]['picture'])
            self.assertIsNotNone(self.response['windows'][self.i]['name'])
            self.assertIsNotNone(self.response['windows'][self.i]['score'])
            self.assertIsNotNone(self.response['windows'][self.i]['sold_num'])
            self.assertIsNotNone(self.response['windows'][self.i]['canteen_id'])
            self.assertIsNotNone(self.response['windows'][self.i]['id'])

        for self.i in range(len(self.response['products'])):
            self.assertIsNotNone(self.response['products'][self.i]['picture'])
            self.assertIsNotNone(self.response['products'][self.i]['description'])
            self.assertIsNotNone(self.response['products'][self.i]['price'])
            self.assertIsNotNone(self.response['products'][self.i]['score'])
            self.assertIsNotNone(self.response['products'][self.i]['sold_num'])
            self.assertIsNotNone(self.response['products'][self.i]['category_id'])
            self.assertIsNotNone(self.response['products'][self.i]['id'])
            self.assertIsNotNone(self.response['products'][self.i]['unit'])
            self.assertIsNotNone(self.response['products'][self.i]['name'])


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
import unittest
import urllib2
import json


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.requrl = 'http://api.shundaoer.net.cn/v1/windows/1/'

    def testWindow(self):
        self.req = urllib2.Request(self.requrl)
        self.response = urllib2.urlopen(self.req)
        self.response = json.loads(self.response.read())

        self.assertIsNotNone(self.response['window']['picture'])
        self.assertIsNotNone(self.response['window']['name'])
        self.assertIsNotNone(self.response['window']['score'])
        self.assertIsNotNone(self.response['window']['sold_num'])
        self.assertIsNotNone(self.response['window']['canteen_id'])
        self.assertIsNotNone(self.response['window']['id'])

        for self.i in range(len(self.response['products_data'])):
            self.assertIsNotNone(self.response['products_data'][self.i]['category'])
            for self.j in range(len(self.response['products_data'][self.i]['products'])):
                self.assertIsNotNone(self.response['products_data'][self.i]['products'][self.j]['picture'])
                self.assertIsNotNone(self.response['products_data'][self.i]['products'][self.j]['description'])
                self.assertIsNotNone(self.response['products_data'][self.i]['products'][self.j]['price'])
                self.assertIsNotNone(self.response['products_data'][self.i]['products'][self.j]['score'])
                self.assertIsNotNone(self.response['products_data'][self.i]['products'][self.j]['sold_num'])
                self.assertIsNotNone(self.response['products_data'][self.i]['products'][self.j]['category_id'])
                self.assertIsNotNone(self.response['products_data'][self.i]['products'][self.j]['id'])
                self.assertIsNotNone(self.response['products_data'][self.i]['products'][self.j]['unit'])
                self.assertIsNotNone(self.response['products_data'][self.i]['products'][self.j]['name'])

if __name__ == '__main__':
    unittest.main()

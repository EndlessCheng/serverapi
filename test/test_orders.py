# -*- coding: utf-8 -*-

import unittest
import urllib
import urllib2
import json


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.test_data = dict()
        self.test_data['cateen_id'] = 1
        self.test_data['customer_id'] = 1
        self.test_data['window_id'] = 1
        self.test_data['product_list'] = '1_3_4'
        self.test_data['product_price'] = 9
        self.test_data['ship_price'] = 0
        self.test_data['promotion'] = 0
        self.test_data['total_price'] = 9
        # self.test_data['if_self_help'] = 1
        self.test_data['address_id'] = 1
        self.test_data['expect_time'] = 0
        self.test_data['leave_msg'] = 'leave_msg'
        self.test_data_urlencode = urllib.urlencode(self.test_data)
        # self.requrl = 'http://115.159.208.167/v1/orders'
        self.requrl = 'http://api.shundaoer.net.cn/v1/orders/'

    def testOrder(self):
        self.req = urllib2.Request(url=self.requrl, data=json.dumps(self.test_data))
        self.response = urllib2.urlopen(self.req)
        self.code = self.response.getcode()
        self.response = json.loads(self.response.read())
        self.assert_(201, self.code)
        self.assert_(201, self.response["status"])
        self.assert_("下单成功", self.response["msg"])

if __name__ == '__main__':
    unittest.main()


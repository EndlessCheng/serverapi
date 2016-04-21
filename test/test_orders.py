# -*- coding: utf-8 -*-

import unittest
import urllib
import urllib2
import json


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.test_data = dict()
        self.test_data['cateen_id'] = '001'
        self.test_data['product_list'] = 'id2_id4_id1'
        self.test_data['product_price'] = '15.00'
        self.test_data['ship_price'] = '2.00'
        self.test_data['promotion'] = '3.00'
        self.test_data['total_price'] = '14'
        self.test_data['if_self_help'] = '0'
        self.test_data['expect_time'] = '30'
        self.test_data['leave_msg'] = 'leave_msg'
        self.test_data_urlencode = urllib.urlencode(self.test_data)
        self.requrl = 'http://api.byway.net.cn/v1/orders'

    def testOrder(self):
        self.req = urllib2.Request(url=self.requrl, data=self.test_data_urlencode)
        self.response = urllib2.urlopen(self.req)
        self.code = self.response.getcode()
        self.response = json.loads(self.response.read())
        self.assert_(201, self.code, "正常下单未返回正常值")
        self.assert_(201, self.response["status"], "正常下单未返回正常值")
        self.assert_("下单成功", self.response["msg"], "正常下单未返回msg")

if __name__ == '__main__':
    unittest.main()


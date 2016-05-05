# -*- coding: utf-8 -*-

import unittest
from register import Register

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.name = "Tom"
        self.mail = "tom@bjtu.edu.com"
        self.wrongmail = "tom@mail.tom.com"
        self.phone = "110110110"
        self.password = "password"
        self.register = Register(self.name,self.mail,self.phone,self.password)
        self.wrongregister = Register(self.name,self.wrongmail,self.phone,self.password)


    def tearDown(self):
        self.register.deleteTest()
        self.register = None
        self.wrongregister = None

    def testNormal(self):
        self.assert_(200,self.register.insert(),"正常注册未返回正常值")
        self.assert_(201, self.register.insert(), "重复注册未返回正常值")

    def testWrongMail(self):
        self.assert_(202,self.wrongregister.insert(),"非学校邮箱未返回正常值")


if __name__ == '__main__':
    unittest.main()

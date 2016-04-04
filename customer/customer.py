# -*- coding: utf-8 -*-

from util.response_util import *
from models import Customer


def customer(request):
	if request.method == 'POST':
		return post_customer(request)
	elif request.method == 'GET':
		pass


def post_customer(request):
	mail = request.POST.get('mail')
	password = request.POST.get('password')

	data = dict()

	if mail is None or password is None:
		data['status'] = 0
		data['msg'] = u'信息缺失'
		return create_data_response(data)

	new_customer = Customer()
	new_customer.mail = mail
	new_customer.password = password
	if_signed = new_customer.signup_customer()

	if if_signed:
		data['status'] = 1
		data['msg'] = u'注册成功'
		return create_data_response(data)
	else:
		data['status'] = 0
		data['msg'] = u'注册失败'
		return create_data_response(data)

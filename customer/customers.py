# -*- coding: utf-8 -*-
import json

from util.response_util import *
from models import Customer
from core.jsonresponse import *


def customer(request):
	if request.method == 'POST':
		return post_customer(request)
	elif request.method == 'GET':
		pass


def post_customer(request):
	customer_data = json.loads(request.body)
	mail = customer_data.get('mail', None)
	phone = customer_data.get('phone', None)
	password = customer_data.get('password', None)

	data = dict()

	if mail is None or password is None or phone is None:
		data = u'信息缺失'
		return create_response(422, data)

	new_customer = Customer()
	new_customer.mail = mail
	new_customer.phone = phone
	new_customer.password = password
	if_signed = new_customer.signup_customer()

	if if_signed:
		content = dict()
		content['status'] = 201
		content['msg'] = u'注册成功,请登录邮箱进行验证'
		content['href'] = '%s%s%s' % (BASE_PATH, 'customers/', str(new_customer.id))

		return create_simple_response(201, json.dumps(content))
	else:
		content = dict()
		content['status'] = 422
		content['msg'] = u'注册失败'
		return create_simple_response(422, json.dumps(content))


# 邮件验证CUSTOMER
# （提供该CUSTOMER的全部信息）
def put_customer(request):
	pass
	# customer_id = request.GET.get('customer_id')
	# verify_token = request.GET.get('verify_code')
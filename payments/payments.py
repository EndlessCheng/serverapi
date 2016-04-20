# -*- coding: utf-8 -*-

import json

from models import *
from util.response_util import *


def payments(request, payment_id=None):
	if request.method == 'POST':
		return post_payments(request)
	elif request.method == 'PATCH':
		pass
	elif request.method == 'GET':
		pass
	else:
		pass


def post_payments(request, payment_id=None):
	payment_data = json.loads(request.body)
	content = dict()
	payment_record = PaymentRecord()

	try:
		payment_record.order_id = Order.objects.get(id=payment_data.get('order_id', None))
		payment_record.customer_id = Customer.objects.get(id=payment_data.get('customer_id', None))
		payment_record.pay_way = payment_data.get('pay_way', 'Default')
	except:
		content['status'] = 406
		content['msg'] = u'Request格式有误'
		return create_simple_response(406, json.dumps(content))

	if payment_record.create_payment():
		content['status'] = 201
		content['msg'] = u'支付成功'
		content['href'] = '%s%s%s' % (BASE_PATH, 'payments/', str(payment_record.id))
		return create_simple_response(201, json.dumps(content))
	else:
		content['status'] = 500
		content['msg'] = u'支付失败,服务端存储出现异常'
		return create_simple_response(500, json.dumps(content))

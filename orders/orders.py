# -*- coding: utf-8 -*-

import json

from models import *
from util.response_util import *


def orders(request, order_id=None):
	if request.method == 'POST':
		return post_orders(request, order_id)
	elif request.method == 'GET':
		return create_simple_response(200, 'hi')
	else:
		pass


def post_orders(request, order_id=None):
	order_data = json.loads(request.body)

	order = Order()
	content = dict()
	try:
		order.customer_id = Customer.objects.get(id=order_data.get('customer_id', None))
		order.canteen_id = Canteen.objects.get(id=order_data.get('cateen_id', None))
		order.product_list = order_data.get('product_list', None)
		order.product_price = order_data.get('product_price', None)
		order.ship_price = order_data.get('ship_price', None)
		order.promotion = order_data.get('promotion', None)
		order.total_price = order_data.get('total_price', None)
		order.if_self_help = order_data.get('is_self_help', 0)
		order.address = Ship.objects.get(id=order_data.get('address_id', None))
		order.expect_time = order_data.get('expect_time', None)
		order.leave_msg = order_data.get('leave_msg', None)
		order.combo_id = '%s_%s_%s' % (str(order.canteen_id.id), str(order.customer_id.id),
		                               str(order.if_self_help))
	except Exception, e:
		print(e)
		content['status'] = 406
		content['msg'] = u'Request格式有误'
		return create_simple_response(406, json.dumps(content))

	if order.create_order():
		content['status'] = 201
		content['msg'] = u'下单成功'
		content['href'] = '%s%s%s' % (BASE_PATH, 'orders/', str(order.id))
		return create_simple_response(201, json.dumps(content))
	else:
		content['status'] = 500
		content['msg'] = u'下单失败,服务端存储出现异常'
		return create_simple_response(500, json.dumps(content))


def get_orders(request, order_id=None):
	if order_id is None:
		# return all orders...
		pass
	else:
		order = Order.objects.get(id=order_id)
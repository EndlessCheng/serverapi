import json

from models import *
from util.response_util import *


def orders(request, order_id=None):
	if request.method == 'POST':
		return post_orders(request, order_id)
	elif request.method == 'GET':
		pass
	else:
		pass


def post_orders(request, order_id=None):
	order_data = json.dumps(request.body)

	order = Order()
	content = dict()
	try:
		order.canteen_id = order_data.get('cateen_id', None)
		order.product_list = order_data.get('product_list', None)
		order.product_price = order_data.get('product_price', None)
		order.ship_price = order_data.get('ship_price', None)
		order.promotion = order_data.get('promotion', None)
		order.total_price = order_data.get('total_price', None)
		order.if_self_help = order_data.get('is_self_price', 0)
		order.expect_time = order_data.get('expect_time', None)
		order.leave_msg = order_data.get('leave_msg', None)
		order.combo_id = str(order.canteen_id)+str(order.if_self_help)+str(order.id)
	except:
		content['status'] = 406
		content['msg'] = 'Request格式有误'
		return create_simple_response(406, json.dumps(content))

	if order.save_order():
		content['status'] = 201
		content['msg'] = '下单成功'
		content['href'] = '%s%s%s' % (BASE_PATH, 'orders/', str(order.id))
		return create_simple_response(201, json.loads(content))
	else:
		content['status'] = 500
		content['msg'] = '下单失败,服务端存储出现异常'
		return create_simple_response(500, json.loads(content))

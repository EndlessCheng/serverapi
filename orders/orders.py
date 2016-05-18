# -*- coding: utf-8 -*-

import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login

from models import *
from util.response_util import *
from util.models_util import OrderUtils


def orders(request, order_id=None):
	if request.method == 'POST':
		return post_orders(request, order_id)
	elif request.method == 'GET':
		return get_orders(request, order_id)
	elif request.method == 'PATCH':
		return patch_orders(request, order_id)
	else:
		pass


@login_required
def post_orders(request, order_id=None):
	order_data = json.loads(request.body)

	order = Order()
	content = dict()
	try:
		order.customer_id = Customer.objects.get(id=request.user.id)
		order.canteen_id = Canteen.objects.get(id=order_data.get('cateen_id', None))
		order.window_id = Window.objects.get(id=order_data.get('window_id', None))
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


@login_required
def get_orders(request, order_id=None):
	if order_id is None:
		query_type = request.GET.get('query_type', None)
		order_utils = OrderUtils()
		if query_type == 'window':
			window_id = request.GET.get('window_id', None)
			expect_status = request.GET.get('expect_status', None)
			order_list = order_utils.get_order_by_window(window_id, expect_status)
			content = order_utils.orders_to_array(order_list)
		elif query_type == 'deliver':
			canteen_id = request.GET.get('canteen_id', None)
			expect_status = ORDER_PUSHED
			order_list = order_utils.get_order_by_deliver(canteen_id, expect_status)
			content = order_utils.orders_to_array(order_list)
		else:
			content = []
			pass

		return create_simple_response(200, content)
	else:
		order = Order.objects.get(id=int(order_id))
		order_record = OrderRecord.objects.get(order_id=order.id)
		if order.update_order_state(ORDER_PULLED) and \
			order_record.update_order_state(ORDER_PULLED):
			order_dict = order.to_dict()
			return create_simple_response(200, json.dumps(order_dict))
		else:
			content = dict()
			content['status'] = 500
			content['msg'] = u'操作失败,服务端存储出现异常'
			return create_simple_response(500, json.dumps(content))


@login_required
def patch_orders(request, order_id):
	content = dict()
	patch_data = json.loads(request.body)

	try:
		order_status_new = patch_data.get('new_status', None)
		order_deliver = patch_data.get('deliver_id', None)
	except:
		content['status'] = 406
		content['msg'] = u'Request格式有误'
		return create_simple_response(406, json.dumps(content))

	try:
		order = Order.objects.get(id=order_id)
		order_record = OrderRecord.objects.get(order_id=order.id)
	except:
		content['status'] = 404
		content['msg'] = u'资源未找到'
		return create_simple_response(404, json.dumps(content))

	if order.update_order_state(order_status_new) and order_record.update_order_state(order_status_new, order_deliver):
		order = Order.objects.get(id=order_id)
		order_dict = order.to_dict()
	else:
		content['status'] = 500
		content['msg'] = u'操作失败,服务端存储出现异常'
		return create_simple_response(500, json.dumps(content))

	return create_simple_response(200, json.dumps(order_dict))
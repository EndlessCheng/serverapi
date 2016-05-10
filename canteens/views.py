# -*- coding: utf-8 -*-
import json

from models import *
from util.response_util import *

DEFAULT_CANTEEN_ID = 1


def home(request, canteen_id=None):
	if request.method == 'GET':
		if canteen_id is None:
			canteen_id = DEFAULT_CANTEEN_ID

		try:
			canteen_data = dict()
			window_list = []
			now_canteen = Canteen.objects.get(id=canteen_id)
			now_windows = Window.objects.filter(canteen_id=canteen_id)

			for window in now_windows:
				window_list.append(window.to_dict())

			canteen_data = now_canteen.to_dict()
			canteen_data['windows_data'] = window_list

			return create_simple_response(200, json.dumps(canteen_data))
		except:
			content = dict()
			content['msg'] = 'resource not found'
			return create_simple_response(404, json.dumps(content))


def search(request):
	query_param = request.GET.get('query_param', None)
	if not query_param:
		content = {'msg': 'resource not found'}
		return create_simple_response(404, json.dumps(content))
	else:
		window_result_objs = Window.objects.filter(name__icontains=query_param)
		product_result_objs = Product.objects.filter(name__icontains=query_param)

		search_result = dict()
		window_result_arr = []
		product_result_arr = []

		for window_obj in window_result_objs:
			window_result_arr.append(window_obj.to_dict())
		for product_obj in product_result_objs:
			product_result_arr.append(product_obj.to_dict())

		search_result['windows'] = window_result_arr
		search_result['products'] = product_result_arr

		return create_simple_response(200, json.dumps(search_result))

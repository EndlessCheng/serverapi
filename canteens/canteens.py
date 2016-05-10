# -*- coding: utf-8 -*-
import json
from django.http import HttpResponseRedirect

from models import *
from util.response_util import *


def canteens(request, canteen_id=None):
	if canteen_id:
		return HttpResponseRedirect('/v1/canteens/'+canteen_id)
	else:
		canteens_list = Canteen.objects.all()
		# canteens_dict = dict()
		canteens_arr = []

		for canteen in canteens_list:
			canteens_arr.append(canteen.to_dict())

		return create_simple_response(200, json.dumps(canteens_arr))


def windows(request, window_id=None):
	if request.method == 'GET':
		window = Window.objects.get(id=window_id)
		categories = Category.objects.filter(window_id=window_id)

		result = dict()
		cate_list = []
		result['window'] = window.to_dict()

		for cate in categories:
			cate_obj = dict()
			product_list = []

			cate_obj['category'] = cate.name
			cate_products = Product.objects.filter(category_id=cate.id)
			for product in cate_products:
				product_list.append(product.to_dict())
			cate_obj['products'] = product_list
			cate_list.append(cate_obj)

		result['products_data'] = cate_list

		return create_simple_response(200, json.dumps(result))

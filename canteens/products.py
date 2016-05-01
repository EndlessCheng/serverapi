# -*- coding: utf-8 -*-
import json

from models import *
from util.response_util import *


def heatgoods(request):
	if request.method == 'GET':
		heat_goods = HeatProduct.objects.all()
		heat_products = []

		for good in heat_goods:
			product = good.product_id
			heat_products.append(product.to_dict())

		return create_simple_response(200, json.dumps(heat_products))
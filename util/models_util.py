# -*- coding: utf-8 -*-
import json

from orders.models import *


class OrderUtils(object):

	def get_order_by_window(self, window_id, status=None):
		if status is None:
			return Order.objects.filter(window_id=window_id)
		else:
			return Order.objects.filter(window_id=window_id, status=status)

	def get_order_by_deliver(self, canteen_id, status):
		return Order.objects.filter(canteen_id=canteen_id, status=status)

	def orders_to_array(self, order_list):
		order_arr = []
		for order in order_list:
			order_arr.append(order.to_dict())
		return order_arr
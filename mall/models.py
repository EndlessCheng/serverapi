# -*- coding: utf-8 -*-
from django.db import models

from customers.models import *

ORDER_CREATED = 0
ORDER_PAYED = 1
ORDER_WAITING = 2
ORDER_RECEIVED = 3
ORDER_PUSHED = 4
ORDER_PULLED = 5
ORDER_COMPLETED = 6


class Canteen(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	picture = models.CharField(max_length=255)
	phone = models.CharField(max_length=100)
	address = models.CharField(max_length=255)
	status = models.IntegerField(default=1)


class Order(models.Model):
	customer_id = models.ForeignKey(Customer)
	canteen_id = models.ForeignKey(Canteen)
	combo_id = models.CharField(max_length=255)
	nowa_id = models.IntegerField(default=0)    # 当天订单id,每天从1自增
	product_list = models.CharField(max_length=255)
	product_price = models.FloatField(default=0.00)
	ship_price = models.FloatField(default=0.00)
	promotion = models.FloatField(default=0.00)
	total_price = models.FloatField(default=0.00)
	if_paid = models.IntegerField(default=0)
	if_self_help = models.IntegerField(default=0)
	address = models.ForeignKey(Ship)
	expect_time = models.IntegerField(default=0)
	leave_msg = models.CharField(max_length=255)
	status = models.IntegerField(default=ORDER_CREATED)
	created_at = models.DateTimeField(auto_now_add=True)

	def save_order(self):
		try:
			self.save()
			return True
		except:
			return False


class OrderRecord(models.Model):
	order_id = models.ForeignKey(Order)
	create_time = models.DateTimeField(auto_now_add=True)
	payment_time = models.DateTimeField()
	receive_time = models.DateTimeField()
	push_time = models.DateTimeField()
	pull_time = models.DateTimeField()
	finish_time = models.DateTimeField()
	deliver_id = models.ForeignKey(Customer, blank=True)


class Window(models.Model):
	name = models.CharField(max_length=100)
	canteen_id = models.ForeignKey(Canteen)
	picture = models.CharField(max_length=255)
	score = models.FloatField(default=5)
	sold_num = models.IntegerField(default=0)


class Category(models.Model):
	name = models.CharField(max_length=100)
	window_id = models.ForeignKey(Window)


class Product(models.Model):
	name = models.CharField(max_length=100)
	category_id = models.ForeignKey(Category)
	description = models.CharField(max_length=255)
	picture = models.CharField(max_length=255)
	price = models.FloatField(default=0.00)
	score = models.FloatField(default=5)
	unit = models.CharField(max_length=10, default=u'个')
	sold_num = models.IntegerField(default=0)


class PaymentRecord(models.Model):
	customer_id = models.ForeignKey(Customer)
	order_id = models.ForeignKey(Order)
	pay_way = models.CharField(max_length=50)


class WindowComment(models.Model):
	customer_id = models.ForeignKey(Customer)
	window_id = models.ForeignKey(Window)
	score = models.FloatField()
	comment = models.CharField(max_length=255)


class Operator(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	window_id = models.ForeignKey(Window)
	status = models.IntegerField(default=1)
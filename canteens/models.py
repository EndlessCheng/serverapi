# -*- coding: utf-8 -*-

from customers.models import *


class Canteen(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	picture = models.CharField(max_length=255)
	phone = models.CharField(max_length=100)
	address = models.CharField(max_length=255)
	status = models.IntegerField(default=1)


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
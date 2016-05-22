# encoding:utf-8

import time
import redis
import json

from celery.task import task

from canteens.models import *


# 这里用time模拟耗时操作
@task
def _do_kground_work(name):
	for i in range(10):
		print('hello:%s %s' % (name, i))
		time.sleep(1)


@task
def collect_heat_products():
	r = redis.StrictRedis(host='localhost', port=6379, db=10)
	HeatProduct.objects.all().delete()
	r.delete('heat_products')
	heat_products = Product.objects.all().order_by('-sold_num')[:4]
	for product in heat_products:
		heat_item = HeatProduct()
		heat_item.product_id = product
		heat_item.save()
		r.sadd('heat_products', product.to_dict())
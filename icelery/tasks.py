# encoding:utf-8

import time

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
	HeatProduct.objects.all().delete()
	heat_products = Product.objects.all().order_by('-sold_num')[:4]
	for product in heat_products:
		heat_item = HeatProduct()
		heat_item.product_id = product
		heat_item.save()
# encoding:utf-8

import time

from celery.task import task


# 这里用time模拟耗时操作
@task
def _do_kground_work(name):
	for i in range(10):
		print('hello:%s %s' % (name, i))
		time.sleep(1)

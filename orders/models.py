# -*- coding: utf-8 -*-

from django.forms.models import model_to_dict

from canteens.models import *
from util.qr_util import *

# Create your models here.

ORDER_CREATED = 0
ORDER_PAYED = 1
ORDER_WAITING = 2
ORDER_RECEIVED = 3
ORDER_PUSHED = 4
ORDER_PULLED = 5
ORDER_SENDING = 6
ORDER_COMPLETED = 7


class Order(models.Model):
	customer_id = models.ForeignKey(Customer)
	canteen_id = models.ForeignKey(Canteen)
	window_id = models.ForeignKey(Window)
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
	qr_storage_pre = models.CharField(max_length=255)
	status = models.IntegerField(default=ORDER_CREATED)
	created_at = models.DateTimeField(auto_now_add=True)

	def save_order(self):
		try:
			return self.create_order(self)
		except:
			return False

	def create_order(self):
		try:
			self.qr_storage_pre = '%s%s' % (HOST_URL, '/media/qrcode/')
			self.save()
			order_record = OrderRecord()
			order_record.order_id = self
			order_record.save()
			qr_url = '%s%s/%sorders/%s%s' % (HTTP_SCHEMA, HOST_URL, API_VERSION, str(self.id), '?operation=send')
			generate_qrcode(qr_url, str(self.id)+'.jpg')
			return True
		except Exception, e:
			print(e)
			return False

	def update_order_state(self, new_status):
		try:
			Order.objects.filter(id=self.id).update(status=new_status)
			return True
		except:
			return False

	def to_dict(self):
		order_dict = model_to_dict(self, exclude=['qr_storage_pre'])
		order_dict['qr_storage_url'] = self.qr_storage_pre+str(self.id)+'.jpg'
		return order_dict


class OrderRecord(models.Model):
	order_id = models.ForeignKey(Order)
	create_time = models.DateTimeField(auto_now_add=True)
	payment_time = models.DateTimeField(blank=True)
	receive_time = models.DateTimeField(blank=True)
	push_time = models.DateTimeField(blank=True)
	pull_time = models.DateTimeField(blank=True)
	send_time = models.DateTimeField(blank=True)
	finish_time = models.DateTimeField(blank=True)
	deliver_id = models.ForeignKey(Customer, blank=True)

	def update_order_state(self, status, order_deliver_id=None):
		if status == ORDER_PAYED:
			return self.append_payment_time()
		elif status == ORDER_RECEIVED:
			return self.append_receive_time()
		elif status == ORDER_PUSHED:
			return self.append_push_time()
		elif status == ORDER_PULLED:
			if order_deliver_id is not None:
				deliver = Customer.objects.get(id=order_deliver_id)
				if self.append_pull_time():
					return self.append_deliver(deliver)
				else:
					return False
			else:
				return self.append_pull_time()
		elif status == ORDER_SENDING:
			deliver = Customer.objects.get(id=order_deliver_id)
			if self.append_send_time():
				return self.append_deliver(deliver)
			else:
				return False
		elif status == ORDER_COMPLETED:
			return self.append_finish_time()
		else:
			return False

	def append_payment_time(self):
		try:
			# local_time = time.strftime(ISOTIMEFORMAT, time.localtime())
			OrderRecord.objects.filter(order_id=self.order_id).update(payment_time=timezone.now())
			return True
		except Exception, e:
			print(e)
			return False

	def append_pull_time(self):
		try:
			OrderRecord.objects.filter(order_id=self.order_id).update(pull_time=timezone.now())
			return True
		except Exception, e:
			print(e)
			return False

	def append_receive_time(self):
		try:
			OrderRecord.objects.filter(order_id=self.order_id).update(receive_time=timezone.now())
			return True
		except Exception, e:
			print(e)
			return False

	def append_push_time(self):
		try:
			OrderRecord.objects.filter(order_id=self.order_id).update(push_time=timezone.now())
			return True
		except Exception, e:
			print(e)
			return False

	def append_send_time(self):
		try:
			OrderRecord.objects.filter(order_id=self.order_id).update(send_time=timezone.now())
			return True
		except Exception, e:
			print(e)
			return False

	def append_finish_time(self):
		try:
			OrderRecord.objects.filter(order_id=self.order_id).update(finish_time=timezone.now())
			return True
		except Exception, e:
			print(e)
			return False

	def append_deliver(self, deliver):
		try:
			OrderRecord.objects.filter(order_id=self.order_id).update(deliver_id=deliver)
			return True
		except Exception, e:
			print(e)
			return False
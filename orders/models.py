# -*- coding: utf-8 -*-

from canteens.models import *

# Create your models here.

ORDER_CREATED = 0
ORDER_PAYED = 1
ORDER_WAITING = 2
ORDER_RECEIVED = 3
ORDER_PUSHED = 4
ORDER_PULLED = 5
ORDER_COMPLETED = 6


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
			return self.create_order(self)
		except:
			return False

	def create_order(self):
		try:
			self.save()
			order_record = OrderRecord()
			order_record.order_id = self
			order_record.save()
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


class OrderRecord(models.Model):
	order_id = models.ForeignKey(Order)
	create_time = models.DateTimeField(auto_now_add=True)
	payment_time = models.DateTimeField(blank=True)
	receive_time = models.DateTimeField(blank=True)
	push_time = models.DateTimeField(blank=True)
	pull_time = models.DateTimeField(blank=True)
	finish_time = models.DateTimeField(blank=True)
	deliver_id = models.ForeignKey(Customer, blank=True)

	def append_payment_time(self):
		try:
			# local_time = time.strftime(ISOTIMEFORMAT, time.localtime())
			print(timezone.now())
			OrderRecord.objects.filter(order_id=self.order_id).update(payment_time=timezone.now())
			return True
		except Exception, e:
			print(e)
			return False
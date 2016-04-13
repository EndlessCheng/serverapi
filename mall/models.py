from django.db import models

from users import models as Users

ORDER_WAITING = 0
ORDER_RECEIVED = 1
ORDER_PUSHED = 2
ORDER_PULLED = 3
ORDER_COMPLETED = 4


class Order(models.Model):
	canteen_id = models.ForeignKey(Canteen)
	combo_id = models.CharField(max_length=255)
	nowa_id = models.AutoField()    # 当天订单id,每天从1自增
	product_list = models.CharField(max_length=255)
	product_price = models.FloatField(default=0.00)
	ship_price = models.FloatField(default=0.00)
	promotion = models.FloatField(default=0.00)
	total_price = models.FloatField(default=0.00)
	if_paid = models.IntegerField(default=0)
	if_self_help = models.IntegerField(default=0)
	expect_time = models.IntegerField(default=0)
	leave_msg = models.CharField(max_length=255)
	status = models.IntegerField(default=ORDER_WAITING)
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
	receive_time = models.DateTimeField()
	push_time = models.DateTimeField()
	pull_time = models.DateTimeField()
	finish_time = models.DateTimeField()


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
	unit = models.CharField(max_length=10, default='个')
	sold_num = models.IntegerField(default=0)


class PaymentRecord(models.Model):
	customer_id = models.ForeignKey(Users.Customer)
	order_id = models.ForeignKey(Order)
	pay_way = models.CharField(max_length=50)


class WindowComment(models.Model):
	customer_id = models.ForeignKey(Users.Customer)
	window_id = models.ForeignKey(Window)
	score = models.FloatField()
	comment = models.CharField(max_length=255)
from orders.models import *

# Create your models here.


class PaymentRecord(models.Model):
	customer_id = models.ForeignKey(Customer)
	order_id = models.ForeignKey(Order, unique=True)
	pay_way = models.CharField(max_length=50)
	created_time = models.DateTimeField(auto_now_add=True)

	def create_payment(self):
		try:
			self.save()
			current_order = self.order_id
			current_order_record = OrderRecord.objects.get(order_id=current_order.id)
			if_update_state = current_order.update_order_state(ORDER_PAYED)
			if_append_paytime = current_order_record.append_payment_time()
			if if_append_paytime and if_update_state:
				return True
			else:
				return False
		except Exception, e:
			print(e)
			return False

from django.db import models


# Create your models here.
class Customer(models.Model):
	mail = models.CharField(max_length=40)
	phone = models.CharField(max_length=20)
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	score = models.IntegerField(default=0)

	def signup_customer(self):
		check_customer = self.get_customer_by_mail()
		if check_customer is None:
			self.save()
			return True
		else:
			return False

	def get_customer_by_mail(self):
		try:
			customer = Customer.objects.get(mail=self.mail)
		except Exception, e:
			return None
		else:
			return customer



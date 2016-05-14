# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from util.response_util import *
from util.general_util import *
from util.email_util import *
from models import Customer
from core.jsonresponse import *

reg_subject = u'[顺道儿]邮件验证'


def customers(request, customer_id=None):
	if request.method == 'POST':
		return post_customer(request)
	elif request.method == 'GET':
		return get_customer(request, customer_id)


def get_customer(request, customer_id=None):
	content = dict()
	customer = None
	# print('>>>>'+(customer_id))
	try:
		customer = Customer.objects.get(id=int(customer_id))
		if request.GET.get('validate', None) == 'true':
			validate_token = request.GET.get('token', None)
			Customer.objects.filter(id=int(customer_id), token=validate_token).update(status=1)
			new_user = User.objects.create_user(customer.mail, customer.mail, customer.password)
			content['status'] = 201
			content['msg'] = u'验证成功'
			return create_simple_response(201, json.dumps(content))
		else:
			content = customer.to_dict()
			return create_simple_response(200, json.dumps(content))
	except Exception as e:
		print(e)
		content['status'] = 404
		content['msg'] = '未找到'
		return create_simple_response(404, json.dumps(content))


def post_customer(request):
	customer_data = json.loads(request.body)
	mail = customer_data.get('mail', None)
	phone = customer_data.get('phone', None)
	password = customer_data.get('password', None)

	if mail is None or password is None or phone is None:
		content = dict()
		content['status'] = 422
		content['msg'] = u'信息缺失'
		return create_simple_response(422, json.dumps(content))

	new_customer = Customer()
	new_customer.mail = mail
	new_customer.phone = phone
	new_customer.password = password
	new_customer.token = generate_token()
	if_signed = new_customer.signup_customer()

	if if_signed:
		content = dict()
		try:
			query_str = 'customers/'+str(new_customer.id)+'?validate=true&token='+new_customer.token
			reg_msg = u'感谢您注册顺道儿,请点击链接完成验证: <a href="%s%s%s">- 验证 GO -</a>'%(BASE_SCHEMES, BASE_PATH, query_str)
			send_register_email(new_customer.mail, reg_msg, reg_subject)
		except:
			content['status'] = 422
			content['msg'] = u'验证失败'
		else:
			content['status'] = 201
			content['msg'] = u'注册成功,请登录邮箱进行验证'
			content['href'] = '%s%s%s' % (BASE_PATH, 'customers/', str(new_customer.id))
		finally:
			return create_simple_response(201, json.dumps(content))
	else:
		content = dict()
		content['status'] = 422
		content['msg'] = u'注册失败'
		return create_simple_response(422, json.dumps(content))


# 邮件验证CUSTOMER
# （提供该CUSTOMER的全部信息）
def put_customer(request):
	pass
	# customer_id = request.GET.get('customer_id')
	# verify_token = request.GET.get('verify_code')
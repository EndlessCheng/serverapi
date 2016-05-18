# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

from serverapi import settings
from util.response_util import *
from models import *


# Create your views here.

def login(request):
	if request.method == 'POST':
		return post_login(request)


def post_login(request):
	content = {}
	login_data = json.loads(request.body)
	username = login_data.get('username', None)
	password = login_data.get('password', None)

	if not username or not password:
		content['status'] = 422
		content['msg'] = u'用户名或密码为空'
		return create_simple_response(422, json.dumps(content))
	else:
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				content['status'] = 201
				content['msg'] = u'登陆成功'
				return create_simple_response(201, json.dumps(content))
			else:
				content['status'] = 422
				content['msg'] = u'用户失效'
				return create_simple_response(422, json.dumps(content))
		else:
			content['status'] = 422
			content['msg'] = u'用户名或密码错误'
			return create_simple_response(422, json.dumps(content))


@login_required
def test_session(request):
	user = authenticate(username='13301052@bjtu.edu.cn', password='123')
	return create_simple_response(200, json.dumps({'id': user.id, 'name': user.username}))


@login_required
def user_info(request):
	if request.method == 'GET':
		current_customer = Customer.objects.get(mail=request.user.email)
		return create_simple_response(200, json.dumps(current_customer.to_dict()))

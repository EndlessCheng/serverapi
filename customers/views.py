# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

from util.response_util import *


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
	return create_simple_response(200, json.dumps({'name': 'test'}))

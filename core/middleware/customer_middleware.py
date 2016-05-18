# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse


class CustomerAuthMiddleware():

	def process_request(self, request):
		if request.user.is_authenticated():
			return HttpResponse()
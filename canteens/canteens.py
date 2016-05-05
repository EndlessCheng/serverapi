# -*- coding: utf-8 -*-
import json
from django.http import HttpResponseRedirect

from models import *
from util.response_util import *


def canteens(request, canteen_id=None):
	if canteen_id:
		return HttpResponseRedirect('/v1/canteens/'+canteen_id)
	else:
		canteens_list = Canteen.objects.all()
		# canteens_dict = dict()
		canteens_arr = []

		for canteen in canteens_list:
			canteens_arr.append(canteen.to_dict())

		return create_simple_response(200, json.dumps(canteens_arr))

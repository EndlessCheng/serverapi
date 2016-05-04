# -*- coding: utf-8 -*-
import json

from models import *
from util.response_util import *

DEFAULT_CANTEEN_ID = 1


def home(request, canteen_id=None):
	if request.method == 'GET':
		if canteen_id is None:
			canteen_id = DEFAULT_CANTEEN_ID

		if canteen_id:
			window_list = []
			now_windows = Window.objects.filter(canteen_id=canteen_id)

			for window in now_windows:
				window_list.append(window.to_dict())

			return create_simple_response(200, json.dumps(window_list))
		else:
			content = dict()
			content['msg'] = 'resource not found'
			return create_simple_response(404, json.dumps(content))

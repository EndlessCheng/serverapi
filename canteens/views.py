# -*- coding: utf-8 -*-
import json

from models import *
from util.response_util import *

DEFAULT_CANTEEN_ID = 1


def home(request, canteen_id=None):
	if request.method == 'GET':
		if canteen_id is None:
			canteen_id = DEFAULT_CANTEEN_ID

		try:
			canteen_data = dict()
			window_list = []
			now_canteen = Canteen.objects.get(id=canteen_id)
			now_windows = Window.objects.filter(canteen_id=canteen_id)

			for window in now_windows:
				window_list.append(window.to_dict())

			canteen_data = now_canteen.to_dict()
			canteen_data['windows_data'] = window_list

			return create_simple_response(200, json.dumps(canteen_data))
		except:
			content = dict()
			content['msg'] = 'resource not found'
			return create_simple_response(404, json.dumps(content))

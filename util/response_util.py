from core.jsonresponse import *


def create_data_response(data):
	response = create_response(200)
	response.data = data
	return response.get_response()

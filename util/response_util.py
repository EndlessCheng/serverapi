from django.http import HttpResponse

BASE_SCHEMES = r'http://'
BASE_PATH = r'api.byway.net.cn/v1/'


def create_simple_response(code, content):
	response = HttpResponse()
	response.status_code = code
	response.content = content
	return response
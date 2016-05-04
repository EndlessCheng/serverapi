from django.http import HttpResponse

from tasks import _do_kground_work


def get(request):
	print('testing celery')
	_do_kground_work.delay('Celery')
	return HttpResponse('Hello, World !')

# python manage.py celery worker --loglevel=info
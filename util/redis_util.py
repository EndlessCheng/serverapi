import redis


class RConnectionPool(object):
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = redis.ConnectionPool(host='localhost', port=6379, db=10)
		return cls._instance
#
# def get_connection():
# 	pool = redis.ConnectionPool(host='localhost', port=6379, db=10)
# 	return redis.Redis(connection_pool=pool)
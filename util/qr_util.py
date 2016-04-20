import qrcode

from serverapi.settings import *


def generate_qrcode(url_info, qr_name):
	img = qrcode.make(url_info)

	with open(MEDIA_ROOT+'/qrcode/'+qr_name, 'w') as f:
		img.save(f)

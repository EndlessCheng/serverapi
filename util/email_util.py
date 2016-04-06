# -*- coding: utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

from_addr = '18813090635@163.com'
password = 'yan123456'
to_addr = '386670057@qq.com'
smtp_server = 'smtp.163.com'


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def send_register_email(aim, msg, subject):
	msg = MIMEText(msg, 'plain', 'utf-8')
	msg['From'] = _format_addr(from_addr)
	msg['To'] = _format_addr(to_addr)
	msg['Subject'] = Header(subject, 'utf-8').encode()

	server = smtplib.SMTP(smtp_server, 25)
	# server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()

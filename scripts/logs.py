from datetime import datetime
from typing import Optional
from multiprocessing import Process


def form_ip(i: int, x1: int, x2: int, y1: int, y2: int) -> str:
	"""
	Function forms and returns IP as a st
	:param i:
	:param x1:
	:param x2:
	:param y1:
	:param y2:
	:return:
	"""
	return f"10.0.{i * x1 % x2}.{i * y1 % y2}"


def form_date(i: int, time_int: int, option: Optional[int] = None) -> str:
	"""
	Function forms the date for logs
	:param i: loop int passed from run_loop method
	:param time_int: passed time str from log_stream1 or log_stream2
	:param option: Optional int passed from log_stream2 AKA 2.
	:return:
	"""
	if option:
		return datetime.fromtimestamp(time_int + i * option).strftime(
			"%Y-%m-%d %H:%M:%S"
		)
	else:
		return datetime.fromtimestamp(time_int + i).strftime("%Y-%m-%d %H:%M:%S")


def stdout(date: str, ip: str, code: int):
	"""
	print formed log to stdout
	:param date: log time
	:param ip: log ip
	:param code: http status code
	:return:
	"""
	dict_log = {"time": date, "ip": ip, "status_code": code}
	print(dict_log)


def log_stream1(i: int):
	"""
	this function is simple the bash script 1 rewritten in python
	:param i: loop int passed from run_loop method
	:return:
	"""
	ip: str = form_ip(i, 191, 256, 219, 250)
	date: str = form_date(i, 1557824751)
	code: int = int(i * 55 / 6 % 4 + 2) * 100 + (i * 19 % 4)
	stdout(date, ip, code)


def log_stream2(i: int):
	"""
	this function is simple the bash script 2 rewritten in python
	:param i: loop int passed from run_loop method
	:return:
	"""
	ip: str = form_ip(i, 19, 256, 37, 250)
	date: str = form_date(i, 1420063200, 2)
	code: int = int(i * 8 / 6 % 4 + 2) * 100 + (i * 13 % 4)
	stdout(date, ip, code)


def run_loop():
	for i in range(1, 1000001):
		log_stream1(i)
		log_stream2(i)


if __name__ == "__main__":
	p1 = Process(target=run_loop, )
	p1.start()
	p1.join()

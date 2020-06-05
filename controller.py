# _author_ = Johnleonard C.O
# _Date_ = 6/4/2020

from multiprocessing import Process, Manager, Array
from datetime import datetime
from typing import Optional


def form_ip(i: int, x1: int, x2: int, y1: int, y2: int) -> str:
	part1: int = i * x1 % x2
	part2: int = i * y1 % y2
	return f"10.0.{part1}.{part2}"


def form_date(i: int, time_int: int, option: Optional[int] = None) -> str:
	if option:
		return datetime.fromtimestamp(time_int + i * option).strftime("%Y-%m-%d %H:%M:%S")
	else:
		return datetime.fromtimestamp(time_int + i).strftime("%Y-%m-%d %H:%M:%S")


def error_status_code(logs: dict) -> tuple:
	if int(str(logs.get('status_code'))[:1]) == 5:
		date = datetime.strptime(logs.get('time'), '%Y-%m-%d %H:%M:%S')
		return str(date.date()) + '_' + logs.get('ip'), str(date.hour)


def user_log(ip, hour, visitors, hour_list):
	print("Flagged IP ----> ", ip, hour)
	if hour not in hour_list:
		hour_list.append(hour)
		visitors[hour] = []
	visitors[hour] += [ip]
	return visitors


def stdout(date: str, ip: str, code: int) -> dict:
	dict_log = {"time": date, "ip": ip, "status_code": code}
	print(dict_log)
	return dict_log


def log_stream1(arg1, arg2):
	print('Starting Stream 1')
	for i in range(10000):
		ip: str = form_ip(i, 191, 256, 219, 250)
		date: str = form_date(i, 1557824751)
		code: int = int((i * 55 / 6 % 4 + 2) * 100 + (i * 19 % 4))
		logged_ip_hr = error_status_code(stdout(date, ip, code))
		if logged_ip_hr:
			x, y = logged_ip_hr
			_ = user_log(x, y, arg1, arg2)


def log_stream2(arg1, arg2):
	print('Starting stream 2')
	for i in range(10000):
		ip: str = form_ip(i, 19, 256, 37, 250)
		date: str = form_date(i, 1420063200, 2)
		code: int = int((i * 8 / 6 % 4 + 2) * 100 + (i * 13 % 4))
		logged_ip_hr = error_status_code(stdout(date, ip, code))
		if logged_ip_hr:
			x, y = logged_ip_hr
			_ = user_log(x, y, arg1, arg2)


def count_uniq_ips(aata: dict):
	pass


if __name__ == '__main__':
	manager = Manager()
	shared_hour_list = manager.list()
	shared_visitors_dict = manager.dict()

	p1 = Process(target=log_stream1, args=(shared_visitors_dict, shared_hour_list))
	p2 = Process(target=log_stream2, args=(shared_visitors_dict, shared_hour_list))
	p1.start()
	p2.start()
	p1.join()
	p2.join()

	for i in shared_visitors_dict:
		print(i, shared_visitors_dict[i])


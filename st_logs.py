# _author_ = Johnleonard C.O
# _Date_ = 6/4/2020

from datetime import datetime
from typing import Optional
from tqdm import tqdm
from utils import log_set


def form_ip(
		i: int,
		x1: int,
		x2: int,
		y1: int,
		y2: int
) -> str:
	# part1: int = i * x1 % x2
	# part2: int = i * y1 % y2
	return f"10.0.{i * x1 % x2}.{i * y1 % y2}"


def form_date(
		i: int,
		time_int: int,
		option: Optional[int] = None
) -> str:
	if option:
		return datetime.fromtimestamp(time_int + i * option).strftime("%Y-%m-%d %H:%M:%S")
	else:
		return datetime.fromtimestamp(time_int + i).strftime("%Y-%m-%d %H:%M:%S")


def error_status_code(logs: dict) -> tuple:
	if int(str(logs.get('status_code'))[:1]) == 5:
		# date = datetime.strptime(logs.get('time'), '%Y-%m-%d %H:%M:%S')
		return (
			f"{str(datetime.strptime(logs.get('time'), '%Y-%m-%d %H:%M:%S').date())}_{logs.get('ip')}",
			f"{str(datetime.strptime(logs.get('time'), '%Y-%m-%d %H:%M:%S').hour)}"
		)


def errored_user_logging(
		ip: str,
		hour: str,
		visitors: dict,
		hour_list: list
):
	# log_set.info(fr"/!!\ Flagged IP ----> Date : {ip.split('_')[0]}, IP : {ip.split('_')[1]}, Hour : {hour} ")
	if hour not in hour_list:
		hour_list.append(hour)
		visitors[hour] = []
	visitors[hour] += [ip]
	return visitors


def stdout(
		date: str,
		ip: str,
		code: int
) -> dict:
	# log_set.info('"time": {}, "ip": {}, "status_code": {}'.format(date, ip, code))
	return {"time": date, "ip": ip, "status_code": code}


def log_stream1(arg1: dict, arg2: list):
	print('Starting Stream 1')
	for i in tqdm(range(1000000), desc="First Data Stream --> "):
		ip: str = form_ip(i, 191, 256, 219, 250)
		date: str = form_date(i, 1557824751)
		code: int = int((i * 55 / 6 % 4 + 2) * 100 + (i * 19 % 4))
		logged_ip_hr = error_status_code(stdout(date, ip, code))
		if logged_ip_hr:
			x, y = logged_ip_hr
			_ = errored_user_logging(x, y, arg1, arg2)


def log_stream2(arg1: dict, arg2: list):
	print('Starting stream 2')
	for i in tqdm(range(1000000), desc="Second Data Stream --> "):
		ip: str = form_ip(i, 19, 256, 37, 250)
		date: str = form_date(i, 1420063200, 2)
		code: int = int((i * 8 / 6 % 4 + 2) * 100 + (i * 13 % 4))
		logged_ip_hr = error_status_code(stdout(date, ip, code))
		if logged_ip_hr:
			x, y = logged_ip_hr
			_ = errored_user_logging(x, y, arg1, arg2)

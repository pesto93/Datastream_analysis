# _author_ = Johnleonard C.O
# _Date_ = 6/4/2020

from multiprocessing import (
	Process,
	Manager,
)
from st_logs import (
	log_stream1,
	log_stream2,
)


def count_uniq_ips(data: dict):
	for i in data:
		print(f"Hours: {i}, uniq_value : {len(set(data[i]))}, Total Value : {len(data[i])}")


def main() -> dict:
	manager = Manager()
	shared_hour_list = manager.list()
	shared_visitors_dict = manager.dict()

	p1 = Process(
		target=log_stream1,
		args=(
			shared_visitors_dict,
			shared_hour_list
		)
	)
	p1.start()
	p2 = Process(
		target=log_stream2,
		args=(
			shared_visitors_dict,
			shared_hour_list
		)
	)
	p2.start()
	p1.join()
	p2.join()
	return shared_visitors_dict


if __name__ == '__main__':
	count_uniq_ips(main())

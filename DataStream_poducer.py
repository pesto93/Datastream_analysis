from kafka import KafkaProducer
from json import dumps
import subprocess
import ast
from resources.utils import (
	SCRIPTS_DIR,
	topics,
	log_set,
)

# Kafka producer config
# Producers are the apps responsible to publish data into Kafka system.
# They publish data on the topic of their choice.
producer = KafkaProducer(
	bootstrap_servers='localhost:9092',
	value_serializer=lambda x: dumps(x).encode('utf-8')
)


def send_msg_to_topic(msg: dict, topic: str):
	"""
	Function sends json msg to a kafka topic for consumption based on the status code.
	See all topics in resources/utils.py
	This ensures extensibility of the system since a consumer can subscribe to any topic of choice and consume only data from that topic while
	ignoring the rest.
	:param msg: Json message
	:param topic: Topic to send to (check out resources/utils.py)
	:return:
	"""
	# You can print out the logs by commenting out this line.
	# log_set.info(f"Topic -> {topic} <--->  Message - > {msg}")
	producer.send(topic=topic, value=msg)
	producer.flush()


def check_status_code(logs: dict):
	"""
	function check the http status code of captured logs
	:param logs: logs msg
	:return:
	"""
	if str(logs.get('status_code'))[:1] == str(5):
		send_msg_to_topic(logs, topics.get("500"))
	else:
		send_msg_to_topic(logs, topics.get("others"))


def main():
	"""
	Function streams bash stdout, checks the status code and sends each log to there respective topics
	:return:
	"""
	# On Windows - you should have (similar) C:user\programs\GIT\bin\bash.exe in your environmental variable.
	# Since I am using windows at the moment I already have it my path.
	log_set.info("Reading Data From Bash STDOUT")
	proc = subprocess.Popen(
		[
			"bash",
			SCRIPTS_DIR / 'logs.sh'
		],
		stdout=subprocess.PIPE
	)
	while True:
		line = proc.stdout.readline()
		if not line:
			break
		# the code does filtering here
		check_status_code(ast.literal_eval(line.decode("utf8").rstrip()))


if __name__ == "__main__":
	main()

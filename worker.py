#!/usr/bin/env python
from kombu.mixins import ConsumerMixin
from kombu.utils import kwdict, reprcall
import logging
from log import logger
from queues import task_queues

class Worker(ConsumerMixin):
	
	def __init__(self, connection):
		self.connection = connection

	def get_consumers(self, Consumer, channel):
		return [Consumer(queues = task_queues,
						accept = ['pickle', 'json'],
						callbacks = [self.process_task])]
	
	def process_task(self, body, message):
		fun = body['fun']
		args = body['args']
		kwargs = body['kwargs']
		info = {"fun":fun, "args": args, "kwargs": kwargs}
		logger.info(info)
		try:
			fun(*args, **kwdict(kwargs))
		except Exception as exc:
			logger.error('task raised exception:%r', exc)
		message.ack()
	

if __name__ == '__main__':
	from kombu import Connection
	with Connection('amqp://admin:cress@localhost:5672//') as conn:
		try:
			worker = Worker(conn)
			worker.run()
		except KeyboardInterrupt:
			print('bye bye')

#!/usr/bin/env python
import logging

#create a logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

#create a handler,use for writing log to file
filehandler = logging.FileHandler('./log/worker.log')
filehandler.setLevel(logging.DEBUG)

#create another handler,user for writing log to terminal
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#define format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filehandler.setFormatter(formatter)
filehandler.setFormatter(formatter)

#add handler for logger
logger.addHandler(filehandler)
logger.addHandler(ch)

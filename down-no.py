#! /usr/bin/env python3
import logging
import sys
import datetime
import certstream

def print_callback(message, context):
    #logging.debug("Message -> {}".format(message))
    if message['message_type'] == "certificate_update":
        #all_domains = message['data']['leaf_cert']['all_domains']
        for entry in [entry for entry in message['data']['leaf_cert']['all_domains'] if entry.endswith(".no")]:
                sys.stdout.write(entry + "\n")
                sys.stdout.flush()

logging.basicConfig(format='[%(levelname)s:%(name)s] %(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.disabled = True
certstream.listen_for_events(print_callback)

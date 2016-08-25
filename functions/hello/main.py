#!/usr/bin/env python
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(event, context):
    try:
        logger.info('hello')
    except Exception as e:
        logger.error(e)

if __name__ == '__main__':
    import json
    import sys
    logging.basicConfig()
    ev = json.load(sys.stdin, encoding='utf-8')
    handle(ev, None)

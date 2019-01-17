# -*- coding: utf-8 -*-

import json
import time
import datetime
import dateutil.parser

reference = '{ "timestamp": "2018-11-26T03:54:20+03:00" }'

got = json.loads(reference)
timestamp = got['timestamp']

# Calculate the offset taking into account daylight saving time
print(dateutil.parser.parse(timestamp))
# print(datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%Z"))

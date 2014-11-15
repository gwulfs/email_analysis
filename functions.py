import json
import calendar
import re
from datetime import datetime


def read_from_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return json.loads(data)


def write_to_file(path, data):
    with open(path, 'wb') as f:
        f.write(json.dumps(data))


def get_bin_month(timestamp):
    # timestamp is unix timestamp
    date = datetime.utcfromtimestamp(timestamp)
    # get the first day,hour,minute,second of the month
    date = date.replace(day=1, hour=1, minute=1, second=1)
    # convert to utc timestamp
    return calendar.timegm(date.utctimetuple())


def get_bin_day(timestamp):
    # timestamp is unix timestamp
    date = datetime.utcfromtimestamp(timestamp)
    # get the first day,hour,minute,second of the month
    date = date.replace(hour=1, minute=1, second=1)
    # convert to utc timestamp
    return calendar.timegm(date.utctimetuple())


def extract_words(sentence):
    # replace all non-word characters with empty space
    return re.split(r" +", re.sub(r'[+{}=_\'"*,<>!?:;()\[\]\/\\.@#$]+', ' ', sentence).strip())

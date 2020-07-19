"""
@time: 2020-06-26 12:01
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""
import json
from json import JSONDecodeError

import requests


def request_translate(content):
    if not isinstance(content, str):
        raise TypeError('content must be a str')
    url = 'https://api.shanbay.com/bdc/search/?word={}'.format(content)
    res = requests.get(url)
    try:
        text = json.loads(res.text)
    except JSONDecodeError as e:
        print('word:', content)
        raise e
    return text

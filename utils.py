"""
@time: 2020-06-26 12:01
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""
import json
import pprint

import requests



def request_translate(content):
    if not isinstance(content, str):
        raise TypeError('content must be a str')
    url = 'https://api.shanbay.com/bdc/search/?word={}'.format(content)
    res = requests.get(url)
    text = json.loads(res.text)
    return text

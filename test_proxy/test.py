import random
import time

import requests


def get_random_proxy():
    '''随机从文件中读取proxy'''
    while 1:
        with open('proxies.txt', 'r') as f:
            proxies = f.readlines()
        if proxies:
            break
        else:
            time.sleep(1)
    proxy = random.choice(proxies).strip()
    return proxy


p = get_random_proxy()
h = 'https' if 'https' in p else 'http'
proxies = {h: p}
print(p)
status_code = requests.get('http://www.baidu.com', proxies=proxies, timeout=2).status_code
print(status_code)

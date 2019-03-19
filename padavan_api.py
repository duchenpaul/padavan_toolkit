'''A template for sending requests to websites'''
import logging

import requests
import urllib.parse
try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import base64


# proxies = { "http": "http://127.0.0.1:8888", }

class Padavan():
    """docstring for Padavan"""

    def __init__(self, username, password):
        self.host = '192.168.123.1'
        self.username = username
        self.password = password
        self.url = 'http://{}/'.format(self.host)
        self.authorization = base64.b64encode((username + ':' + password).encode()).decode()
        self.sess = requests.Session()
        self.headers = {
            'Host': self.host,
            'Connection': 'keep-alive',
            'Authorization': 'Basic {}'.format(self.authorization),
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

    def webpage_get(self, url, headers=None, allow_redirects=True):
        if headers is None:
            headers = dict()
        # print("Get: " + url)
        proxies = None
        self.resp = self.sess.get(
            url, headers=headers, allow_redirects=allow_redirects, verify=False, proxies=proxies)
        # print(self.resp.content.decode('utf-8').replace('\r\n', '\n'))
        return self.resp

    def webpage_post(self, url, data, headers=None):
        if headers is None:
            headers = dict()
        self.resp = self.sess.post(
            url, data=data, headers=headers, verify=False)
        return self.resp

    def save_page(self, page):
        with open('./test.html', 'w', encoding='utf-8') as f:
            f.write(page)
        print("Page has been saved as " + './test.html')

    def request_api(self, api_string):
        '''Returns result of api. 
            Take in api string, e.g: update.cgi?output=netdev
        '''
        api_url = self.url + api_string
        logging.info('Request url: {}'.format(api_url))
        print('Request url: {}'.format(api_url))
        self.resp = self.webpage_get(
            api_url, headers=self.headers, allow_redirects=True)
        return self.resp.text


if __name__ == '__main__':
    username, password = 'admin', 'admin'
    coconut_ins = Padavan(username, password)
    api_string = 'update.cgi?output=netdev'
    resp = coconut_ins.request_api(api_string)
    print(resp)

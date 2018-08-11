import json
import requests
import execjs
import hashlib
from fake_useragent import UserAgent

ua = UserAgent()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=100743473@10.169.0.84; JSESSIONID=aaaVQxP56Ef2r_X5mnOuw; ___rl__test__cookies=1533992957639; OUTFOX_SEARCH_USER_ID_NCOO=983011131.3688496; SESSION_FROM_COOKIE=youdao; UM_distinctid=16528fe950c9-05758f64de64f08-4c312b7b-e1000-16528fe950e1f6",
    "Referer": "http//fanyi.youdao.com/",
    "X-Requested-With": "XMLHttpRequest" }



# headers['User-Agent'] = ua.random

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
r = execjs.eval('"" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))')
S = "fanyideskweb"
D = "ebSeFb%=XZ%T[KZ)c(sy!"

    
    




def translate(word):
    n = word
    tol = S + n + r + D
    sign = hashlib.md5(tol.encode('utf-8')).hexdigest();
    data = {
        'action': 'FY_BY_ENTER',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'from': 'AUTO',
        'i': n, 
        'keyfrom': 'fanyi.web',
        'salt': r,
        'sign': sign, 
        'smartresult': 'dict',
        'to': 'AUTO',
        'typoResult': 'true',
        'version': '2.1'
    }
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        # print(response.json())
        # print(type(response.json()))
        return response.json()
    else:
        print('translation failed')
        return None

def get_result(result):
    if result.get('errorCode') == 0:
        print('input words: {}'.format(result['translateResult'][0][0]['src']))
        print('get result : {}'.format(result['translateResult'][0][0]['tgt']))
    else:
        print(result)


def main():
    word = input('please input words that you want to translate: ')
    trans = translate(word)
    get_result(trans)

if __name__ == '__main__':
    # print(headers['User-Agent'])
    main()


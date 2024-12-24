from functools import reduce
from hashlib import md5
import urllib.parse
import time
import requests
from typing import Tuple, Dict, Any

mixinKeyEncTab = [
    46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35, 27, 43, 5, 49,
    33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13, 37, 48, 7, 16, 24, 55, 40,
    61, 26, 17, 0, 1, 60, 51, 30, 4, 22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11,
    36, 20, 34, 44, 52
]

def getMixinKey(orig: str) -> str:
    '对 imgKey 和 subKey 进行字符顺序打乱编码'
    return reduce(lambda s, i: s + orig[i], mixinKeyEncTab, '')[:32]

def encWbi(params: Dict[str, Any], img_key: str, sub_key: str) -> Dict[str, str]:
    '为请求参数进行 wbi 签名'
    mixin_key = getMixinKey(img_key + sub_key)
    curr_time = round(time.time())
    params['wts'] = curr_time  # 添加 wts 字段
    
    # 按照 key 重排参数
    sorted_params = dict(sorted(params.items()))
    
    # 过滤 value 中的 "!'()*" 字符
    filtered_params = {
        k: ''.join(filter(lambda ch: ch not in "!'()*", str(v)))
        for k, v in sorted_params.items()
    }
    
    query = urllib.parse.urlencode(filtered_params)  # 序列化参数
    wbi_sign = md5((query + mixin_key).encode()).hexdigest()  # 计算 w_rid
    
    signed_params = filtered_params.copy()
    signed_params['w_rid'] = wbi_sign
    
    return signed_params

def getWbiKeys() -> Tuple[str, str]:
    '获取最新的 img_key 和 sub_key'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://www.bilibili.com/'
    }
    resp = requests.get('https://api.bilibili.com/x/web-interface/nav', headers=headers)
    resp.raise_for_status()
    json_content = resp.json()
    img_url: str = json_content['data']['wbi_img']['img_url']
    sub_url: str = json_content['data']['wbi_img']['sub_url']
    img_key = img_url.rsplit('/', 1)[1].split('.')[0]
    sub_key = sub_url.rsplit('/', 1)[1].split('.')[0]
    return img_key, sub_key

# 获取最新的 img_key 和 sub_key
img_key, sub_key = getWbiKeys()

# 准备并签名请求参数
params = {
    'foo': '114',
    'bar': '514',
    'baz': 1919810
}
signed_params = encWbi(params, img_key, sub_key)

awts =signed_params.get('wts')
awrid= signed_params.get('w_rid')

url = 'https://api.bilibili.com/x/space/wbi/acc/info'
final_params = {
    'mid': 8549831,
    'w_rid': signed_params.get('w_rid'),
    'wts': signed_params.get('wts')
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/xml',
    'Referer': 'https://www.bilibili.com/',
    'Origin': 'https://www.bilibili.com',
    'Cookie': 'enable_web_push=DISABLE;header_theme_version=CLOSE;hit-dyn-v2=1;FEED_LIVE_VERSION=V_FAVOR_WATCH_LATER;'
              'buvid_fp_plain=undefined;opus-goback=1;'
              'buvid3=F17F179B-7B05-6F7C-C48E-7CD13A5BA9DD17666infoc;b_nut=1717861217;'
              '_uuid=E46456FC-FBCF-DEE9-74106-9ADCE15C7108A15844infoc;'
              'rpdid=|(kmR~~klml|0J\'u~u~)YJ)uk;LIVE_BUVID=AUTO5317179154493908;blackside_state=0;'
              'CURRENT_BLACKGAP=0;SESSDATA=75571ac1%2C1737438997%2C41e07%2A71CjAbKc62U_3MlXbMvllEWqQrpEi6SYNy-MNcDqvHNDCq6dx4Q20gdptC9FOP5dNQvPkSVktRdmV2VUdZZzF5R2JzZUs0MDNIOHdiQ2x3MzE4dGFpZnNfcURBRjhFMVMyZzdhTGh5ZzBWRXlIN3FYb3dWRHktcEZoVERwU3V5ZlR1MHRldkk2UXFBIIEC;'
              'bili_jct=3998c7686889fc1174d9c5463fbdec60;fingerprint=fc1d4eba19e68d926e156656389b47b3;'
              'buvid_fp=fc1d4eba19e68d926e156656389b47b3;CURRENT_QUALITY=0;PVID=2;'
              'b_lsid=F43D14E7_193F63B2C5C;bmg_af_switch=1;bmg_src_def_domain=i2.hdslb.com;'
              'buvid4=DADC899C-091A-1147-178F-846D0BEB0A3A94791-024122401-3tubV4O8sG7LttNU48bmyw%3D%3D;'
              'bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzUyNjIwOTQsImlhdCI6MTczNTAwMjgzNCwicGx0IjotMX0.bmQWuYFZ30EYDGs9lF7QVecZHaBXdXqPswfEMQaDRnY;'
              'bili_ticket_expires=1735262034;CURRENT_FNVAL=2000;sid=7cwakdi0;home_feed_column=4;'
              'browser_resolution=464-851',  
}

response = requests.get(url=url, headers=headers, params=final_params)

response.encoding=response.apparent_encoding
data = response.json()
print(data)
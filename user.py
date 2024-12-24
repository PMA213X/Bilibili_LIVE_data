import requests
import re
#直播间基本信息提取
def get_user_info(mid):
    url = 'https://api.bilibili.com/x/web-interface/card'
    params = {
            'mid':mid
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

    response = requests.get(url=url, headers=headers, params=params)

    response.encoding=response.apparent_encoding
    data = response.json()
    
    # 添加错误处理
    if 'data' not in data or 'card' not in data['data']:
        return {
            '性别': '未知',
            '等级': '未知',
            'VIP类型': -9999,
            '官方认证类型': -99999,
            '用户名': '未知',
        }
    
    card_data = data['data']['card']
    vip_data = card_data['vip']
    official_data = card_data['Official']
    extracted_info = {
            '性别': card_data.get('sex', '未提供'),
            '等级': card_data.get('level_info', {}).get('current_level', '未知'),
            'VIP类型': vip_data.get('type', -9999),
            '官方认证类型': official_data.get('type', -99999),
            '用户名': card_data.get('name', '未知'),
        }

    return extracted_info

import requests
import re

url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=203469289'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/xml',
    'Referer': 'https://www.bilibili.com/',
    'Origin': 'https://www.bilibili.com',
    'Cookie': 'your_cookie_here',  
}

response = requests.get(url=url,headers=headers)

response.encoding=response.apparent_encoding

data_list =re.findall('<d p=".*?">(.*?)</d>',response.text)

for index in data_list:
    with open('弹幕.txt',mode='a',encoding='UTF-8') as f:
        f.write(index)
        f.write('\n')
    print(index)
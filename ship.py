from time import sleep, time
import requests
import re
import json

# 直播间基本信息提取
base_url = 'https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList'
room_id = 31368680
ruid = 1694351351
page_size = 27

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/xml',
    'Referer': 'https://www.bilibili.com/',
    'Origin': 'https://www.bilibili.com',
    'Cookie': 'your_cookie_here',
}

def print_user_info(item, prefix=""):
    rank = item.get('rank', 'N/A')
    username = item.get('username', 'N/A')
    medal_name = item['medal_info'].get('medal_name', 'N/A') if 'medal_info' in item else 'N/A'
    medal_level = item['medal_info'].get('medal_level', 'N/A') if 'medal_info' in item else 'N/A'
    accompany = item.get('accompany', 'N/A')
    
    print(f"{prefix}排名: {rank},\t  粉丝牌名称: {medal_name},    "
          f"粉丝牌等级: {medal_level},    大航海陪伴时间: {accompany},      用户名: {username}")

page = 1
top3_printed = False
start_time = time()
while True:
    if time() - start_time > 10:
        break
    
    url = f'{base_url}?roomid={room_id}&page={page}&ruid={ruid}&page_size={page_size}'
    response = requests.get(url=url, headers=headers)
    data = response.json()
    
    user_list = data.get('data', {}).get('list', [])
    top3_list = data.get('data', {}).get('top3', [])
    if page == 1 :

        for item in top3_list:
            print_user_info(item, prefix="Top ")
        top3_printed = True

    if not user_list and not top3_list:
        break
    
    # 提取并打印 'list' 中的用户信息
    for item in user_list:
        print_user_info(item)
    
    page += 1



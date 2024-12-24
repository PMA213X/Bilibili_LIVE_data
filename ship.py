from time import sleep, time
import requests
import re
import json
import user


# 直播间基本信息提取
base_url = 'https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList'
room_id = 21672023
ruid = 477317922
page_size = 27
a = 'Miki'
b = f"{a}{int(time())}"
ship = []

def save_to_json(data, filename):
    with open(filename + '.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json',
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
    uid = item.get('uid', 'N/A')
    
    # 获取用户更多信息
    user_info = user.get_user_info(uid)
    gender = user_info['性别']
    level = user_info['等级']
    vip_type = user_info['VIP类型']
    official_type = user_info['官方认证类型']
    
    print(f"{prefix}排名: {rank},\t  粉丝牌名称: {medal_name},    "
          f"粉丝牌等级: {medal_level},    "
          f"\t性别: {gender},\t等级: {level},"
          f"\tVIP类型: {vip_type},\t官方认证类型: {official_type},\t大航海陪伴时间: {accompany},\t用户名: {username}")
    
    user_info_dict = {
        'rank': rank,
        'username': username,
        'medal_name': medal_name,
        'medal_level': medal_level,
        'accompany': accompany,
        'uid': uid,
        '性别': gender,
        '等级': level,
        'VIP类型': vip_type,
        '官方认证类型': official_type
    }
    
    # 添加到 ship 列表
    ship.append(user_info_dict)

page = 1

while True:
    url = f'{base_url}?roomid={room_id}&page={page}&ruid={ruid}&page_size={page_size}'
    response = requests.get(url=url, headers=headers)
    data = response.json()
    
    user_list = data.get('data', {}).get('list', [])
    top3_list = data.get('data', {}).get('top3', [])
    if page == 1:
        for item in top3_list:
            print_user_info(item, prefix="Top ")
    
    if not user_list:
        break
    
    # 提取并打印 'list' 中的用户信息
    for item in user_list:
        print_user_info(item)
    
    page += 1

# 保存到本地文件夹
save_to_json(ship, b)

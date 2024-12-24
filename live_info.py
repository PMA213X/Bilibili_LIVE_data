import requests
import re
#直播间基本信息提取
def livedata(room_id):

    url = 'https://api.live.bilibili.com/room/v1/Room/get_info'
    params = {
            'room_id':room_id
        }
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/xml',
        'Referer': 'https://www.bilibili.com/',
        'Origin': 'https://www.bilibili.com',
        'Cookie': 'your_cookie_here',  
    }

    response = requests.get(url=url, headers=headers, params=params)

    response.encoding=response.apparent_encoding
    data = response.json()
    room_data = data['data']
    print(f"UID: {room_data['uid']}")
    print(f"Room ID: {room_data['room_id']}")
    print(f"Attention: {room_data['attention']}")
    print(f"Online: {room_data['online']}")
    print(f"Live Status: {'直播中' if room_data['live_status'] == 1 else '未直播'}")
    print(f"Title: {room_data['title']}")
    print(f"Live Time: {room_data['live_time']}")
    print(f"Area Name: {room_data['area_name']}")
    print(f"Parent Area Name: {room_data['parent_area_name']}")
    print("Hot Words:", ", ".join(room_data['hot_words']))
    
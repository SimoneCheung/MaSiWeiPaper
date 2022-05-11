import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
import random


#########################################
#########################################

## 设置爬取参数
## pids 为博文参数
## uid 为用户 id
pids = [4765751774544077] # 博文 id
uid = 6570121219 # 微博用户 id


##########################################
##########################################

def fetchUrl(cursor):

    # url
    url = "https://www.douyin.com/aweme/v1/web/comment/list/"

    # request_headers
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36", "cookies":"__ac_nonce=0627bb74f0004caa5c465",
        
    }

    params = {
       
       'device_platform': 'webapp',
       'aid': '6383',
       'channel': 'channel_pc_web',
       'aweme_id': '7093811362492648715',
       'cursor': 105 + cursor * 20,
       'count': '20',
       'version_code': '170400',
       'version_name': '17.4.0',
       'cookie_enabled': 'true',
       'screen_width': '1920',
       'screen_height': '1080',
       'browser_language': 'zh-CN',
       'browser_name': 'Chrome',
       'browser_version': '100.0.4896.127',
       'browser_online': 'true',
       'engine_name': 'Blink',
       'engine_version': '100.0.4896.127',
       'os_name': 'Windows',
       'os_version': '10',
       'cpu_core_num': '4',
       'device_memory': '8',
       'platform': 'PC',
       'downlink': '10',
       'effective_type': '4g',
       'round_trip_time': '0',
       'webid':'7096467145814836775',
       'msToken':'57cqPeMEmONnuBx_4ukTH_3QFm6bd4F2rRmAqcbxEuqBRaTrg2kL1TXy1qy7TRuI9W_f7znDAbalt3QXUkgZ6yP2YcFB6tmd0V1jXE7uRcG6',
       'X-Bogus': 'DFSzswVLEltANC5eSWttewOZax5/',
       '_signature':
        '_02B4Z6wo00001aKTlcgAAIDCfv-KYY0L.22ik5FAAArgb7',
   
    }

    r = requests.get(url, headers=headers, params=params)
    return r.json()


def save_data(data, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    dataframe = pd.DataFrame(data)
    dataframe.to_csv(path + filename, encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)


def parseJson(jsonObj):
    data = jsonObj["data"]


    commentData = []
    for item in data:
        # 评论id
        aweme_id = item["aweme_id"]
        # 评论内容
        content = BeautifulSoup(item["text"], "html.parser").text
        # 评论时间
        create_time = item["create_time"]
        # 点赞数
        digg_count = item["digg_count"]
        # 评论数
        total_number = item["total_number"]

        # 评论者 id，name，city
        user = item["user"]
        userID = user["id"]
        userName = user["name"]
        userCity = user["location"]

        dataItem = [aweme_id, create_time, userID, userName, userCity, like_counts, total_number, content]
        print(dataItem)
        commentData.append(dataItem)

    return commentData, max_id



path = "./comments/"  # 保存评论位置
csvHeader = [["评论id", "发布时间", "用户id", "用户昵称", "用户城市", "点赞数", "回复数", "评论内容"]]

for cursor in range(10):
    max_id = 0
    filename = 'cmt' + '.csv'
    save_data(csvHeader, path, filename)
    while True:
        time.sleep(random.random() * 3)
        html = fetchUrl(cursor)
        comments, max_id = parseJson(html)
        save_data(comments, path, filename)
        # max_id 为 0 时，表示爬取结束
        if max_id == 0:
            break
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
import random


#########################################
#########################################



##########################################
##########################################

def fetchUrl(cursor):

    # url
    url = "https://www.douyin.com/aweme/v1/web/comment/list/"

    # request_headers
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36", 
        
        "cookies":"strategyABtestKey=1652283920.012; _tea_utm_cache_1300=undefined; passport_csrf_token=a90e88ab4fa70b61a1f90c846737d291; passport_csrf_token_default=a90e88ab4fa70b61a1f90c846737d291; _tea_utm_cache_2285=undefined; s_v_web_id=verify_l31r6q1n_xVCfomFS_IZXZ_4cfA_BmvZ_lyon9eUKzu3f; ttcid=882812087b2d430faf5f8f5f8535f21831; AB_LOGIN_GUIDE_TIMESTAMP=1652283919815; _tea_utm_cache_6383=undefined; msToken=xF6WpzxaWOjtVw1P9pyCZ6quDJrPbqwmZcI-cJcIbZa-NFzwMra_lIPaUPwbyuqHyngEoPy-i23oQWbf-VL9-xXAYLKhFUexZolb9JS6lglx; n_mh=5ZZ39lrcO7SlmdB1ATbKg--QV7Bacaw0i2EAqqecX0Y; sso_uid_tt=f6c46beba2a2d74041411785481d4fa7; sso_uid_tt_ss=f6c46beba2a2d74041411785481d4fa7; toutiao_sso_user=7d68d655da74f9c101cfa57a02ca5a61; toutiao_sso_user_ss=7d68d655da74f9c101cfa57a02ca5a61; sid_ucp_sso_v1=1.0.0-KDdiMWM1Mzg0ZWQzZDg4ZDI3NThiZTk2YTFmZmI0ZjVlOTY0ZjM2YTIKHwiw7fCv3fTpAxDPtO-TBhjvMSAMMKu99vIFOAZA9AcaAmxmIiA3ZDY4ZDY1NWRhNzRmOWMxMDFjZmE1N2EwMmNhNWE2MQ; ssid_ucp_sso_v1=1.0.0-KDdiMWM1Mzg0ZWQzZDg4ZDI3NThiZTk2YTFmZmI0ZjVlOTY0ZjM2YTIKHwiw7fCv3fTpAxDPtO-TBhjvMSAMMKu99vIFOAZA9AcaAmxmIiA3ZDY4ZDY1NWRhNzRmOWMxMDFjZmE1N2EwMmNhNWE2MQ; __ac_nonce=0627bda510002ec8e685e; __ac_signature=_02B4Z6wo00f01aJCGfQAAIDCfi4GXDzbJD2iYh1AAArs6b; uid_tt=f6c46beba2a2d74041411785481d4fa7; uid_tt_ss=f6c46beba2a2d74041411785481d4fa7; sid_tt=7d68d655da74f9c101cfa57a02ca5a61; sessionid=7d68d655da74f9c101cfa57a02ca5a61; sessionid_ss=7d68d655da74f9c101cfa57a02ca5a61; sid_guard=7d68d655da74f9c101cfa57a02ca5a61%7C1652283996%7C5184000%7CSun%2C+10-Jul-2022+15%3A46%3A36+GMT; sid_ucp_v1=1.0.0-KGIzMzIwYjU0MmI5NjFhYTAwMjcwZDIxZTI1NTE3ZDIyMWVhZDJlZmUKHwiw7fCv3fTpAxDctO-TBhjvMSAMMKu99vIFOAZA9AcaAmxmIiA3ZDY4ZDY1NWRhNzRmOWMxMDFjZmE1N2EwMmNhNWE2MQ; ssid_ucp_v1=1.0.0-KGIzMzIwYjU0MmI5NjFhYTAwMjcwZDIxZTI1NTE3ZDIyMWVhZDJlZmUKHwiw7fCv3fTpAxDctO-TBhjvMSAMMKu99vIFOAZA9AcaAmxmIiA3ZDY4ZDY1NWRhNzRmOWMxMDFjZmE1N2EwMmNhNWE2MQ; ttwid=1%7Ccv86OqdaRjoJMu9gRNHQSzxwoEwaKDGDFSyS7r8d2UI%7C1652283997%7C78012c1984eeb8072b42cb66605670ee92666bbf83ba4d15635f12fb81c535b0; msToken=vjPzPVGRazsPq-1XXVMjKvggGBAd51Da3moDJW3nzsoN_UbtM7D_5TKkIhb0WHSoyBM2684BQ9RTEsqbXO1BOwmzsFo7l84NOXy8GkTBHZ2D; odin_tt=92134afde30e9b13b910cdccbf64f86cfd33fd46e0b3e697207e188dd5f46cefe91f70953eab46bb630ec556ce497140e9f1a69f72ea090af548c1f1ebded2d3; home_can_add_dy_2_desktop=1; pwa_guide_count=1; THEME_STAY_TIME=299623; IS_HIDE_THEME_CHANGE=1",
        
    }

    params = {
       
       'device_platform': 'webapp',
       'aid': '6383',
       'channel': 'channel_pc_web',
       'aweme_id': '7093811362492648715',
       'cursor': 125 + cursor * 20,
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
        '_02B4Z6wo00001S59XYgAAIDC8hFCIGoBJSEufVkAACnnae',
   
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
    for comment in data:
        # 评论id
        aweme_id = comment["aweme_id"]
        # 评论内容
        content = BeautifulSoup(comment["text"], "html.parser").text
        # 评论时间
        create_time = comment["create_time"]
        # 点赞数
        digg_count = comment["digg_count"]
        # 评论数
        #total_number = item["total_number"]

        # 评论者 id，name，city
        user = comment['user']['nickname'] 
        userID = comment["cid"]
        #userName = user["name"]
        #userCity = user["location"]

        dataItem = [aweme_id, create_time, user, userID, digg_count, content]
        print(dataItem)
        commentData.append(dataItem)

    return commentData, max_id



path = "./comments/"  # 保存评论位置
csvHeader = [["评论id", "发布时间", "用户", "用户id", "点赞数", "评论内容"]]

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
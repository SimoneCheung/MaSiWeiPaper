import requests

for cursor in range(10):
    params = (
       ('device_platform', 'webapp'),
       ('aid', '6383'),
       ('channel', 'channel_pc_web'),
       ('aweme_id', '7093811362492648715'),
       ('cursor', str(105+cursor*20)),
       ('count', '20'),
       ('version_code', '170400'),
       ('version_name', '17.4.0'),
       ('cookie_enabled', 'true'),
       ('screen_width', '1920'),
       ('screen_height', '1080'),
       ('browser_language', 'zh-CN'),
       ('browser_name', 'Chrome'),
       ('browser_version', '100.0.4896.127'),
       ('browser_online', 'true'),
       ('engine_name', 'Blink'),
       ('engine_version', '100.0.4896.127'),
       ('os_name', 'Windows'),
       ('os_version', '10'),
       ('cpu_core_num', '4'),
       ('device_memory', '8'),
       ('platform', 'PC'),
       ('downlink', '10'),
       ('effective_type', '4g'),
       ('round_trip_time', '0'),
       ('msToken',
        'xO8ykiImW4_y1P17rjjV82tkToK8sdVUSXsck7dqlo5egXnsLielL_-gNoh0eTlNzohikTmdqccSsY3Es0-we3HmgJYX-jaWe7rO1uKCGLQSCz4tUKiWsZwpNQ=='),
       ('X-Bogus', 'DFSzswVuuEtANasbSiKxme9WX7j6'),
       ('_signature',
        '_02B4Z6wo00001cGgFBAAAIDBQaLuUEhgJOnBoBCAABHQa2zGW56-brVbd8zPJMMr5zV9wMRK.Fw-baUMHl14.I7n6EC4lETZbOyGYyoi08uVzPer1kHjbwJPWfXZBARPia3I0l-u0HyASZI012'),
   )

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "cookies":"__ac_nonce=0627bb74f0004caa5c465",
    }
    response = requests.get('https://www.douyin.com/aweme/v1/web/comment/list/', headers=headers, params=params)


r = response.json()['comments']  
for i in r:
   with open('comment.txt', 'a') as f:
       f.write(i['text'])
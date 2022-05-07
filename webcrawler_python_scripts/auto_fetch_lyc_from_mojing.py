from bs4 import BeautifulSoup
from matplotlib.pyplot import get
import requests 
import pandas as pd
import os

def fetchlyc(lycid):
    url = 'https://mojim.com'+str(lycid)
    print (lycid)
    headers = {       
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "cookies":"PHPSESSID=9l8ln3vb9hoduos1neo445p0tj",    
        }
    r = requests.get(url, headers=headers) # 向网站发送请求
    demo = r.text  # demo为抓取的ml数据  

    soup = BeautifulSoup(demo, 'html.parser')  # 抓取的页面数据；bs4的解析器
    # Here we can output the parsed HTML page in a hierarchical structure
    # print(soup.prettify())

    title = soup.find(id="fsZx2").get_text()
    print (title)
    lyc = soup.find(id="fsZx3").get_text()
    print (lyc)
    return title, lyc

def save_data(data, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    dataframe = pd.DataFrame(data)
    dataframe.to_csv(path + filename, encoding='utf_8_sig', mode='a', index=False, sep=',', header=False)

path = "./lyc/"  # where to store the output file
csvHeader = [["title", "lyc"]]
filename = 'dataoutput.csv' # the name of the output csv file
content=[]
save_data(csvHeader, path, filename)
f = open ("lycids.txt",'r') # This file is to store all the links of songs, such as "/cny216829x11x1.htm"
lines = f.readlines() # Read all the lines from the file
for line in lines:
    lycid=line.strip()
    title,lyc = fetchlyc(lycid) # fetch the song titles and lyrics
    content = [[title,lyc]]
    save_data(content, path, filename) # write into csv
f.close()

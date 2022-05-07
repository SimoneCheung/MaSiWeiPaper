import requests
from bs4 import BeautifulSoup

url = 'https://mojim.com/cnh189797.htm' # here is the url of the singer information
headers = {       
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
   "cookies":"PHPSESSID=9l8ln3vb9hoduos1neo445p0tj",    
   }
r = requests.get(url, headers=headers) # 向网站发送请求
demo = r.text  # demo为抓取的ml数据  
#创建一个BeautifulSoup解析对象
soup = BeautifulSoup(demo,"html.parser")
#获取所有的链接
links1 = soup.select('span[class="hc3"] a')
links2 = soup.select('span[class="hc4"] a')
links = links1 + links2

print ("所有的链接")
for link in links:
 #   print (link.name,link['href'],link.get_text())
 #   print (link['href'],link['title'])
 #    print (link['title'])
    print (link['href'])
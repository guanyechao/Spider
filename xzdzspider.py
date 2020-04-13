import requests
from bs4 import BeautifulSoup
# 请求头
headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
          }
# 先爬第一页：
url = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'
res = requests.get(url,headers = headers)
soup = BeautifullSoup(res.text,'lxml')
print(soup.prettify())

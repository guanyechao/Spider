### 案例1：爬取小猪短租北京地区短租房信息
##### 1. 库： 
      `requests，BeautifulSoup`

##### 2. 爬虫思路分析：
> 网址
  请求网址:http://bj.xiaozhu.com/ <br>
  请求方法:GET  <br>
  Host: bj.xiaozhu.com  <br>
  User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0 <br>
  第一页url:http://bj.xiaozhu.com/ &nbsp;&nbsp;&emsp;http://bj.xiaozhu.com/search-duanzufang-p1-0/ <br>
  第二页url:http://bj.xiaozhu.com/search-duanzufang-p2-0/  <br>
  第三页url:http://bj.xiaozhu.com/search-duanzufang-p3-0/  <br>
   
> 需求信息：
标题、地址、价格、房东名称、房东姓名、房东图像链接

##### 3. 爬虫代码分析：

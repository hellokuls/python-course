import requests
from bs4 import BeautifulSoup
import re
import csv
import _thread
import time
User_Agent = 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'
headers = {
    'User-Agent': User_Agent,
}
# 获取每一页的所有电影下载链接
def get_new_movie(page):
    r = requests.get(url="https://www.ygdy8.com/html/gndy/dyzz/list_23_{}.html".format(page), headers=headers) 
    
    r.encoding = 'gb2312' #因为该网站的编码是gb2312，所以这里我们需要设置一下编码，否则会报错
    html = r.text
    name_list = [] # 用来装获取到的电影名称
    download_list = [] # 用来装获取到的电影下载链接
    bs = BeautifulSoup(html, "html.parser") # 用BeautifulSoup进行html解析
    b = bs.findAll(class_="co_content8")
    b = b[0].findAll(class_="ulink") # 此处拿到了每一页中的电影列表
    for i in range(0, len(b)):
        name = b[i].get_text() # 获取每个电影的名称
        href = "https://www.ygdy8.com/"+b[i].get("href") # 获取每个电影的详情页面的url
        print(b[i].get_text())
        r1 = requests.get(url=href,headers=headers) # 访问每部电影的详情页面
        r1.encoding = 'gb2312'
        html1 = r1.text
        bs1 = BeautifulSoup(html1, "html.parser")
        b1 = bs1.find("tbody").find_next("td").find_next("a")
        download_url = b1.get("href") # 获取到下载链接
        print(download_url)
        name_list.append(name)
        download_list.append(download_url)
    return name_list,download_list


def get_total_page(url):
    r = requests.get(url=url,headers=headers)
    r.encoding = 'gb2312'

    pattern = re.compile(r'(?<=页/)\d+') # re解析
    t = pattern.findall(r.text)

    return int(t[0])


def wirte_into_csv(name,down_url):
    f = open('最新电影.csv', 'a+', encoding='utf-8') # a+表示追加
    csv_writer = csv.writer(f)
    csv_writer.writerow([name,down_url])
    f.close()

def run(start_page, end_page):
    for p in range(start_page, end_page):
        name_list, down_list = get_new_movie(p)
        for i in range(0, len(name_list)):
            wirte_into_csv(name_list[i],down_list[i])
        time.sleep(3)

if __name__ == '__main__':

    # get_new_movie()
    total_page = get_total_page("https://www.ygdy8.com/html/gndy/oumei/list_7_1.html")
    total_page = int(total_page/25+1)
    end = int(total_page/4)
    print(end)
    # 创建四个线程，并对其分配任务
    try:
        _thread.start_new_thread(run, (1, end))
        _thread.start_new_thread(run, (end+1, end*2))
        _thread.start_new_thread(run, (end*2 + 1, end * 3))
        _thread.start_new_thread(run, (end*3 + 1, end * 4))
    except:
        print("Error: 无法启动线程")

    while(1):
        pass


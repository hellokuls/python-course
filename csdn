import requests
from bs4 import BeautifulSoup
cookie = '填写你的cookie'
User_Agent = 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'
headers = {
    'User-Agent': User_Agent,
    'cookie': cookie,
'referer': 'https://mp.csdn.net/console/article',
}

for i in range(1,11): # 你的页数，自己修改
    url = 'https://blog.csdn.net/qq_36547531/article/list/'+str(i)
    r = requests.get(url=url,headers=headers)
    s = BeautifulSoup(r.text,'html.parser')
    t = s.find_all(class_='article-item-box')
    for item in t:
        if item:
            s1 = BeautifulSoup(str(item),'html.parser')
            type1 = s1.find(class_='type-2')
            if type1 is not None:

                headers1 = {
                            'User-Agent': User_Agent,
                            'cookie': cookie,
                            }
                print(item['data-articleid'])
                url1 = 'https://blog.csdn.net/phoenix/web/v1/articleListApi/del'
                data = {'articleId': int(item['data-articleid'])}
                r1 = requests.post(url=url1,data=data,headers=headers1)
                print(r1.text)

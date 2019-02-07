'''
 自动下载１３６书屋的小说   - power  IT资源君
'''
# 用于获取网页的html
from urllib import request
# 用于解析html
from bs4 import BeautifulSoup

# 得到网页的html


def getHtml(url):
    url = url
    res = request.urlopen(url)
    res = res.read().decode()
    # print(res)
    return res


# 解析小说章节页面,获取所有章节的子链接


def jsoupUrl(html):
    # 获取soup对象
    url_xiaoshuo = BeautifulSoup(html)
    # 因为我们要拿取class为box1中的div
    class_dict = {'class': 'box1'}
    url_xiaoshuo = url_xiaoshuo.find_all('div', attrs=class_dict)
    # 因为分析html中的代码可以发现div的class为box1的有两个,通过上面的代码返回的是一个list格式的结果，所以下面的索引应该是１
    # 我们要获取li中的值，所以find_all，这个方法返回的是一个ｌｉｓｔ集合
    url_xiaoshuo = url_xiaoshuo[1].find_all('li')
    # print(url_xiaoshuo)
    # 创建一个集合,用于存放每个章节的链接
    url_xs = []
    for item in url_xiaoshuo:
        # 获取每个元素中的href值
        url = item.a['href']
        # 将值传入url_xs集合中
        url_xs.append(url)
    return url_xs


# 解析小说每个章节的的主要内容

def jsoupXiaoshuo(list):
    for item in list:
        html = getHtml(item)
        html = BeautifulSoup(html)
        # 获取小说标题
        title = html.h1.get_text()
        xiaoshuo = html.find_all('p')

        for item in xiaoshuo:
            str = item.get_text()
            # open中的第二个参数是让每一次的字符串接连到上一个字符串，千万不能是ｗ
            with open(title + '.txt', 'a') as f:
                f.write(str+'\n')


if __name__ == '__main__':
    html = getHtml("http://www.136book.com/dadaozhaotian/")

    url_xs = jsoupUrl(html)

    jsoupXiaoshuo(url_xs)

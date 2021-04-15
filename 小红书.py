from mitmproxy import ctx
import re
import requests
import json
import csv
from lxml import etree
from bs4 import BeautifulSoup
# 获取收藏数和评论数
def get_star_comment(url):
    headers = {
        "Connection": "keep-alive",
        "Host": "www.xiaohongshu.com",
        "cookie":"xhsTrackerId=b3185969-98c5-4082-c0e2-6c9d856c44bb; extra_exp_ids=gif_clt1,ques_exp1; xhs_spses.5dde=*; xhs_spid.5dde=779bba5dba98beab.1610936353.1.1610936365.1610936353.97d8475b-f50a-4129-822c-4f7c6fa5e5ce",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    }
    html=requests.get(url=url,headers=headers).text
    bs = BeautifulSoup(html, "html.parser")

    star=bs.find(class_="star")
    star = star.span.get_text()
    comment=bs.find(class_="comment")
    comment = comment.span.get_text()
    return [star,comment]


contents_all=[]

try:
    # 所有的请求都会经过request
    def request(flow):

        if 'https://www.xiaohongshu.com/fe_api/burdock/weixin/v2/search/notes' in flow.request.url:
            authorization=re.findall("authorization',.*?'(.*?)'\)",str(flow.request.headers))[0]
            x_sign=re.findall("x-sign',.*?'(.*?)'\)",str(flow.request.headers))[0]
            url=flow.request.url

            headers = {
                "authorization":authorization,
                "x-sign": x_sign,
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.21(0x17001525) NetType/WIFI Language/zh_CN',
            }
            html = requests.get(url=url, headers=headers, verify=False).text
            # print(html)
            content = json.loads(html)
            f = open('小红书.csv', 'a+', encoding='utf-8')  # a+表示追加
            csv_writer = csv.writer(f)
            for i in range(len(content["data"]["notes"])):
                id = content["data"]["notes"][i]["id"]
                title = content["data"]["notes"][i]["title"]
                img_user = content["data"]["notes"][i]["user"]["image"]
                like = content["data"]["notes"][i]["likes"]
                user = content["data"]["notes"][i]["user"]["nickname"]
                user_id = content["data"]["notes"][i]["user"]["id"]
                time = content["data"]["notes"][i]["time"]

                note_url = "https://www.xiaohongshu.com/discovery/item/" + str(id)
                # star1 = get_star_comment(note_url)[0]
                # comment1 = get_star_comment(note_url)[1]

                # t1="id: {},标题：{},喜欢：{},用户名：{},用户头像：{}, 用户id: {}, 发布时间：{}, 收藏数：{}, 评论数: {}".format(id,title,like,user,img_user,user_id,time,star1, comment1)+"\n"
                # print(t1)
                t1 = "id: {},标题：{},喜欢：{},用户名：{},用户头像：{}, 用户id: {}, 发布时间：{}".format(id, title, like,
                                                                                                    user, img_user,
                                                                                                    user_id, time,
                                                                                                  ) + "\n"
                print(t1)
                csv_writer.writerow([id,title,like,user,img_user,user_id,time])
            f.close()
except:
    pass

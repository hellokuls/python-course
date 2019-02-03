# -*- coding: utf-8 -*-
import itchat
from pandas import DataFrame
import matplotlib.pyplot as plt
# 登录微信
itchat.login()
# 获取朋友列表
friends = itchat.get_friends(update=True)
# 利用pandas把数据转化成DataFrame形式
frame = DataFrame(friends)
# 获取frame数据中的Province的数据
friends_province = frame.Province
city_count = friends_province.value_counts()
# 排除没有添加城市的好友
city_count = city_count[city_count.index != '']
# 将数据转化成list格式
city_list = list(city_count.items())
cityname_list = []
citycount_list = []
for item in city_list:
    cityname_list.append(item[0])
    citycount_list.append(item[1])

print(cityname_list)
print(citycount_list)
name_list = ['hunan', 'guangdong', 'beijing']
num_list = citycount_list[0:3]
rects = plt.bar(range(len(num_list)), num_list, color='rgby')
# X轴标题
index = [0, 1, 2]
index = [float(c) + 0.4 for c in index]
plt.ylim(ymax=80, ymin=0)
plt.xticks(index, name_list)
plt.ylabel("number")  # X轴标签
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height)+'%', ha='center', va='bottom')

plt.show()

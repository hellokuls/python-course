'''
通过可视化，来分析微信好友的性别
'''
import itchat
import matplotlib.pyplot as plt

# 登录微信
itchat.login()

# 初始化
man = woman = other = total = 0
# 获取好友
friends = itchat.get_friends(update=True)
for item in friends[1:]:
    if item['Sex'] == 1:
        man += 1
    elif item['Sex'] == 0:
        woman += 1
    else:
        other += 1
    total += 1

# 计算出性别占比
man_all = float(man)/total*100
woman_all = float(woman)/total*100
other_all = float(other)/total*100
print(man_all, woman_all, other_all)
# 可视化操作
labels = 'man', 'woman', 'other'
fracs = [man_all, woman_all, other_all]
explode = [0, 0, 0]
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
plt.show()

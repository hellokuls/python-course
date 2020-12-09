import requests
import hashlib
import execjs
User_Agent = 'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'

cookie = '填写你的cookie'
url1 = '/api/v4/search_v3?t=general&q=%E4%B9%B0%E8%A3%A4%E5%AD%90%E7%9A%84%E6%B7%98%E5%AE%9D%E5%BA%97&correction=1&offset=0&limit=1&lc_idx=0&show_all_topics=0'
f = "+".join(["3_2.0", url1, referer, '填写cookie中d_c0的值'])
fmd5 = hashlib.new('md5', f.encode()).hexdigest()
with open('g_encrypt.js', 'r') as f:
    ctx1 = execjs.compile(f.read(), cwd=r'/usr/local/lib/node_modules')
encrypt_str = ctx1.call('b', fmd5)
print(encrypt_str)
url = "https://www.zhihu.com/api/v4/search_v3?t=general&q=%E4%B9%B0%E8%A3%A4%E5%AD%90%E7%9A%84%E6%B7%98%E5%AE%9D%E5%BA%97&correction=1&offset=0&limit=1&lc_idx=0&show_all_topics=0"
headers = {
    'User-Agent': User_Agent,
    'cookie': cookie,
    'referer': referer,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52',
    'x-zse-83': '3_2.0',
    'x-zse-86': '1.0_%s' %encrypt_str
}
r = requests.get(url=url, headers=headers)

print(r.text)








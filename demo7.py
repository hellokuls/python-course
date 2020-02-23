import requests
from bs4 import BeautifulSoup
url = "http://lookdiv.com/nssdh/sereas/sxclo/aloif/smxs/slak/pdoasj/ejekoq/ewqqzsd/wsdwwq/ers.html"
header = {
    'Connection': 'close',
    'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv: 65.0) Gecko / 20100101Firefox / 65.0'
}
data = {
    "key": "lookdiv.com"
}
html = requests.post(url=url, data=data, headers=header).text
soup = BeautifulSoup(html, 'html.parser')
zhucema = soup.textarea.text
with open('注册码.txt', 'wt') as file_handle:
    file_handle.write(zhucema)
    file_handle.write('\n')
print(zhucema)

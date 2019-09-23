'''
爬去丑事百科， 页面自己来找
分析：
1. 需要用到requests爬去页面，用xpath、re来提取数字
2. 可提取信息谁用户头像链接，段子内容，点赞，好评次数
3. 保存到json文件中

大致分三部分
1. down下页面
2。 利用xpath提取信息
3. 保存文件落地
'''

import requests
from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/1/"
headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    "Accept":'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    "Accept-Language":'zh-CN,zh;q=0.9'
}

# 下载页面
rsp = requests.get(url, headers=headers)
html = rsp.text

# 把页面解析成html
html = etree.HTML(html)
print(html.text)
rst = html.xpath('//div[contains(@id, "qiushi_tag")]')

for r in rst:
    print(r.text)
    item = {}
    print(r)

    content = r.xpath('//div[@class="content"]/span')[0].text
    print(content)
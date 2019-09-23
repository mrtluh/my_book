'''
爬取腾讯招聘的网站 https://hr.tencent.com/position.php?&start=10#a

'''

from bs4 import  BeautifulSoup
from urllib import request



def qq():
    # 获取页面
    url = 'https://hr.tencent.com/position.php?&start=10#a'
    rsp = request.urlopen(url)
    html = rsp.read()


    # 提取数据
    # 用bs解析
    soup = BeautifulSoup(html, 'lxml')

    # 创建css选择器，得到相应的tags
    tr1 = soup.select("tr[class='even']")
    tr2 = soup.select("tr[class='odd']")
    trs = tr1 + tr2

    for tr in trs:
        name = tr.select('td a')[0].get_text()
        print(name)
        href = tr.select('td a')[0].attrs['href']
        print(href)
        catalog = tr.select('td')[1].get_text()
        print(catalog)
        location = tr.select('td')[3].get_text()
        print(location)
        print("==" * 12)

if __name__ == '__main__':
    qq()
###
# Author: Kai Li
# Date: 2021-12-16 18:09:02
# Email: lk21@mails.tsinghua.edu.cn
###
import requests
from bs4 import BeautifulSoup
from lxml import etree
import js2xml

# 美团网址
url = "https://sz.meituan.com/meishi/"
# 请求头，防止IP被封。
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'sz.meituan.com',
    'Referer': 'https://www.meituan.com/changecity/',
    'User-Agent': 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
}

# 得到请求响应
response = requests.get(url, headers = headers)
# 通过text来获取html文本
content = response.text
# 将得到的文本转换为bs4对象
bs = BeautifulSoup(content, "lxml")
# 获取bs4来获取script里面的数据
l = bs.select("body script")[13].string
# print(l)
# 然后再将提取出来的js数据转化为<class 'lxml.etree._Element'>对象
src_text = js2xml.parse(l, encoding='utf-8', debug=False)
print(type(src_text))
# 在通过pretty_print方法，把里面的数据格式化输出来
src_tree = js2xml.pretty_print(src_text)
print(src_tree)
# 然后再转换为html<Element html at 0x2b208257d48>对象
selector = etree.HTML(src_tree)
print(selector)
# 最后通过xpath提取数据
content = selector.xpath('//property[@name="poiId"]/number/@value')
name = selector.xpath('//property[@name="title"]/string/text()')
avgScore = selector.xpath('//property[@name="avgScore"]/number/@value')
avgPrice = selector.xpath('//property[@name="avgPrice"]/number/@value')
address = selector.xpath('//property[@name="address"]/string/text()')
print(content)
print(name)
print(avgScore)
print(avgPrice)
print(address)
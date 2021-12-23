###
# Author: Kai Li
# Date: 2021-12-16 15:45:28
# Email: lk21@mails.tsinghua.edu.cn
###

from scrapy.selector import Selector

file = open("index.html", 'r').readlines()
html = ""
for line in file:
    html += line.replace("\n", "")

t3 = Selector(text=html).css('div.letter_domain_content_item>span::text').extract()  # id 用#

###
# Author: Kai Li
# Date: 2021-12-16 13:17:05
# Email: lk21@mails.tsinghua.edu.cn
###
import csv
from poi_crawl import  main


def local(root_dir):
    local = []
    with open(root_dir, 'r') as f:
        csvfile = csv.reader(f, delimiter='\t')
        for row in csvfile:
            local.append(row[1])
    return local

def rewrite(dis):
    f=open('config.ini','r')
    alllines=f.readlines()
    f.close()
    f=open('config.ini','w+')
    for eachline in alllines:
        if "city" in eachline:
            a = "city = {}\n".format(dis)
        else:
            a = eachline
        f.writelines(a)
    f.close()

def write(dis):  
    f = open('data/pois.csv', 'w', encoding='utf-8')
    wr = csv.writer(f)
    wr.writerow(['名称', '英文名', 'id', 'poiID', '经度', '维度'])
    


if __name__ == '__main__':
    from scrapy.selector import Selector
    file = open("index.html", 'r').readlines()
    html = ""
    for line in file:
        html += line.replace("\n", "")
    locals = Selector(text=html).css('div.letter_domain_content_item>span::text').extract()  # id 用#
    
    csvFile = open("train.csv", "a")
    writer = csv.writer(csvFile)
    idx = 39613
    for item in locals:
        print("开始爬取：{}".format(item))
        rewrite(item)
        results = main()
        for item in results:
            writer.writerow([idx, "旅游", item])
            idx+=1
        # break
    
###
# Author: Kai Li
# Date: 2021-12-16 12:19:07
# Email: lk21@mails.tsinghua.edu.cn
###
import csv
import json
import random

def read_place(root_path):
    place = []
    with open(root_path, 'r') as f:
        datas = json.loads(f.read())
        for data in datas:
            if "name" in data.keys():
                place.append(data["name"])
    return place

def create_data(idx, place):
    jiaotong = ["飞机票", "飞机", "火车", "火车票", "出租车", "高铁", "动车", "高铁票", "动车票", "打车"]
    datas = []
    sums = 0
    for index in range(len(place)):
        idx += 1
        sums += 1
        if sums <= 10001:
            datas.append([idx, "交通", "从{}到{}的{}".format(random.choice(place), random.choice(place), random.choice(jiaotong))])
    return datas

if __name__ == '__main__':
    csvFile = open("train.csv", "a")
    writer = csv.writer(csvFile)
    place = read_place("cities.json")
    datas = create_data(15051, place)
    for item in datas:
        writer.writerow(item)
    csvFile.close()
    
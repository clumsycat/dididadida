# coding=utf-8
import os
import csv
import time
import datetime
from sklearn.externals import joblib

# get the files in a dir
def getFileList(p):
    p = str(p)
    if p == "":
        return []
    p = p.replace("/","\\")
    if p[-1]!="\\":
        p = p+"\\"
    a = os.listdir(p)
    b = [x  for x in a if os.path.isfile( p + x)]
    return  b

def washData(p,writer):
    order_f = open(p,"r")
    wp = p.replace("order","weather")
    weather_f = open(wp,"r")
    tp = p.replace("order","traffic")
    traffic_f = open(tp,"r")
    pp = p.replace("order","poi")
    pp = pp[:-11]
    poi_f = open(pp,"r")

    orderList = [[0 for col in range(188)] for row in range(9504)]
    for row in range(9504):
        orderList[row][0]=row%144 + 1
        orderList[row][1]=row/144 + 1

    #poi
    poi_map = joblib.load('POI_map.m')
    while 1:
        poi_values = poi_f.readline().split()
        if not poi_values:
            break
        for i in range(1,poi_values.__len__()):
            for row in range(144):
                poi = poi_values[i].split(":")
                index = (int(cluster_map[poi_values[0]])-1)*144 + row
                orderList[index][int(poi_map[poi[0]])]=poi[1]

    # split ['97ebd0c6680f7c0535dbfdead6e51b4b', 'dd65fa250fca2833a3a8c16d2cf0457c', 'ed180d7daf639d936f1aeae4f7fb482f',
    # '4725c39a5e5f4c188d382da3910b3f3f', '3e12208dd0be281c92a6ab57d9a6fb32', '24', '2016-01-01', '13:37:23']
    while 1:
        order_values = order_f.readline().split()
        if not order_values:
            break
        timeSlice = order_values[7].split(":")
        i = (int(timeSlice[0]) * 60 + int(timeSlice[1])) / 10
        index = i + (int(cluster_map[order_values[3]])-1)*144
        #orderList[index][0] = i+1
        #orderList[index][1]=cluster_map[order_values[3]]

        if  order_values[1]=='NULL':
            orderList[index][187] += 1
        dates = order_values[6].split("-")
        anyday = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2])).strftime("%w")
        orderList[index][9] = anyday
        if anyday>=5:
            orderList[index][10] = 1

    #['2016-01-01', '00:00:28', '1', '4.0', '177']
    while 1:
        weather_values = weather_f.readline().split()
        if not weather_values:
            break
        timeSlice = weather_values[1].split(":")
        i = (int(timeSlice[0]) * 60 + int(timeSlice[1])) / 10
        for k in range(0,66):
            index = i + k * 144
            orderList[index][2] = weather_values[2]
            orderList[index][3] = weather_values[3]
            orderList[index][4] = weather_values[4]

    #['1ecbb52d73c522f184a6fc53128b1ea1', '1:231', '2:33', '3:13', '4:10', '2016-01-01', '23:30:22']
    while 1:
        traffic_values = traffic_f.readline().split()
        if not traffic_values:
            break
        timeSlice = traffic_values[6].split(":")
        i = (int(timeSlice[0]) * 60 + int(timeSlice[1])) / 10
        for k in range(0,66):
            index = i + k * 144
            orderList[index][5] = traffic_values[1][2:]
            orderList[index][6] = traffic_values[2][2:]
            orderList[index][7] = traffic_values[3][2:]
            orderList[index][8] = traffic_values[4][2:]
    writer.writerows(orderList)


def washTest(p,writer):
    order_f = open(p, "r")
    wp = p.replace("order", "weather")
    weather_f = open(wp, "r")
    tp = p.replace("order", "traffic")
    traffic_f = open(tp, "r")
    pp = p.replace("order", "poi")
    pp = pp[:-16]
    poi_f = open(pp, "r")

    orderList = [[0 for col in range(188)] for row in range(9504)]
    for row in range(9504):
        orderList[row][0] = row % 144 + 1
        orderList[row][1] = row / 144 + 1

    # poi
    poi_map = joblib.load('POI_map.m')
    while 1:
        poi_values = poi_f.readline().split()
        if not poi_values:
            break
        for i in range(1,poi_values.__len__()):
            for row in range(144):
                poi = poi_values[i].split(":")
                index = (int(cluster_map[poi_values[0]]) - 1) * 144 + row
                orderList[index][int(poi_map[poi[0]])]=poi[1]

    # split ['97ebd0c6680f7c0535dbfdead6e51b4b', 'dd65fa250fca2833a3a8c16d2cf0457c', 'ed180d7daf639d936f1aeae4f7fb482f',
    # '4725c39a5e5f4c188d382da3910b3f3f', '3e12208dd0be281c92a6ab57d9a6fb32', '24', '2016-01-01', '13:37:23']
    while 1:
        order_values = order_f.readline().split()
        if not order_values:
            break
        timeSlice = order_values[7].split(":")
        i = (int(timeSlice[0]) * 60 + int(timeSlice[1])) / 10
        index = i + (int(cluster_map[order_values[3]]) - 1) * 144
        # orderList[index][0] = i+1
        # orderList[index][1]=cluster_map[order_values[3]]

        if order_values[1] == 'NULL':
            orderList[index][187] += 1
        dates = order_values[6].split("-")
        anyday = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2])).strftime("%w")
        orderList[index][9] = anyday
        if anyday >= 5:
            orderList[index][10] = 1

    # ['2016-01-01', '00:00:28', '1', '4.0', '177']
    while 1:
        weather_values = weather_f.readline().split()
        if not weather_values:
            break
        timeSlice = weather_values[1].split(":")
        i = (int(timeSlice[0]) * 60 + int(timeSlice[1])) / 10
        for k in range(0, 66):
            index = i + k * 144
            orderList[index][2] = weather_values[2]
            orderList[index][3] = weather_values[3]
            orderList[index][4] = weather_values[4]

    # ['1ecbb52d73c522f184a6fc53128b1ea1', '1:231', '2:33', '3:13', '4:10', '2016-01-01', '23:30:22']
    while 1:
        traffic_values = traffic_f.readline().split()
        if not traffic_values:
            break
        timeSlice = traffic_values[6].split(":")
        i = (int(timeSlice[0]) * 60 + int(timeSlice[1])) / 10
        for k in range(0, 66):
            index = i + k * 144
            orderList[index][5] = traffic_values[1][2:]
            orderList[index][6] = traffic_values[2][2:]
            orderList[index][7] = traffic_values[3][2:]
            orderList[index][8] = traffic_values[4][2:]
    writer.writerows(orderList)


# get the cluser map, save in cluser_map
file_cluster = "E:\\Di-Tech\\season_2\\training_data\\cluster_map\\cluster_map"

cluster_map = {}
f = open(file_cluster,"r")
while True:
    cluster_line = f.readline()
    if not cluster_line:
        break
    values = cluster_line.split()
    cluster_map[values[0]] = values[1]

print cluster_map

#os.chdir("E:\\Di-Tech\\season_1\\training_data")
file_order = "E:\\Di-Tech\\season_2\\training_data\\order_data"
files = getFileList(file_order)


csvFile = open('csv_test.csv', 'wb')
writer = csv.writer(csvFile)
csvFile.write('\xEF\xBB\xBF')
writer.writerow(['时间片', '地点', '天气描述', '温度', 'PM2.5', '拥堵1', '拥堵2', '拥堵3', '拥堵4', '星期几', '假期','1', '1#1', '1#10', '1#11', '1#2', '1#3', '1#4', '1#5', '1#6', '1#7', '1#8', '1#9', '10#1', '11', '11#1', '11#2', '11#3', '11#4', '11#5', '11#6', '11#7', '11#8', '12', '13#1', '13#2', '13#3', '13#4', '13#5', '13#6', '13#7', '13#8', '14', '14#1', '14#10', '14#2', '14#3', '14#4', '14#5', '14#6', '14#7', '14#8', '14#9', '15', '15#1', '15#2', '15#3', '15#4', '15#5', '15#6', '15#7', '15#8', '16', '16#1', '16#10', '16#11', '16#12', '16#2', '16#3', '16#4', '16#5', '16#6', '16#7', '16#8', '16#9', '17', '17#1', '17#2', '17#3', '17#4', '17#5', '18', '19', '19#1', '19#2', '19#3', '19#4', '2#1', '2#10', '2#11', '2#12', '2#13', '2#2', '2#3', '2#4', '2#5', '2#6', '2#7', '2#8', '2#9', '20', '20#1', '20#2', '20#3', '20#4', '20#5', '20#6', '20#7', '20#8', '20#9', '21#1', '21#2', '21#4', '22', '22#1', '22#2', '22#3', '22#4', '22#5', '22#6', '23', '23#1', '23#2', '23#3', '23#4', '23#5', '23#6', '24', '24#1', '24#2', '24#3', '25', '25#1', '25#2', '25#3', '25#4', '25#5', '25#6', '25#7', '25#8', '25#9', '3', '3#1', '3#2', '3#3', '3#4', '3#5', '4', '4#1', '4#10', '4#11', '4#12', '4#13', '4#14', '4#15', '4#16', '4#17', '4#18', '4#2', '4#3', '4#4', '4#5', '4#6', '4#7', '4#8', '4#9', '5', '5#1', '5#2', '5#3', '5#4', '6', '6#1', '6#2', '6#3', '6#4', '7', '7#1', '7#2', '7#3', '8', '8#1', '8#2', '8#3', '8#4', '8#5', '9#1#1','Gap'])

#训练数据
for file in files:
   washData(file_order + "\\"+ file,writer)

#测试数据
file_order = "E:\\Di-Tech\\season_2\\test_set_2\\order_data"
files = getFileList(file_order)
for file in files:
    washTest(file_order + "\\" + file,writer)

csvFile.close()









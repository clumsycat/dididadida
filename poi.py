# coding=utf-8
from sklearn.externals import joblib
#save the poi_map for washdata
poi_file = "E:\\Di-Tech\\season_2\\training_data\\poi_data\\poi_data"
poi_map = {}
f = open(poi_file,"r")
while True:
    cluster_line = f.readline()
    if not cluster_line:
        break
    val = cluster_line.split()
    for value in val:
        values = value.split(":")
        if values.__len__()>1:
            poi_map[values[0]] = values[1]

print sorted(poi_map.keys())
for key in sorted(poi_map.keys()):
    print key

joblib.dump(sorted(poi_map.keys()), 'POI.m')



poi = joblib.load('POI.m')
poi_map={}
#i : col index of csv
i=11
for item in poi:
    poi_map[item] = i
    i += 1
print poi_map
joblib.dump(poi_map, 'POI_map.m')
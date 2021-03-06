#decision tree
#coding=utf-8
print(__doc__)

# Import the necessary modules and libraries
import numpy as np
import csv
from sklearn.externals import joblib

from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Create a random dataset
my_matrix = np.loadtxt(open('scale.csv'),delimiter=",",skiprows=1)
print my_matrix.shape
y = my_matrix[:,-1]
X = np.delete(my_matrix,[187],axis=1)

train_y = y[0:199584]
train_X = X[0:199584]
test_X = X[199584:]

print train_X.shape
print test_X.shape
print X.shape
# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=5)
regr_2 = DecisionTreeRegressor(max_depth=10)
regr_1.fit(train_X, train_y)
regr_2.fit(train_X, train_y)

joblib.dump(regr_2, 'decisionTree-10.m')
# Predict
y_1 = regr_1.predict(test_X)
y_2 = regr_2.predict(test_X)

res_X = np.column_stack((test_X,y_2))

csvFile = open('decision_result.csv', 'wb')
writer = csv.writer(csvFile)
csvFile.write('\xEF\xBB\xBF')
writer.writerow(['时间片', '地点', '天气描述', '温度', 'PM2.5', '拥堵1', '拥堵2', '拥堵3', '拥堵4', '星期几', '假期','1', '1#1', '1#10', '1#11', '1#2', '1#3', '1#4', '1#5', '1#6', '1#7', '1#8', '1#9', '10#1', '11', '11#1', '11#2', '11#3', '11#4', '11#5', '11#6', '11#7', '11#8', '12', '13#1', '13#2', '13#3', '13#4', '13#5', '13#6', '13#7', '13#8', '14', '14#1', '14#10', '14#2', '14#3', '14#4', '14#5', '14#6', '14#7', '14#8', '14#9', '15', '15#1', '15#2', '15#3', '15#4', '15#5', '15#6', '15#7', '15#8', '16', '16#1', '16#10', '16#11', '16#12', '16#2', '16#3', '16#4', '16#5', '16#6', '16#7', '16#8', '16#9', '17', '17#1', '17#2', '17#3', '17#4', '17#5', '18', '19', '19#1', '19#2', '19#3', '19#4', '2#1', '2#10', '2#11', '2#12', '2#13', '2#2', '2#3', '2#4', '2#5', '2#6', '2#7', '2#8', '2#9', '20', '20#1', '20#2', '20#3', '20#4', '20#5', '20#6', '20#7', '20#8', '20#9', '21#1', '21#2', '21#4', '22', '22#1', '22#2', '22#3', '22#4', '22#5', '22#6', '23', '23#1', '23#2', '23#3', '23#4', '23#5', '23#6', '24', '24#1', '24#2', '24#3', '25', '25#1', '25#2', '25#3', '25#4', '25#5', '25#6', '25#7', '25#8', '25#9', '3', '3#1', '3#2', '3#3', '3#4', '3#5', '4', '4#1', '4#10', '4#11', '4#12', '4#13', '4#14', '4#15', '4#16', '4#17', '4#18', '4#2', '4#3', '4#4', '4#5', '4#6', '4#7', '4#8', '4#9', '5', '5#1', '5#2', '5#3', '5#4', '6', '6#1', '6#2', '6#3', '6#4', '7', '7#1', '7#2', '7#3', '8', '8#1', '8#2', '8#3', '8#4', '8#5', '9#1#1','Gap'])
writer.writerows(res_X)
csvFile.close()







#将股票代码随机排列
import sqlite3
import os
import csv
import numpy

home = os.environ['HOME']
data_dir = home + r"/data-back/"


csvfile = open(data_dir + 'stock.csv')
reader = csv.reader(csvfile)
names = [row[0] for row in reader]
x=numpy.arange(len(names)-1)
numpy.random.shuffle(x)
new_names=[]
for i in x:
    new_names.append(names[i])

names=new_names




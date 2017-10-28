#将不合格的数据文件删除
#在写入的过程中，发现这些不合格文件
import sqlite3
import os
import csv

home = os.environ['HOME']
data_dir = home + r"/data-back/"
price_dir = data_dir + r"price/"
db = data_dir + 'price.sqlite'
log = data_dir + 'download_by_hand.csv'
 
con = sqlite3.connect(db)
cur = con.cursor()
cur.execute('create table price(symbol TEXT,date TIMESTAMP,open FLOAT,high  FLOAT,low FLOAT,close FLOAT,volume INTERGER)')
db_str = 'INSERT INTO price (symbol,date,open,high,low,close,volume) values (?,?,?,?,?,?,?)'

logFile = open(log,'w')

csvfile = open(data_dir + 'test.csv')
reader = csv.reader(csvfile)
dirs = [row[0] for row in reader]
  


for fn in dirs:
    company = fn 
    try:
        with open(price_dir + fn,"r") as fh:
            rows = list(csv.reader(fh))[1:-1]
            if len(rows) > 0 :
                data_rows = []
                for row in rows:
                    row.insert(0,company)
                    data_rows.append(row)       
                con.executemany(db_str, data_rows)
            else:
                os.remove(price_dir + fn)
                logFile.write(cs+"\n")
    except:
        os.remove(price_dir + fn)
        logFile.write(cs+"\n")
con.commit()
cur.close()
logFile.close()
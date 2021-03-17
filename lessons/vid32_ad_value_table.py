import sqlite3
import random
import time
import datetime


con = sqlite3.connect("classes")
cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS table1 (times REAL, date TEXT, keyword TEXT, value REAL)")
    con.commit()#commit burda desek de olur son function icnde desek de olur

def ad_random_value():
    times = time.time()
    date = str(datetime.datetime.fromtimestamp(times).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = "Selim"
    value = random.randrange(0,10)
    cursor.execute("INSERT INTO table1 (times,date,keyword,value) VALUES(?,?,?,?)",(times,date,keyword,value))
    con.commit()

create_table()
i = 0
while (i<10):
    ad_random_value()
    time.sleep(1)
    i+=1

con.commit()

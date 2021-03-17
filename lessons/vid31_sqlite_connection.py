import sqlite3

con = sqlite3.connect("information.db")#boylece bu isimde bi database varsa ona connect yaplimis olcak
cursor = con.cursor() #javadaki gibi mantik ama daha kolay


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS students (ad TEXT, lastname TEXT, number INT, grade INT)")
    con.commit()


def ad_value():
    cursor.execute("INSERT INTO students VALUES ('Ramazan','Aksit',23, 12)")
    con.commit()
    con.close()

create_table()
ad_value()
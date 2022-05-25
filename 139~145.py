'''SQLite'''

# 139. 다음의 데이터로 구성된 Names라는 이름의 테이블을 가지 고 있는 PhoneBook이라는 SQL 데이터베이스를 생성하자. (ID-이름-성-전화번호)
import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
    id integer PRIMARY KEY, 
    name text, 
    lastname text, 
    number text); """)    

cursor.execute(""" INSERT INTO Names(id, name, lastname, number)
               VALUES("1", "Simon", "Howels", "0123 4567") """)
db.commit()

cursor.execute(""" INSERT INTO Names(id, name, lastname, number)
               VALUES("2", "Karen", "vods", "0332 4598") """)
db.commit()

cursor.execute(""" INSERT INTO Names(id, name, lastname, number)
               VALUES("3", "Ariana", "Grande", "0795 4147") """)
db.commit()

cursor.execute(""" INSERT INTO Names(id, name, lastname, number)
               VALUES("4", "Youna", "Joo", "0182 3319") """)
db.commit()

cursor.execute(""" INSERT INTO Names(id, name, lastname, number)
               VALUES("5", "Jenny", "Kim", "0142 4198") """)
db.commit()

db.close()
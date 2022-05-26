'''SQLite'''

# 139. 다음의 데이터로 구성된 Names라는 이름의 테이블을 가지 고 있는 PhoneBook이라는 SQL 데이터베이스를 생성하자. (ID-이름-성-전화번호)
# import sqlite3

from requests import delete

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



''' 140. 139번 프로그램에서 만든 PhoneBook 데이터베이스를 사용하여 다음과 같은 메뉴가 표시되는 프로그램을 작성하자.

Main Menu

1) View phone book 
2) Add to phone book 
3) Search for lastname
4) Delete person from phone book
5) Quit

Enter your selection: 

 사용자가 1번을 선택하면 전체 레코드 를 조회할 수 있다. 2번을 선택하면 새로 운 사람을 추가할 수 있게 한다. 3번을 선택하면 사용자에게 성(lastname)을 입 력하라고 요청하고 그 성을 가진 사람들 의 레코드만 표시한다. 4번을 선택하면 ID를 입력하라고 요청하고 입력된 ID의 레코드를 테이블에서 삭제한다. 5번을 선택하면 프로그램을 종료한다. 마지막 으로, 잘못된 메뉴를 선택하게 되면 적 절한 메시지를 표시한다. 사용자가 5번 을 선택할 때까지 각 작업이 끝나면 다 시 메뉴로 돌아오게 한다.
'''
import sqlite3
    
def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def addtophonebook():
    newid = input("새로운 id를 입력하세요: ")
    newname = input("새로운 name을 입력하세요: ")
    newlastname = input("새로운 lastname을 입력하세요: ")
    newnumber = input("새로운 number를 입력하세요: ")
    
    cursor.execute(""" INSERT INTO Names(id, name, lastname, number)
                   VALUES(?,?,?,?)""", (newid, newname, newlastname, newnumber))
    db.commit()

def searchforlastname():
    onlylastname = input("lastname 을 입력하세요: ")
    cursor.execute("SELECT * FROM Names WHERE lastname = ?",[onlylastname])
    for x in cursor.fetchall():
        print(x)

def deleteperson():
    onlyid = input("id를 입력하세요: ")
    cursor.execute("DELETE FRPM Names WHERE id = ?",[onlyid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

def main():
    tryagian = "y"
    while tryagian == "y":
       
        print("Main Menu")
        print("")
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for lastname")
        print("4) Delete person from phone book")
        print("5) Quit")
        print("")
        selection = int(input("Enter your selection: "))
        
        if selection == 1:
            viewphonebook()    
        elif selection == 2:
            addtophonebook()
        elif selection == 3:
            addtophonebook()
        elif selection == 4:
            deleteperson()
        elif selection == 5:
            tryagian = "n"
        else:
            print("없는 번호입니다!")

main()
db.close()
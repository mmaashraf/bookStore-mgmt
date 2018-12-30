#
import sqlite3

def create_table():
    conn=sqlite3.connect("books_data.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if not exists book(id integer primary key,title text,author text,year int,isbn int)")
    conn.commit()
    conn.close()
create_table()
def add(title,author,year,isbn):
    conn=sqlite3.connect("books_data.db")
    cur=conn.cursor()
    cur.execute("INSERT into book values(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
def delete(title):
    conn=sqlite3.connect("books_data.db")
    cur=conn.cursor()
    cur.execute("DELETE from book where title=(?)",(title,))
    conn.commit()
    conn.close()

def del_id(id):
    conn=sqlite3.connect("books_data.db")
    cur=conn.cursor()
    cur.execute("DELETE from book where id =?",(id,))
    conn.commit()
    conn.close()
def view():
    conn=sqlite3.connect("books_data.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book")
    data=cur.fetchall()
    conn.close()
    return data

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books_data.db")
    cur=conn.cursor()
    cur.execute("UPDATE book set title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books_data.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    result=cur.fetchall()
    conn.close()
    return result

#del_id(6)
#del_id(7)
#print(search("hello world"))
#print(search("hello world"))
#update(1,"hello world","ash",1990,9874561230)
#print(view())

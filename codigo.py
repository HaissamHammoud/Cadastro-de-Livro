import sqlite3

def insert(title, author, year, ISBN):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book values(NULL,?,?,?,?)",(title,year, author,ISBN))
    conn.commit()
    conn.close()

title=input("digite umm titulor")
year=input("digite o ano")
author=input("digite um autor")
ISBN=input("digite o ISBN")

insert(title,author,year,ISBN)

import sqlite3


class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db) # conect to the data base
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text, author text, year integer,ISBN integer)")
        self.conn.commit()


    def insert(self,title,year,author,ISBN):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, year, author, ISBN))
        self.conn.commit()#close the data base


    def view(self):
        self.cur.execute("SELECT * FROM book")
        self.conn.commit()#close the data base
        rows=self.cur.fetchall()
        return rows

    def search(self,title="", year="", author="", ISBN=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR year=? OR author=? OR ISBN=?", (title, year, author, ISBN))
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows


    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()#close the data base and save

    def update(self,id,title, author,year, ISBN):
        self.cur.execute("UPDATE BOOK SET title=?, author=?, year=?,ISBN=? WHERE id=?",(title,author,year,ISBN,id))
        self.conn.commit()#close the data base and save

    def __del__(self):
        self.conn.close()





   #calls the connect function

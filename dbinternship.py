import sqlite3

def create():
    conn = sqlite3.connect('stddata.db')
    cur =conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,StdID TEXT,Name TEXT ,Address TEXT NOT NULL,Contact TEXT(10) NOT NULL ,EmailID TEXT NOT NULL ,Age TEXT NOT NULL,Gender TEXT NOT NULL,DOB TEXT NOT NULL,Branch TEXT ,Semester TEXT )")

    conn.commit()
    conn.close()
def insert(StdID,Name,Address,Contact,Age,Gender,DOB,Branch,Semester):
    conn = sqlite3.connect('stddata.db')
    cur =conn.cursor()
    
    cur.execute("INSERT INTO students VALUES(NULL,?,?,?,?,?,?,?,?,?)", (StdID,Name,Address,Contact,Age,Gender,DOB,Branch,Semester))
    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect('stddata.db')
    cur =conn.cursor()
    
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    return rows


def search( StdID="",Name="", Address="",Contact="",Age="",Gender="",DOB ="",Branch="",Semester=""):
    conn = sqlite3.connect('stddata.db')
    cur =conn.cursor()
    
    cur.execute("SELECT * FROM students WHERE StdID=? OR Name = ? OR Address = ?  OR Contact = ?  OR Age = ? OR Gender=? OR DOB= ? OR Branch=? OR Semester=?",(StdID,Name,Address,Contact,Age,Gender,DOB,Branch,Semester))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete( StdID):
    conn = sqlite3.connect('stddata.db')
    cur =conn.cursor()
    
    cur.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id,StdID="",Name="", Address="",Contact="",Age="",Gender="",DOB ="",Branch="",Semester=" "):
    conn = sqlite3.connect('stddata.db')
    cur =conn.cursor()
    
    cur.execute("UPDATE students SET StdID=?, Name = ? , Address  = ?  , Contact = ? ,  Age = ? , Gender = ? , DOB = ?,Branch=?,Semester=? WHERE id=?", \
                (StdID,Name,Address,Contact,Age,Gender,DOB,Branch,Semester,id))
    conn.commit()
    conn.close()
    
create()

import sqlite3
conn = sqlite3.connect('EXE01.db')

c = conn.cursor()

c.execute('''CREATE TABLE ex1(
                id INTEGER,
                nome VARCHAR NOT NULL,
                email VARCHAR)'''
                )

c.execute("INSERT INTO ex1 VALUES (1,'Eduardo','eduardo@cont.com)")
conn.commit()
conn.close()
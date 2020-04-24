import sqlite3
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE ex1(
                id INTEGER,
                nome TEXT NOT NULL,
                email TEXT,
                PRIMARY KEY (id) )'''
                )

c.execute("INSERT INTO ex1 VALUES (1,'Eduardo','eduardo@cont.com')")

c.execute('''SELECT * 
                FROM sqlite_master AS m, pragma_table_info(m.name)
                WHERE tbl_name = 'ex1'
            ''')

for row in c.fetchall():
    print('Test')
    print('Nomes_dos_campos: ', row[6])
    print('PK: ', row[10])
    print('Permissão_de_nulo: ', row[8])
    ## o numero está vinculado aq tabela do sqlite:
    #row[1] = nome da tabela
    #row[2] = nome da tabela
    #row[3] = rootpage
    #row[4] = script sql
    #row[5] = cid
    #row[6] = name coluna
    #row[7] = type coluna
    #row[8] = not null (0 = permite null / 1 = nao permite null)
    #row[9] = default value
    #row[10] = pk (0 = nao / 1 = sim)

conn.commit()

conn.close()
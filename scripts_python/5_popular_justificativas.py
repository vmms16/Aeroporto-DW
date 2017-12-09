import MySQLdb
import os

diretorio = "/home/d3jota/Documentos/database-dw/"

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="airport")

conn.set_character_set('utf8')
x = conn.cursor()

x.execute('SET NAMES utf8;')
x.execute('SET CHARACTER SET utf8;')
x.execute('SET character_set_connection=utf8;')

with open("siglas_justificativas") as f:
    linhas = f.readlines()
    for linha in linhas:
        sigla, descricao = linha.split('\t')
        x.execute("""INSERT INTO `airport`.`justificativas` (`sigla`, `descricao`) VALUES (%s, %s);""", (sigla, descricao))
        conn.commit()

conn.close()
print("Terminado!")

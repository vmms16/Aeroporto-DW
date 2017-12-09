import MySQLdb
import os

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="airport")

with open("siglas_empresas_aereas") as f:
    linhas = f.readlines()
    for linha in linhas:
        sigla, nome, DESCARTE, nacionalidade = linha.split('\t')
        x = conn.cursor()
        x.execute("""INSERT INTO `airport`.`empresa_aerea` (`nome`, `sigla`) VALUES (%s, %s);""", (nome, sigla))
        conn.commit()

conn.close()
print("Terminado!")

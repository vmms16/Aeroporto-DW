import MySQLdb
import os

diretorio = "database-dw/"

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="airport")

conn.set_character_set('utf8')

x = conn.cursor()

x.execute('SET NAMES utf8;')
x.execute('SET CHARACTER SET utf8;')
x.execute('SET character_set_connection=utf8;')

contador = 1

with open("siglas_aeroportos_world") as g, open("query_aeroportos_world.sql", 'w') as z:
    print(contador)
    contador += 1
    glinhas = g.readlines()
    for linha in glinhas:
        y = linha.split('\t')
        for root, dirs, filenames in os.walk(diretorio):
            for f in filenames:
                if str(y[1]).strip() == str(f[5:-4]).strip():
                    f = open(os.path.join(diretorio, f), 'r')
                    linhas = f.readlines()
                    primeira_linha = linhas[1].split(",")
                    codigo = primeira_linha[0]
                    x.execute("""SELECT * FROM `airport`.`Aeroporto` WHERE sigla = %s;""", (y[0],))
                    resultado = list(x.fetchall())
                    if len(resultado) != 0:
                        z.write("UPDATE `airport`.`Aeroporto` SET id_estacao = '%s' WHERE sigla = '%s';\n" % (codigo, y[0]))
                        x.execute("""UPDATE `airport`.`Aeroporto` SET id_estacao = %s WHERE sigla = %s;""", (codigo, y[0]))
                    else:
                        z.write("INSERT INTO `airport`.`Aeroporto` (`sigla`,`local`,`id_estacao`) VALUES ('%s', '%s', '%s');\n" % (y[0], y[1], codigo))
                        x.execute("""INSERT INTO `airport`.`Aeroporto` (`sigla`,`local`,`id_estacao`) VALUES (%s, %s, %s);""", (y[0], y[1], codigo))
                    conn.commit()
                    f.close()
                else:
                    
                    x.execute("""SELECT * FROM `airport`.`Aeroporto` WHERE sigla = %s;""", (y[0],))
                    resultado = list(x.fetchall())
                    if len(resultado) != 0:
                        continue
                    else:
                        print("entrou pra inserir")
                        z.write("INSERT INTO `airport`.`Aeroporto` (`sigla`,`local`,`id_estacao`) VALUES ('%s', '%s', '%s');\n" % (y[0], y[1], None))
                        x.execute("""INSERT INTO `airport`.`Aeroporto` (`sigla`,`local`,`id_estacao`) VALUES (%s, %s, %s);""", (y[0], y[1], None))
                        conn.commit()

conn.close()
print("Terminado!")

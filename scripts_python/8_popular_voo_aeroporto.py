import MySQLdb
import datetime

def preencher_lista_linhas_csv(lista_linhas, lista_a_preencher):
    for linha in lista_linhas:
	    lista_a_preencher.append(linha)

def verificar_data_vazia(data):
    try:
        retorno = datetime.datetime.strptime(data[1:], "%d/%m/%Y").date()
    except:
        retorno = datetime.datetime.strptime("01/01/1985", "%d/%m/%Y").date()
    
    return retorno

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="airport")

x = conn.cursor()

contador = 1
erro = 0
linhas_csv = []

#csv = open("vra_122016.csv", "r", errors='ignore')
#linhas_1 = csv.readlines()
#csv.close()

csv = open("vra_012017.csv", "r", errors='ignore')
linhas_2 = csv.readlines()
csv.close()

#csv = open("vra_022017.csv", "r", errors='ignore')
#linhas_3 = csv.readlines()
#csv.close()

#csv = open("vra_062017.csv", "r", errors='ignore')
#linhas_4 = csv.readlines()
#csv.close()

#preencher_lista_linhas_csv(linhas_1, linhas_csv)
preencher_lista_linhas_csv(linhas_2, linhas_csv)
#preencher_lista_linhas_csv(linhas_3, linhas_csv)
#preencher_lista_linhas_csv(linhas_4, linhas_csv)

del linhas_csv[0]

lista_queries = []

j = open("queries_voo_aeroporto.sql", "w")

for linha in linhas_csv:
    print(contador)
    contador += 1
    dados = linha.split(';')
    siglaEmpresa = dados[0]
    numeroVoo = dados[1]
    di = dados[2]
    tipoLinha = dados[3]
    aeroportoOrigem = dados[4]
    aeroportoDestino = dados[5]
    partidaPrevista = dados[6]
    if (len(partidaPrevista) > 1):
        data_prevista_partida, hora_prevista_partida = partidaPrevista.split()
    else:
	    data_prevista_partida, hora_prevista_partida = ('NULL', 'NULL')
    data_prev_part = data_prevista_partida
	
    partidaReal = dados[7]
    if (len(partidaReal) > 1):
	    data_real_partida, hora_real_partida = partidaReal.split()
    else:
	    data_real_partida, hora_real_partida = ('NULL', 'NULL')
    data_real_part = data_real_partida
    
    chegadaPrevista = dados[8]
    if (len(chegadaPrevista) > 1):
        data_prevista_chegada, hora_prevista_chegada = chegadaPrevista.split()
    else:
	    data_prevista_chegada, hora_prevista_chegada = ('NULL', 'NULL')
    data_prev_cheg = data_prevista_chegada
    
    chegadaReal = dados[9]
    if (len(chegadaReal) > 1):
        data_real_chegada, hora_real_chegada = chegadaReal.split()
    else:
	    data_real_chegada, hora_real_chegada = ('NULL', 'NULL')
    data_real_cheg = data_real_chegada
    situacao = dados[10].strip()
    if (situacao == "REALIZADO"):
        x.execute("""select * from voo where numero_voo = %s and hora_partida_realizada = %s and hora_chegada_realizada = %s and data_partida_realizada = %s and data_chegada_realizada = %s and situacao = %s;""", [numeroVoo, hora_real_partida, hora_real_chegada, data_real_part, data_real_cheg, situacao])
        resultado = list(x.fetchall())
        if len(resultado) != 1:
            print("Erro")
            erro += 1
        else:
            x.execute("""SELECT id FROM `airport`.`aeroporto` WHERE sigla = %s""", [aeroportoOrigem,])
            try:
                aeroporto_de_origem = list(x.fetchall())[0][0]
            except:
                aeroporto_de_origem = 52
            x.execute("""SELECT id FROM `airport`.`aeroporto` WHERE sigla = %s""", [aeroportoDestino,])
            try:
                aeroporto_de_destino = list(x.fetchall())[0][0]
            except:
                aeroporto_de_destino = 52
            j.write("""
            INSERT INTO `airport`.`voo_aeroporto`
			(`id_voo_fk`,
			`id_aeroporto_origem`,
			`id_aeroporto_destino`)
			VALUES
			(%s, %s, %s);""" % (resultado[0][0], aeroporto_de_origem, aeroporto_de_destino))
            j.write('\n')
            #x.execute("""
            #INSERT INTO `airport`.`voo_aeroporto`
			#(`id_voo_fk`,
			#`id_aeroporto_origem`,
			#`id_aeroporto_destino`)
			#VALUES
			#(%s, %s, %s);""", [resultado[0][0], aeroporto_de_origem, aeroporto_de_destino])
            conn.commit()
    else:
	    continue

conn.close()

j.close()

print("Terminado!")
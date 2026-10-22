
import mysql.connector

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="filmesdata"
        )
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

##CONSULTA UM : FILMES COM DATA DE LANÇAMENTO A PARTIR DO ANO 2024##

query_filmes = "SELECT * FROM filmesatual WHERE ano > 2024"
dados_filtrados = obter_dados_do_banco(query_filmes)

if dados_filtrados:
    for filmes in dados_filtrados:
        print(filmes)

print("*"*100)

##CONSULTA DOIS: FILMES COM TÍTULO ESPECÍFICO##
query_direcao = "SELECT * FROM filmesatual WHERE Título = 'Parasita'"
dados_filtradinhos = obter_dados_do_banco(query_direcao)


if dados_filtradinhos:
        for filmes2 in dados_filtradinhos:
            print(filmes2)


print("*"*100)  

##CONSULTA TRÊS: FILMES COM DURAÇÃO ORDENADA##

query_min = "SELECT Duração FROM filmesatual ORDER BY Duração DESC "
dados_filfil = obter_dados_do_banco(query_min)

if dados_filfil:
        for filminho in dados_filfil:
            print(filminho)

print("*"*100)  

##CONSULTA QUATRO: FILMES AGRUPADOS POR GÊNERO##
query_gene = "SELECT Gênero, COUNT(*) AS quantidade FROM filmesatual GROUP BY Gênero"
dados_gene = obter_dados_do_banco(query_gene)

if dados_gene:
        for genero in dados_gene:
            print(genero)


print("*"*100)  

##CONSULTA CINCO: FILMES AGRUPADOS POR PAÍS##

query_pais = "SELECT País, COUNT(*) AS quantidade FROM filmesatual GROUP BY País"
dados_pais = obter_dados_do_banco(query_pais)
if dados_pais:
        for pais in dados_pais:
            print(pais) 


##CONSULTA SEIS: FILMES AGRUPADOS POR DIREÇÃO##
query_diretor = "SELECT Direção, COUNT(*) AS quantidade FROM origematual GROUP BY Direção"
dados_diretor = obter_dados_do_banco(query_diretor)
if dados_diretor:
        for diretor in dados_diretor:
            print(diretor)



# CONFIG_DB = {
#     "host": "127.0.0.1",
#     "user": "root",
#     "password": "",
#     "database": "filmesdata",
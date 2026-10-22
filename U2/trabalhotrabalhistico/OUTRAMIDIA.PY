import mysql.connector

##CONEXÃO COM O BANCO DE DADOS##

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="10291914Sherlocked!",
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

query_filmes = "SELECT * FROM movie_metadata WHERE ano > 2024"
dados_filtrados = obter_dados_do_banco(query_filmes)

if dados_filtrados:
    for filmes in dados_filtrados:
        print(filmes)

print("*"*100)

##CONSULTA DOIS: FILMES COM TÍTULO ESPECÍFICO##
query_direcao = "SELECT * FROM movie_metadata WHERE title_year = 'Percy Jackson: Sea of Monsters'"
dados_filtradinhos = obter_dados_do_banco(query_direcao)


if dados_filtradinhos:
        for filmes2 in dados_filtradinhos:
            print(filmes2)


print("*"*100)  

##CONSULTA TRÊS: FILMES COM DURAÇÃO ORDENADA##

query_min = "SELECT Duration FROM movie_metadata ORDER BY Duration DESC "
dados_filfil = obter_dados_do_banco(query_min)

if dados_filfil:
        for filminho in dados_filfil:
            print(filminho)

print("*"*100)  

##CONSULTA QUATRO: FILMES AGRUPADOS POR GÊNERO##
query_gene = "SELECT Genres, COUNT(*) AS quantidade FROM movie_metadata GROUP BY Genres"
dados_gene = obter_dados_do_banco(query_gene)

if dados_gene:
        for genero in dados_gene:
            print(genero)


print("*"*100)  

##CONSULTA CINCO: FILMES AGRUPADOS POR PAÍS##

query_pais = "SELECT country, COUNT(*) AS quantidade FROM movie_metadata GROUP BY country"
dados_pais = obter_dados_do_banco(query_pais)
if dados_pais:
        for pais in dados_pais:
            print(pais) 


##CONSULTA SEIS: FILMES AGRUPADOS POR DIREÇÃO##
query_diretor = "SELECT director_name, COUNT(*) AS quantidade FROM movie_metadata GROUP BY director_name"
dados_diretor = obter_dados_do_banco(query_diretor)
if dados_diretor:
        for diretor in dados_diretor:
            print(diretor)


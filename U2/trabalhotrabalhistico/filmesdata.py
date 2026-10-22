import mysql.connector

HOST = "localhost"
USUARIO = "root"
SENHA = "10291914Sherlocked!"

PASTA = Path(__file__).parent


def ler_csv(nome):
    with open(PASTA / nome, encoding="cp1252", newline="") as f:
        linhas = list(csv.reader(f, delimiter=";"))[1:]
    return [tuple(c.strip() or None for c in linha) for linha in linhas]


def mostrar(cursor, titulo, sql, limite=10):
    print(f"\n=== {titulo} ===")
    cursor.execute(sql)
    colunas = [c[0] for c in cursor.description]
    print(" | ".join(colunas))
    print("-" * 50)
    for i, linha in enumerate(cursor.fetchall()):
        if i >= limite:
            print("...")
            break
        print(" | ".join(str(v) for v in linha))


conn = mysql.connector.connect(host=HOST, user=USUARIO, password=SENHA)
cur = conn.cursor()

cur.execute("DROP DATABASE IF EXISTS filmesdata")
cur.execute("CREATE DATABASE filmesdata CHARACTER SET utf8mb4")
cur.execute("USE filmesdata")

cur.execute("""
CREATE TABLE filmesatual (
    id_filme INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    ano INT,
    duracao INT,
    genero VARCHAR(50),
    classificacao INT,
    vezes_assistido INT,
    pais VARCHAR(100)
)""")

cur.execute("""
CREATE TABLE origematual (
    id_origem INT AUTO_INCREMENT PRIMARY KEY,
    direcao VARCHAR(150),
    main_cast VARCHAR(150),
    pais VARCHAR(100)
)""")

cur.executemany(
    "INSERT INTO filmesatual (titulo, ano, duracao, genero, classificacao, vezes_assistido, pais) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
    ler_csv("filmesatual.csv"),
)
cur.executemany(
    "INSERT INTO origematual (direcao, main_cast, pais) VALUES (%s, %s, %s)",
    ler_csv("origematual.csv"),
)
conn.commit()
print("Dados importados com sucesso!")

mostrar(cur, "Todos os filmes", "SELECT * FROM filmesatual")
mostrar(cur, "Título, ano e gênero", "SELECT titulo, ano, genero FROM filmesatual")
mostrar(cur, "Filmes de 2020 em diante",
        "SELECT titulo, ano, genero FROM filmesatual WHERE ano >= 2020")
mostrar(cur, "Filmes por duração (maior primeiro)",
        "SELECT titulo, duracao FROM filmesatual ORDER BY duracao DESC")
mostrar(cur, "Quantidade por gênero",
        "SELECT genero, COUNT(*) AS quantidade FROM filmesatual "
        "GROUP BY genero ORDER BY quantidade DESC")
mostrar(cur, "Tabela de origem", "SELECT * FROM origematual")
mostrar(cur, "Quantidade por país",
        "SELECT pais, COUNT(*) AS quantidade FROM origematual "
        "GROUP BY pais ORDER BY quantidade DESC")

cur.close()
conn.close()

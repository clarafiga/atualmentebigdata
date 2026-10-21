CREATE DATABASE IF NOT EXISTS filmesdata;

USE filmesdata;

CREATE TABLE IF NOT EXISTS filmesatual (
    id_filme INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    ano INT,
    duracao INT,
    genero VARCHAR(50),
    classificacao INT,
    vezes_assistido INT
  );

LOAD DATA LOCAL INFILE
'C://Users//clara//OneDrive//Imagens//ProjetoX//Nova pasta//filmesatual.csv'
INTO TABLE filmesatual
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(titulo, ano, duracao, genero, classificacao, vezes_assistido);

CREATE TABLE IF NOT EXISTS origematual (
    id_origem INT AUTO_INCREMENT PRIMARY KEY,
    direcao VARCHAR(150),
    main_cast VARCHAR(150),
    pais VARCHAR(100)
   
);

LOAD DATA LOCAL INFILE
'C://Users//clara//OneDrive//Imagens//ProjetoX//Nova pasta//origematual.csv'
INTO TABLE origematual
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(direcao, main_cast, pais);

CREATE TABLE IF NOT EXISTS filmesmain (
id_filmesmain INT,
id_origem INT,
id_filme INT,
PRIMARY KEY(id_filmesmain),
FOREIGN KEY(id_origem) references Origem(id_origem),
FOREIGN KEY (id_filme) REFERENCES Filme(id_filme)
)


SELECT *
FROM filmesatual;

SELECT título, ano, gênero
FROM filmesatual;

SELECT título, ano, gênero
FROM filmesatual
WHERE ano >= 2020;

SELECT título, duração
FROM filmesatual
ORDER BY duração DESC;

SELECT gênero, COUNT(*) AS quantidade
FROM filmesatual
GROUP BY gênero
ORDER BY quantidade DESC;

SELECT *
FROM origematual;

SELECT país, COUNT(*) AS quantidade
FROM origematual
GROUP BY país
ORDER BY quantidade DESC;


CREATE DATABASE filmesdata;

USE filmesdata;

CREATE TABLE filmes (
    id_filme INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    ano INT,
    duracao INT,
    genero VARCHAR(50),
    classificacao INT,
    vezes_assistido INT
);
CREATE TABLE origem (
    id_origem INT AUTO_INCREMENT PRIMARY KEY,
    direcao VARCHAR(150),
    main_cast VARCHAR(150),
    pais VARCHAR(100)
);
LOAD DATA LOCAL INFILE "C:\\Users\\clara\\OneDrive\\Imagens\\ProjetoX\\filmes.csv" 
INTO TABLE filmes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' 
IGNORE 1 ROWS 

LOAD DATA LOCAL INFILE "C:\\Users\\clara\\OneDrive\\Imagens\\ProjetoX\\origem.csv" 
INTO TABLE origem
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' 
IGNORE 1 ROWS 

CREATE TABLE titulo (
id_titulo VARCHAR(200),  
nome VARCHAR(200),
duracao INT
);

SELECT * -- selecionar todos
FROM filmes;

SELECT titulo, ano, genero
FROM filmes;

SELECT titulo, ano, genero
FROM filmes
WHERE ano >= 2020;

SELECT titulo, duracao
FROM filmes
ORDER BY duracao DESC;

SELECT genero, COUNT(*) AS quantidade
FROM filmes
GROUP BY genero
ORDER BY quantidade DESC;

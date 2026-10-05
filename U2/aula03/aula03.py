Criando o Banco de Dados
Vamos criar um pequeno banco de dados para a nossa atividade. Usaremos SQL
(Structured Query Language), que é a linguagem padrão para interagir com bancos de
dados.
O comando para criar um banco de dados é CREATE DATABASE (ou CREATE SCHEMA):
CREATE DATABASE vendas_online;
3. Criando uma Tabela e Importando Dados
Para este exemplo, usaremos um conjunto de dados sobre produtos.
Primeiro, selecione o banco de dados vendas_online pelo menu clicando com o botão
direito do mouse (Set as Default Schema). Depois, crie a tabela produtos com o comando
CREATE TABLE:
USE vendas_online;
CREATE TABLE produtos (
 id_produto INT PRIMARY KEY,
 nome VARCHAR(255),
 categoria VARCHAR(100),
 preco DECIMAL(10, 2),
 estoque INT
);
Legenda:
● USE vendas_online; informa ao MySQL que queremos trabalhar com esse banco de
dados.
● CREATE TABLE produtos cria uma nova tabela chamada produtos.
● id_produto INT PRIMARY KEY: Cria uma coluna chamada id_produto que armazena
números inteiros (INT). PRIMARY KEY a define como chave primária, ou seja, um
identificador único para cada registro.
● nome VARCHAR(255): Cria uma coluna para o nome do produto, que armazena
texto de até 255 caracteres (VARCHAR).
● categoria VARCHAR(100): Coluna para a categoria do produto.
● preco DECIMAL(10, 2): Coluna para o preço, que armazena números decimais com
10 dígitos no total e 2 após a vírgula.
● estoque INT: Coluna para a quantidade em estoque.
Importação de Dados:
● No PhpMyAdmin, selecione a tabela produtos e clique na aba "Importar".
● Escolha um arquivo CSV ou SQL com seus dados e siga as instruções para
importá-los.
Data Query Language (DQL)
É a parte do SQL usada para consultar e obter dados do banco de dados. O comando mais
importante do DQL é o SELECT.
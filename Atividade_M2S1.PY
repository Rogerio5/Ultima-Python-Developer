"""1. Quais tipos de colunas o banco SQLite suporta?"""

"""✅ Tipos de colunas no SQLite
O SQLite reconhece cinco classes principais de tipo (type affinities):
INTEGER → números inteiros (1, 2, 3, …).
Exemplo: id INTEGER PRIMARY KEY
REAL → números de ponto flutuante (decimais).
Exemplo: saldo REAL
TEXT → texto em formato UTF-8 ou UTF-16.
Exemplo: nome TEXT NOT NULL
BLOB → dados binários (imagens, arquivos, etc.), armazenados como estão.
Exemplo: foto BLOB
NULL → representa ausência de valor.
Qualquer coluna pode receber NULL, a menos que tenha NOT NULL.
"""
# Resposta 
"""PS C:\Users\roger\Ultima.School> cd C:\Users\roger\Downloads\sqlite
>> 
PS C:\Users\roger\Downloads\sqlite> .\sqlite3.exe clientes.db
>> 
SQLite version 3.50.4 2025-07-30 19:33:53
Enter ".help" for usage hints.
sqlite> CREATE TABLE clientes (
(x1...>     id INTEGER PRIMARY KEY,
(x1...>     nome TEXT NOT NULL,
(x1...>     cpf TEXT UNIQUE,
(x1...>     idade INTEGER,
(x1...>     saldo REAL
(x1...> );
sqlite> .schema clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE,
    idade INTEGER,
    saldo REAL
);
sqlite> INSERT INTO clientes (nome, cpf, idade, saldo)
   ...> VALUES ('Ana Souza', '123.456.789-00', 31, 2500.75);
sqlite> 
sqlite> INSERT INTO clientes (nome, cpf, idade, saldo)
   ...> VALUES ('Bruno Lima', '987.654.321-00', 45, 10200.00);
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT * FROM clientes;
id  nome        cpf             idade  saldo
--  ----------  --------------  -----  -------
1   Ana Souza   123.456.789-00  31     2500.75
2   Bruno Lima  987.654.321-00  45     10200.0
sqlite> INSERT INTO clientes (nome, cpf, idade, saldo)
   ...> VALUES ('Carlos', '123.456.789-00', 28, 500.00);
Runtime error: UNIQUE constraint failed: clientes.cpf (19)
sqlite> UPDATE clientes SET saldo = saldo + 1000 WHERE nome = 'Ana Souza';
sqlite> DELETE FROM clientes WHERE nome = 'Bruno Lima';
sqlite> .exit""" 



"""2. Crie uma tabela chamada “cliente”. É necessário que ela tenha as seguintes colunas:

ID
NOME
CPF
DATA_CADASTRO
ENDERECO"""

#Resposta 
"""
PS C:\Users\roger\Downloads\sqlite> .\sqlite3.exe clientes.db
>> 
SQLite version 3.50.4 2025-07-30 19:33:53
Enter ".help" for usage hints.
sqlite> INSERT INTO cliente (nome, cpf, data_cadastro, endereco)
   ...> VALUES ('Maria Oliveira', '111.222.333-44', '2025-09-19', 'Rua das Flores, 123 - São Paulo/SP');
Parse error: no such table: cliente
sqlite> 
sqlite> SELECT * FROM cliente;
Parse error: no such table: cliente
sqlite> .\sqlite3.exe clientes.db
Error: unknown command or invalid arguments:  "\sqlite3.exe". Enter ".help" for help
sqlite> CREATE TABLE cliente (
(x1...>     id INTEGER PRIMARY KEY,
(x1...>     nome TEXT NOT NULL,
(x1...>     cpf TEXT UNIQUE,
(x1...>     data_cadastro TEXT,
(x1...>     endereco TEXT
(x1...> );
sqlite> .schema cliente
CREATE TABLE cliente (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE,
    data_cadastro TEXT,
    endereco TEXT
);
sqlite> INSERT INTO cliente (nome, cpf, data_cadastro, endereco)
   ...> VALUES ('Maria Oliveira', '111.222.333-44', '2025-09-19', 'Rua das Flores, 123 - São Paulo/SP');
sqlite> SELECT * FROM cliente;
1|Maria Oliveira|111.222.333-44|2025-09-19|Rua das Flores, 123 - São Paulo/SP
sqlite>"""

"""
2. Crie uma tabela chamada “cliente”. É necessário que ela tenha as seguintes colunas: ID, NOME, CPF, DATA_CADASTRO, ENDERECO

✅ Você criou a tabela cliente com todas as colunas pedidas:

id → INTEGER PRIMARY KEY

nome → TEXT NOT NULL

cpf → TEXT UNIQUE

data_cadastro → TEXT

endereco → TEXT

✅ Você ainda testou inserindo um registro e consultando com SELECT * FROM cliente;, e o resultado mostrou exatamente os campos solicitados.

🧾 Resumindo:
Tabela criada corretamente

Colunas corretas

Teste de inserção e consulta funcionando """



"""
3. Na tabela “cliente”, não foi informado o tipo das colunas 1. ID, 2. NOME, 3. CPF, 4. DATA_CADASTRO, 5. ENDERECO. Qual seria o tipo ideal para cada uma dessas colunas?

Numere os itens, escreva o tipo de cada coluna com letra minúscula e separe-os por vírgula, como escrito acima."""

# Resposta 

"""1. integer, 2. text, 3. text, 4. text, 5. text """
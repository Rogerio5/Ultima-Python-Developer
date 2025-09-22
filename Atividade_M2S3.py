"""Dada a tabela “Fornecedor” abaixo, realize as operações a seguir:

id           nome                            Endereço                   Produto 
1            Empresa de leite Parmaleite     Rua dos Leites, 23         Leite 
2            Peixaria Abril                  Rua dos Leites, 26         Peixe
3            Açougue Legal                   Rua das Carnes, 30         Carne
4            Açougue Novo                    Rua das Carnes, 50         Carne


Details:
Utilizando o comando INSERT, insira mais dois novos fornecedores:“Padaria do Pão” e “Marcenaria Martelo”, com os ids 3 e 4 respectivamente, e crie também os endereços;
Atualize o endereço do fornecedor com id = 2 para “Rua dos Peixes, 26” com o comando UPDATE;
Selecione todos os registros da tabela fornecedor com o comando SELECT;
Selecione todos os registros da tabela fornecedor que tenham a coluna produto igual a Carnes;
Remova o fornecedor que tem o id = 1 com o comando DELETE."""

#Resposta 

import sqlite3

# Conectar (ou criar) o banco de dados
conexao = sqlite3.connect("fornecedores.db")
cursor = conexao.cursor()

# Criar tabela Fornecedor
cursor.execute("""
CREATE TABLE IF NOT EXISTS Fornecedor (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    produto TEXT NOT NULL
);
""")

# Inserir dados iniciais
cursor.execute("INSERT OR REPLACE INTO Fornecedor VALUES (1, 'Empresa de Leite Parmaleite', 'Rua dos Leites, 23', 'Leite')")
cursor.execute("INSERT OR REPLACE INTO Fornecedor VALUES (2, 'Peixaria Abril', 'Rua dos Leites, 26', 'Peixe')")
cursor.execute("INSERT OR REPLACE INTO Fornecedor VALUES (3, 'Açougue Legal', 'Rua das Carnes, 30', 'Carnes')")
cursor.execute("INSERT OR REPLACE INTO Fornecedor VALUES (4, 'Açougue Novo', 'Rua das Carnes, 50', 'Carnes')")

# 1️⃣ Inserir dois novos fornecedores
cursor.execute("INSERT OR REPLACE INTO Fornecedor VALUES (5, 'Padaria do Pão', 'Rua das Flores, 100', 'Pães')")
cursor.execute("INSERT OR REPLACE INTO Fornecedor VALUES (6, 'Marcenaria Martelo', 'Avenida Central, 200', 'Móveis')")

# 2️⃣ Atualizar endereço do fornecedor com id = 2
cursor.execute("""
UPDATE Fornecedor
SET endereco = 'Rua dos Peixes, 26'
WHERE id = 2;
""")

# 3️⃣ Selecionar todos os registros
print("\n📋 Todos os fornecedores:")
for row in cursor.execute("SELECT * FROM Fornecedor;"):
    print(row)

# 4️⃣ Selecionar fornecedores cujo produto seja 'Carnes'
print("\n🥩 Fornecedores de Carnes:")
for row in cursor.execute("SELECT * FROM Fornecedor WHERE produto = 'Carnes';"):
    print(row)

# 5️⃣ Remover fornecedor com id = 1
cursor.execute("DELETE FROM Fornecedor WHERE id = 1;")

# Mostrar tabela final
print("\n📋 Fornecedores após DELETE:")
for row in cursor.execute("SELECT * FROM Fornecedor;"):
    print(row)

# Salvar alterações e fechar
conexao.commit()
conexao.close()

# Explicação
"""🔎 Passo a passo do que aconteceu
Criação da tabela

Foi criada a tabela Fornecedor com as colunas: id, nome, endereco, produto.

Inserção inicial

Foram inseridos 4 fornecedores: Parmaleite, Peixaria Abril, Açougue Legal e Açougue Novo.

Novos fornecedores (INSERT)

Foram adicionados mais dois:

Padaria do Pão (id 5)

Marcenaria Martelo (id 6)

Atualização (UPDATE)

O endereço da Peixaria Abril (id 2) foi alterado de Rua dos Leites, 26 para Rua dos Peixes, 26.

Seleção (SELECT)

Primeiro, listou todos os fornecedores → ids 1 a 6.

Depois, listou apenas os que têm produto = 'Carnes' → Açougue Legal e Açougue Novo.

Remoção (DELETE)

O fornecedor com id = 1 (Parmaleite) foi removido.

Tabela final

Restaram os fornecedores com ids 2 a 6:

Peixaria Abril

Açougue Legal

Açougue Novo

Padaria do Pão

Marcenaria Martelo"""
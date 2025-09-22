"""Exercício:
1 = Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. As tabelas devem compreender as seguintes funcionalidades:
1 = As tarefas devem ser divididas em “categorias”;
2 = Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
3 = As restrições/relacionamentos devem fazer sentido."""



"""
2 = Crie um programa em Python que gere tabelas para uma aplicação de eventos. Elas devem compreender as seguintes funcionalidades:
1 = Eventos devem ter título, data e local, além da referência ao organizador;
2 = O organizador deve ter nome, email e cpf;
3 = As restrições/relacionamentos devem fazer sentido."""

# Resposta 

# -------------------------------
# PARTE 1 - GERENCIADOR DE TAREFAS
# -------------------------------
# (todo o código do menu de tarefas que você já tem)

# -------------------------------
# PARTE 2 - SISTEMA DE EVENTOS
# -------------------------------
import sqlite3
from tkinter import Menu

def conectar_eventos():
    return sqlite3.connect("eventos.db")

def criar_tabelas_eventos():
    conn = conectar_eventos()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS organizador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        cpf TEXT NOT NULL UNIQUE
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS evento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        data TEXT NOT NULL,
        local TEXT NOT NULL,
        organizador_id INTEGER NOT NULL,
        FOREIGN KEY (organizador_id) REFERENCES organizador(id)
    );
    """)
    conn.commit()
    conn.close()

def inserir_organizador(nome, email, cpf):
    conn = conectar_eventos()
    cur = conn.cursor()
    cur.execute("INSERT INTO organizador (nome, email, cpf) VALUES (?, ?, ?)", (nome, email, cpf))
    conn.commit()
    conn.close()

def inserir_evento(titulo, data, local, organizador_id):
    conn = conectar_eventos()
    cur = conn.cursor()
    cur.execute("INSERT INTO evento (titulo, data, local, organizador_id) VALUES (?, ?, ?, ?)",
                (titulo, data, local, organizador_id))
    conn.commit()
    conn.close()

def listar_eventos():
    conn = conectar_eventos()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.id, e.titulo, e.data, e.local, o.nome as organizador
        FROM evento e
        JOIN organizador o ON e.organizador_id = o.id
        ORDER BY e.data;
    """)
    eventos = cur.fetchall()
    conn.close()
    return eventos

# -------------------------------
# ESCOLHA DE QUAL PARTE RODAR
# -------------------------------
if __name__ == "__main__":
    print("=== Escolha o sistema ===")
    print("1 - Gerenciador de Tarefas")
    print("2 - Sistema de Eventos")
    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        Menu()  # chama o menu de tarefas
    elif escolha == "2":
        criar_tabelas_eventos()
        inserir_organizador("Maria Silva", "maria@email.com", "123.456.789-00")
        inserir_organizador("João Souza", "joao@email.com", "987.654.321-00")
        inserir_evento("Congresso de Tecnologia", "2025-10-15", "São Paulo", 1)
        inserir_evento("Workshop de Python", "2025-11-02", "Rio de Janeiro", 2)

        print("\n📅 Lista de eventos:")
        for e in listar_eventos():
            print(f"{e[0]} - {e[1]} | {e[2]} | {e[3]} | Organizador: {e[4]}")

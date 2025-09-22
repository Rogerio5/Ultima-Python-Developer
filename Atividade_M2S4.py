"""Com esta base de dados, vamos criar a aplicação CLI TODO com as funcionalidades:

Criar, atualizar e excluir um TODO;
Criar, atualizar e excluir categorias;
Listar todos os afazeres de um dia específico;
Listar todas as categorias;
Marcar uma tarefa como concluída.
Para esta atividade, recomenda-se criar o banco de dados e as tabelas utilizando o DBeaver e, para cada item da atividade, fazer um programa Python nos moldes dos programas criados nesta semana. Obs: Foram feitos no DBeaver"""

# Resposta 
import sqlite3

# --------------------------------
# Conexão com o banco de dados
# --------------------------------
def get_conn():
    conn = sqlite3.connect("tarefas.db")
    # Ativa verificação de chave estrangeira no SQLite
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

conn = get_conn()
cursor = conn.cursor()

# --------------------------------
# Utilitários
# --------------------------------
def format_status(valor):
    return "Concluída" if valor == 1 else "Pendente"

def print_tarefa_row(row):
    # row: (id, nome_tarefa, data, status_int, nome_categoria)
    print(f"[{row[0]}] {row[1]} | Data: {row[2]} | Status: {format_status(row[3])} | Categoria: {row[4]}")

def print_categoria_row(row):
    # row: (id, nome)
    print(f"[{row[0]}] {row[1]}")

# -------------------------------
# Funções para TAREFAS
# -------------------------------
def criar_tarefa(nome, data, status, categoria_id):
    try:
        cursor.execute(
            """
            INSERT INTO tarefa (nome, data, status, categoria_id)
            VALUES (?, ?, ?, ?)
            """,
            (nome, data, status, categoria_id),
        )
        conn.commit()
        print("✅ Tarefa criada com sucesso!")
    except sqlite3.IntegrityError as e:
        print(f"❌ Erro ao criar tarefa (verifique a categoria_id): {e}")

def listar_tarefas():
    cursor.execute(
        """
        SELECT t.id, t.nome, t.data, t.status, c.nome
        FROM tarefa t
        JOIN categoria c ON t.categoria_id = c.id
        ORDER BY t.data, t.id
        """
    )
    tarefas = cursor.fetchall()
    if tarefas:
        for row in tarefas:
            print_tarefa_row(row)
    else:
        print("⚠️ Nenhuma tarefa encontrada.")

def listar_tarefas_pendentes():
    """Lista apenas tarefas pendentes"""
    cursor.execute("""
        SELECT t.id, t.nome, t.data, t.status, c.nome
        FROM tarefa t
        JOIN categoria c ON t.categoria_id = c.id
        WHERE t.status = 0
        ORDER BY t.data, t.id
    """)
    tarefas = cursor.fetchall()
    if tarefas:
        for row in tarefas:
            print_tarefa_row(row)
    else:
        print("⚠️ Nenhuma tarefa pendente encontrada.")

def listar_tarefas_concluidas():
    """Lista apenas tarefas concluídas"""
    cursor.execute("""
        SELECT t.id, t.nome, t.data, t.status, c.nome
        FROM tarefa t
        JOIN categoria c ON t.categoria_id = c.id
        WHERE t.status = 1
        ORDER BY t.data, t.id
    """)
    tarefas = cursor.fetchall()
    if tarefas:
        for row in tarefas:
            print_tarefa_row(row)
    else:
        print("⚠️ Nenhuma tarefa concluída encontrada.")

def atualizar_tarefa(id_tarefa, novo_nome, nova_data, novo_status, nova_categoria_id):
    try:
        cursor.execute(
            """
            UPDATE tarefa
            SET nome = ?, data = ?, status = ?, categoria_id = ?
            WHERE id = ?
            """,
            (novo_nome, nova_data, novo_status, nova_categoria_id, id_tarefa),
        )
        conn.commit()
        if cursor.rowcount:
            print("✅ Tarefa atualizada com sucesso!")
        else:
            print("⚠️ Nenhuma tarefa com esse ID.")
    except sqlite3.IntegrityError as e:
        print(f"❌ Erro ao atualizar tarefa (verifique a categoria_id): {e}")

def excluir_tarefa(id_tarefa):
    cursor.execute("DELETE FROM tarefa WHERE id = ?", (id_tarefa,))
    conn.commit()
    if cursor.rowcount:
        print("✅ Tarefa excluída com sucesso!")
    else:
        print("⚠️ Nenhuma tarefa com esse ID.")

def listar_tarefas_por_dia(data):
    cursor.execute(
        """
        SELECT t.id, t.nome, t.data, t.status, c.nome
        FROM tarefa t
        JOIN categoria c ON t.categoria_id = c.id
        WHERE t.data = ?
        ORDER BY t.id
        """,
        (data,),
    )
    tarefas = cursor.fetchall()
    if tarefas:
        for row in tarefas:
            print_tarefa_row(row)
    else:
        print("⚠️ Nenhuma tarefa encontrada para esta data.")

def concluir_tarefa(id_tarefa):
    cursor.execute("UPDATE tarefa SET status = 1 WHERE id = ?", (id_tarefa,))
    conn.commit()
    if cursor.rowcount:
        print("✅ Tarefa concluída com sucesso!")
    else:
        print("⚠️ Nenhuma tarefa com esse ID.")

# -------------------------------
# Funções para CATEGORIAS
# -------------------------------
def criar_categoria(nome):
    try:
        cursor.execute("INSERT INTO categoria (nome) VALUES (?)", (nome,))
        conn.commit()
        print("✅ Categoria criada com sucesso!")
    except sqlite3.IntegrityError as e:
        print(f"❌ Erro ao criar categoria (nome pode existir): {e}")

def listar_categorias():
    cursor.execute("SELECT id, nome FROM categoria ORDER BY id")
    categorias = cursor.fetchall()
    if categorias:
        for row in categorias:
            print_categoria_row(row)
    else:
        print("⚠️ Nenhuma categoria encontrada.")

def atualizar_categoria(id_categoria, novo_nome):
    try:
        cursor.execute("UPDATE categoria SET nome = ? WHERE id = ?", (novo_nome, id_categoria))
        conn.commit()
        if cursor.rowcount:
            print("✅ Categoria atualizada com sucesso!")
        else:
            print("⚠️ Nenhuma categoria com esse ID.")
    except sqlite3.IntegrityError as e:
        print(f"❌ Erro ao atualizar categoria (nome pode existir): {e}")

def excluir_categoria(id_categoria):
    try:
        cursor.execute("DELETE FROM categoria WHERE id = ?", (id_categoria,))
        conn.commit()
        if cursor.rowcount:
            print("✅ Categoria excluída com sucesso!")
        else:
            print("⚠️ Nenhuma categoria com esse ID.")
    except sqlite3.IntegrityError as e:
        print(f"❌ Erro ao excluir categoria (pode haver tarefas vinculadas): {e}")

# -------------------------------
# Menu interativo (CLI)
# -------------------------------
def menu():
    while True:
        print("\n=== MENU TODO ===")
        print("1. Criar tarefa")
        print("2. Atualizar tarefa")
        print("3. Excluir tarefa")
        print("4. Listar tarefas")
        print("5. Listar tarefas por dia")
        print("6. Criar categoria")
        print("7. Atualizar categoria")
        print("8. Excluir categoria")
        print("9. Listar categorias")
        print("10. Concluir tarefa")
        print("11. Listar tarefas pendentes")
        print("12. Listar tarefas concluídas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                nome = input("Nome da tarefa: ").strip()
                data = input("Data (YYYY-MM-DD): ").strip()
                categoria_id = int(input("ID da categoria: ").strip())
                criar_tarefa(nome, data, 0, categoria_id)

            elif opcao == "2":
                id_tarefa = int(input("ID da tarefa a atualizar: ").strip())
                novo_nome = input("Novo nome: ").strip()
                nova_data = input("Nova data (YYYY-MM-DD): ").strip()
                novo_status = int(input("Novo status (0=pendente, 1=concluída): ").strip())
                nova_categoria_id = int(input("Novo ID da categoria: ").strip())
                atualizar_tarefa(id_tarefa, novo_nome, nova_data, novo_status, nova_categoria_id)

            elif opcao == "3":
                id_tarefa = int(input("ID da tarefa a excluir: ").strip())
                excluir_tarefa(id_tarefa)

            elif opcao == "4":
                listar_tarefas()

            elif opcao == "5":
                data = input("Digite a data (YYYY-MM-DD): ").strip()
                listar_tarefas_por_dia(data)

            elif opcao == "6":
                nome = input("Nome da categoria: ").strip()
                criar_categoria(nome)

            elif opcao == "7":
                id_categoria = int(input("ID da categoria a atualizar: ").strip())
                novo_nome = input("Novo nome da categoria: ").strip()
                atualizar_categoria(id_categoria, novo_nome)

            elif opcao == "8":
                id_categoria = int(input("ID da categoria a excluir: ").strip())
                excluir_categoria(id_categoria)

            elif opcao == "9":
                listar_categorias()

            elif opcao == "10":
                id_tarefa = int(input("ID da tarefa a concluir: ").strip())
                concluir_tarefa(id_tarefa)

            elif opcao == "11":
                listar_tarefas_pendentes()

            elif opcao == "12":
                listar_tarefas_concluidas()

            elif opcao == "0":
                print("👋 Saindo do programa...")
                break

            else:
                print("⚠️ Opção inválida! Tente novamente.")
        except ValueError:
            print("❌ Entrada inválida. Digite números onde solicitado.")

if __name__ == "__main__":
    try:
        menu()
    finally:
        # Garante fechamento da conexão ao sair
        try:
            cursor.close()
        except:
            pass
        try:
            conn.close()
        except:
            pass


"""🔹 Etapa 1 – Banco no DBeaver
Criou o banco tarefas.db.

Criou as tabelas categoria e tarefa com as chaves corretas.

Inseriu dados de teste (categorias e tarefas). 👉 Isso atende à parte “modelar um banco de dados de aplicação TODO usando SQLite”.

🔹 Etapa 2 – Aplicação CLI no Python
No arquivo Atividade_M2S4.py você implementou:

Criar, atualizar e excluir um TODO → funções criar_tarefa, atualizar_tarefa, excluir_tarefa.

Criar, atualizar e excluir categorias → funções criar_categoria, atualizar_categoria, excluir_categoria.

Listar todos os afazeres de um dia específico → função listar_tarefas_por_dia.

Listar todas as categorias → função listar_categorias.

Marcar uma tarefa como concluída → função concluir_tarefa.

Além disso, você montou um menu interativo (CLI) que chama cada uma dessas funções. 👉 Isso atende à parte “criar a aplicação CLI TODO com as funcionalidades”.

✅ Conclusão
No DBeaver: ✔️ banco e tabelas criados corretamente.

No Python: ✔️ programa CLI implementado com todas as funcionalidades pedidas."""
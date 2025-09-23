import sqlite3

# Conecta ao banco
conn = sqlite3.connect("noticias.db")
cursor = conn.cursor()

# Conta quantos registros existem
cursor.execute("SELECT COUNT(*) FROM noticias")
total = cursor.fetchone()[0]
print(f"Total de notícias salvas: {total}\n")

# Pergunta ao usuário se quer filtrar por categoria
categoria_desejada = input("Digite a categoria que deseja listar (ou deixe vazio para todas): ").strip()

if categoria_desejada:
    cursor.execute("""
        SELECT categoria, titulo, data, descricao 
        FROM noticias 
        WHERE categoria = ? 
        ORDER BY id DESC 
        LIMIT 10
    """, (categoria_desejada,))
else:
    cursor.execute("""
        SELECT categoria, titulo, data, descricao 
        FROM noticias 
        ORDER BY id DESC 
        LIMIT 10
    """)

registros = cursor.fetchall()

if not registros:
    print("⚠️ Nenhuma notícia encontrada para esse filtro.")
else:
    for i, (categoria, titulo, data, descricao) in enumerate(registros, start=1):
        print(f"{i}. [{categoria}] {titulo} ({data})")
        print(f"   {descricao}\n")

conn.close()


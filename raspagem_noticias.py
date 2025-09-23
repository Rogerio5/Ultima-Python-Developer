from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3
import time

# Pergunta ao usuário qual categoria deseja raspar
print("Escolha a categoria para raspar:")
print("1 - Tecnologia (TecMundo)")
print("2 - Esportes (Globo Esporte)")
opcao = input("Digite 1 ou 2: ").strip()

# Configura o driver (Chrome)
driver = webdriver.Chrome()

# Conecta/cria o banco SQLite
conn = sqlite3.connect("noticias.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS noticias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT,
    titulo TEXT,
    data TEXT,
    descricao TEXT
)
""")

# -------------------------------
# TECMUNDO (Tecnologia)
# -------------------------------
if opcao == "1":
    driver.get("https://www.tecmundo.com.br/novidades")
    time.sleep(5)  # espera carregar os cards

    noticias = driver.find_elements(By.CSS_SELECTOR, ".tec--card__info")

    for noticia in noticias:
        try:
            titulo = noticia.find_element(By.TAG_NAME, "h3").text
        except:
            titulo = "Sem título"

        try:
            descricao = noticia.find_element(By.TAG_NAME, "p").text
        except:
            descricao = "Sem descrição"

        print(f"[Tecnologia] {titulo} | {descricao}")

        cursor.execute("""
            INSERT INTO noticias (categoria, titulo, data, descricao)
            VALUES (?, ?, ?, ?)
        """, ("Tecnologia", titulo, "", descricao))

# -------------------------------
# GLOBO ESPORTE (Esportes)
# -------------------------------
elif opcao == "2":
    driver.get("https://ge.globo.com/")
    time.sleep(5)  # espera carregar os cards

    noticias = driver.find_elements(By.CSS_SELECTOR, ".feed-post-body")

    for noticia in noticias:
        try:
            titulo = noticia.find_element(By.TAG_NAME, "a").text
        except:
            titulo = "Sem título"

        try:
            descricao = noticia.find_element(By.CLASS_NAME, "feed-post-body-resumo").text
        except:
            descricao = "Sem descrição"

        print(f"[Esportes] {titulo} | {descricao}")

        cursor.execute("""
            INSERT INTO noticias (categoria, titulo, data, descricao)
            VALUES (?, ?, ?, ?)
        """, ("Esportes", titulo, "", descricao))

else:
    print("⚠️ Opção inválida. Digite 1 ou 2.")

# Salva no banco
conn.commit()
conn.close()
driver.quit()

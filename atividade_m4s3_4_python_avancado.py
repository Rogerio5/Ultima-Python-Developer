# exercicio4.py

# Lista global que armazena as peças cadastradas
pecas = []

def gerar_codigo():
    """
    Gera o próximo código para uma nova peça.
    Se a lista estiver vazia, retorna 1.
    Caso contrário, retorna o último código + 1.
    """
    if not pecas:
        return 1
    return pecas[-1]["codigo"] + 1


def cadastrar_peca(nome, fabricante, valor):
    """
    Cadastra uma nova peça na lista global 'pecas'.
    """
    codigo = gerar_codigo()
    nova_peca = {
        "codigo": codigo,
        "nome": nome,
        "fabricante": fabricante,
        "valor": valor
    }
    pecas.append(nova_peca)
    return nova_peca


def consultar_pecas():
    """
    Retorna a lista de peças cadastradas.
    """
    return pecas


def remover_peca(codigo):
    """
    Remove uma peça pelo código.
    Retorna True se removeu, False se não encontrou.
    """
    for p in pecas:
        if p["codigo"] == codigo:
            pecas.remove(p)
            return True
    return False


def main():
    while True:
        print("\n=== MENU PEÇAS ===")
        print("1 - Cadastrar peça")
        print("2 - Consultar peças")
        print("3 - Remover peça")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da peça: ")
            fabricante = input("Fabricante: ")
            valor = float(input("Valor: "))
            nova = cadastrar_peca(nome, fabricante, valor)
            print(f"Peça cadastrada: {nova}")

        elif opcao == "2":
            for p in consultar_pecas():
                print(p)

        elif opcao == "3":
            codigo = int(input("Código da peça a remover: "))
            if remover_peca(codigo):
                print("Peça removida com sucesso.")
            else:
                print("Peça não encontrada.")

        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

# Explicando por meio visual 

"""
🔧 Sistema de Cadastro de Peças – Documentação em Tabela

📊 Visão Geral
Este programa permite cadastrar, consultar e remover peças de uma lista global chamada `pecas`.
Cada peça possui: código, nome, fabricante e valor.

──────────────────────────────────────────────
📌 Estrutura das Funções

| Função / Parte do código | O que faz                                                                 | Exemplo de uso                                                                 |
|---------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| pecas = []               | Lista global que armazena todas as peças cadastradas.                     | Após cadastrar, pecas = [{"codigo": 1, "nome": "Peça A", ...}]                 |
| gerar_codigo()           | Gera o próximo código automaticamente. Se lista vazia → 1, senão último+1 | Lista vazia → retorna 1 ; Lista com última peça código=3 → retorna 4           |
| cadastrar_peca(...)      | Cria um dicionário com dados da peça e adiciona à lista global.           | cadastrar_peca("Peça A","Fab X",10.0) → {"codigo":1,"nome":"Peça A",...}      |
| consultar_pecas()        | Retorna a lista completa de peças cadastradas.                            | Se houver 2 peças, retorna lista com 2 dicionários.                            |
| remover_peca(codigo)     | Remove peça pelo código. Retorna True se removeu, False se não encontrou. | remover_peca(1) → True (se existir) ; remover_peca(99) → False                 |
| main()                   | Exibe menu interativo para o usuário cadastrar, consultar ou remover.     | Usuário escolhe opção 1 → cadastra peça ; opção 2 → lista peças ; opção 3 → remove |
| if __name__ == "__main__"| Executa o programa apenas se rodado diretamente.                          | python exercicio4.py → inicia o menu                                           |

──────────────────────────────────────────────
📊 Fluxo do Menu (main)

1 - Cadastrar peça  
   → Solicita nome, fabricante e valor.  
   → Gera código automático.  
   → Adiciona peça à lista.  

2 - Consultar peças  
   → Percorre a lista `pecas` e imprime cada peça cadastrada.  

3 - Remover peça  
   → Solicita código.  
   → Se existir, remove e mostra mensagem de sucesso.  
   → Se não existir, mostra mensagem de erro.  

4 - Sair  
   → Encerra o programa.  

──────────────────────────────────────────────
✅ Interpretação
- O programa funciona como um pequeno **sistema de estoque**.  
- Cada peça é representada por um dicionário com código, nome, fabricante e valor.  
- O código é gerado automaticamente para evitar duplicidade.  
- O menu interativo permite ao usuário manipular a lista de peças de forma simples.
"""

# Explicando por meio linha de código

"""
🔧 Sistema de Cadastro de Peças – Documentação linha a linha

# Lista global que armazena as peças cadastradas
pecas = []
→ Cria uma lista vazia chamada `pecas`, que será usada para armazenar dicionários de peças.

def gerar_codigo():
    → Define a função que gera o próximo código automaticamente.
    if not pecas:
        → Se a lista estiver vazia, retorna 1 (primeira peça).
        return 1
    return pecas[-1]["codigo"] + 1
        → Caso contrário, pega o último código da lista e soma 1.

def cadastrar_peca(nome, fabricante, valor):
    → Define a função que cadastra uma nova peça.
    codigo = gerar_codigo()
        → Gera automaticamente o código da peça.
    nova_peca = {"codigo": codigo, "nome": nome, "fabricante": fabricante, "valor": valor}
        → Cria um dicionário com os dados da peça.
    pecas.append(nova_peca)
        → Adiciona a peça à lista global.
    return nova_peca
        → Retorna o dicionário da peça cadastrada.

def consultar_pecas():
    → Retorna a lista completa de peças cadastradas.
    return pecas

def remover_peca(codigo):
    → Define a função que remove uma peça pelo código.
    for p in pecas:
        → Percorre todas as peças cadastradas.
        if p["codigo"] == codigo:
            → Se encontrar a peça com o código informado:
            pecas.remove(p)
                → Remove a peça da lista.
            return True
                → Retorna True indicando sucesso.
    return False
        → Se não encontrar, retorna False.

def main():
    → Função principal que exibe o menu interativo.
    while True:
        → Loop infinito até o usuário escolher sair.
        print("\n=== MENU PEÇAS ===")
            → Exibe o título do menu.
        print("1 - Cadastrar peça")
        print("2 - Consultar peças")
        print("3 - Remover peça")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
            → Lê a opção digitada pelo usuário.

        if opcao == "1":
            → Se o usuário escolher cadastrar:
            nome = input("Nome da peça: ")
            fabricante = input("Fabricante: ")
            valor = float(input("Valor: "))
                → Solicita os dados da peça.
            nova = cadastrar_peca(nome, fabricante, valor)
                → Cadastra a peça chamando a função.
            print(f"Peça cadastrada: {nova}")
                → Mostra a peça cadastrada.

        elif opcao == "2":
            → Se o usuário escolher consultar:
            for p in consultar_pecas():
                print(p)
                → Imprime cada peça cadastrada.

        elif opcao == "3":
            → Se o usuário escolher remover:
            codigo = int(input("Código da peça a remover: "))
                → Solicita o código da peça.
            if remover_peca(codigo):
                print("Peça removida com sucesso.")
            else:
                print("Peça não encontrada.")

        elif opcao == "4":
            → Se o usuário escolher sair:
            print("Saindo...")
            break
                → Encerra o loop e finaliza o programa.

        else:
            → Se o usuário digitar uma opção inválida:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
    → Executa a função principal apenas se o arquivo for rodado diretamente.
"""
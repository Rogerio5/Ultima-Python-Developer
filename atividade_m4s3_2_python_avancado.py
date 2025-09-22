# exercicio2.py

CARDAPIO = {
    "100": {"nome": "Cachorro Quente", "preco": 9.0},
    "101": {"nome": "X-Salada", "preco": 12.0},
    "102": {"nome": "X-Bacon", "preco": 15.0},
    "103": {"nome": "Misto Quente", "preco": 11.0},
    "104": {"nome": "Pão na Chapa", "preco": 5.0},
    "200": {"nome": "Refrigerante Lata", "preco": 6.0},
    "201": {"nome": "Chá Gelado", "preco": 5.0},
}

def calcular_total(pedidos, cardapio=CARDAPIO):
    """
    Recebe uma lista de tuplas (codigo, quantidade) e devolve o total.
    Ignora códigos inexistentes.
    """
    total = 0.0
    for codigo, qtd in pedidos:
        item = cardapio.get(str(codigo))
        if item and qtd > 0:
            total += item["preco"] * qtd
    return round(total, 2)

def formatar_item(codigo, cardapio=CARDAPIO):
    """Retorna uma string formatada 'codigo - nome - preco' ou mensagem de inválido."""
    item = cardapio.get(str(codigo))
    if not item:
        return f"Código {codigo} inválido."
    return f"{codigo} - {item['nome']} - R$ {item['preco']:.2f}"

def imprimir_cardapio(cardapio=CARDAPIO):
    print("=== CARDÁPIO ===")
    for codigo in sorted(cardapio.keys()):
        print(formatar_item(codigo, cardapio))

def main():
    imprimir_cardapio()
    print("\nDigite os pedidos (código e quantidade). Enter vazio para finalizar.")
    pedidos = []
    while True:
        codigo = input("Código: ").strip()
        if not codigo:
            break
        qtd_str = input("Quantidade: ").strip()
        if not qtd_str:
            break
        try:
            qtd = int(qtd_str)
        except ValueError:
            print("Quantidade inválida, tente novamente.")
            continue
        if str(codigo) not in CARDAPIO:
            print("Código inválido, tente novamente.")
            continue
        pedidos.append((codigo, qtd))

    total = calcular_total(pedidos, CARDAPIO)
    print(f"\nTotal: R$ {total:.2f}")

if __name__ == "__main__":
    main()

# Explicando em meio visual

"""
🍔 Sistema de Lanchonete – Documentação

Este programa simula um cardápio de lanchonete, permitindo ao usuário escolher itens pelo código,
informar quantidades e calcular o valor total da compra.

📊 Estrutura explicada em tabela:

| Parte do código                  | O que faz                                                                 | Exemplo prático                                                                 |
|----------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| CARDAPIO                         | Dicionário com os itens disponíveis (código, nome e preço).               | "100": {"nome": "Cachorro Quente", "preco": 9.0} → código 100 = Cachorro Quente |
| calcular_total(pedidos)          | Recebe lista de tuplas (código, quantidade) e soma os valores.            | [("100", 2), ("101", 1)] → 2*9 + 1*12 = 30                                      |
| formatar_item(codigo)            | Retorna string formatada "codigo - nome - preco" ou mensagem de inválido. | formatar_item("100") → "100 - Cachorro Quente - R$ 9.00"                        |
| imprimir_cardapio()              | Mostra todos os itens do cardápio na tela.                                | Exibe todos os códigos e preços ordenados.                                      |
| main()                           | Fluxo principal: imprime cardápio, lê pedidos, calcula e mostra o total.  | Usuário digita 100 (2 unid) + 200 (1 unid) → Total R$ 24.00                     |
| if __name__ == "__main__": main()| Garante que o programa só roda o main se for executado diretamente.       | python arquivo.py → abre o cardápio e pede pedidos.                             |

🚀 Como interpretar:
- O programa usa o CARDÁPIO como base de dados.
- O cálculo do total ignora códigos inválidos ou quantidades negativas.
- A interação com o usuário é feita no `main`, mas as funções podem ser testadas isoladamente.
- Ideal para treinar testes unitários com pytest:
  - Testar `calcular_total` com pedidos válidos, inválidos e mistos.
  - Testar `formatar_item` com códigos existentes e inexistentes.
  - Testar `imprimir_cardapio` capturando a saída.
"""

# Explicando por meio da linha de código

"""
🍔 Sistema de Lanchonete – Documentação linha a linha

CARDÁPIO = {...}
    → Dicionário que guarda os itens disponíveis, cada um com código, nome e preço.

def calcular_total(pedidos, cardapio=CARDAPIO):
    → Define a função que calcula o valor total de uma lista de pedidos.

    total = 0.0
        → Inicializa o acumulador do valor total em 0.

    for codigo, qtd in pedidos:
        → Percorre cada pedido recebido (código e quantidade).

        item = cardapio.get(str(codigo))
            → Busca o item no cardápio pelo código informado.

        if item and qtd > 0:
            → Verifica se o código existe e se a quantidade é válida (>0).

            total += item["preco"] * qtd
                → Soma ao total o preço do item multiplicado pela quantidade.

    return round(total, 2)
        → Retorna o valor total arredondado com 2 casas decimais.


def formatar_item(codigo, cardapio=CARDAPIO):
    → Define a função que formata a exibição de um item do cardápio.

    item = cardapio.get(str(codigo))
        → Busca o item no cardápio.

    if not item:
        → Se não encontrar, retorna mensagem de inválido.

        return f"Código {codigo} inválido."

    return f"{codigo} - {item['nome']} - R$ {item['preco']:.2f}"
        → Caso exista, retorna string formatada com código, nome e preço.


def imprimir_cardapio(cardapio=CARDAPIO):
    → Define a função que imprime o cardápio completo.

    print("=== CARDÁPIO ===")
        → Exibe título do cardápio.

    for codigo in sorted(cardapio.keys()):
        → Percorre os códigos em ordem crescente.

        print(formatar_item(codigo, cardapio))
            → Imprime cada item formatado.


def main():
    → Função principal que organiza o fluxo do programa.

    imprimir_cardapio()
        → Mostra o cardápio na tela.

    print("\nDigite os pedidos (código e quantidade). Enter vazio para finalizar.")
        → Instrui o usuário sobre como inserir pedidos.

    pedidos = []
        → Cria lista vazia para armazenar os pedidos.

    while True:
        → Loop infinito até o usuário parar.

        codigo = input("Código: ").strip()
            → Pede o código do item.

        if not codigo:
            → Se o usuário não digitar nada, encerra o loop.

            break

        qtd_str = input("Quantidade: ").strip()
            → Pede a quantidade.

        if not qtd_str:
            → Se não digitar nada, encerra o loop.

            break

        try:
            qtd = int(qtd_str)
                → Converte a quantidade para número inteiro.
        except ValueError:
            → Se não for número, mostra erro.

            print("Quantidade inválida, tente novamente.")
            continue

        if str(codigo) not in CARDAPIO:
            → Se o código não existir no cardápio, mostra erro.

            print("Código inválido, tente novamente.")
            continue

        pedidos.append((codigo, qtd))
            → Adiciona o pedido válido à lista.

    total = calcular_total(pedidos, CARDAPIO)
        → Calcula o valor total dos pedidos.

    print(f"\nTotal: R$ {total:.2f}")
        → Exibe o valor final formatado.


if __name__ == "__main__":
    main()
        → Executa a função principal apenas se o arquivo for rodado diretamente.
"""
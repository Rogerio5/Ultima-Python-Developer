# exercicio3.py

def calcular_preco_volume(volume):
    """
    Calcula o preço base de acordo com o volume em cm³.
    """
    if volume < 1000:
        return 10.0
    elif volume < 10000:
        return 20.0
    elif volume < 30000:
        return 30.0
    elif volume < 100000:
        return 20.0
    else:
        return 0.0


def calcular_multiplicador_peso(peso):
    """
    Calcula o multiplicador de acordo com o peso em kg.
    """
    if peso <= 0.1:
        return 1.0
    elif peso <= 1:
        return 1.5
    elif peso <= 10:
        return 2.0
    elif peso <= 30:
        return 3.0
    else:
        return 0.0


def calcular_multiplicador_rota(rota):
    """
    Calcula o multiplicador de acordo com a rota.
    rs = Rio de Janeiro -> São Paulo
    sr = São Paulo -> Rio de Janeiro
    bs = Brasília -> São Paulo
    br = Brasília -> Rio de Janeiro
    """
    rota = rota.lower()
    if rota in ("rs", "sr"):
        return 1.0
    elif rota == "bs":
        return 1.2
    elif rota == "br":
        return 1.5
    else:
        return 0.0


def calcular_frete(preco_volume, multiplicador_peso, multiplicador_rota):
    """
    Calcula o valor final do frete.
    """
    return preco_volume * multiplicador_peso * multiplicador_rota


def main():
    print("=== Cálculo de Frete ===")
    volume = float(input("Digite o volume da encomenda (em cm³): "))
    peso = float(input("Digite o peso da encomenda (em kg): "))
    rota = input("Digite a rota (RS, SR, BS, BR): ")

    preco_volume = calcular_preco_volume(volume)
    mult_peso = calcular_multiplicador_peso(peso)
    mult_rota = calcular_multiplicador_rota(rota)

    total = calcular_frete(preco_volume, mult_peso, mult_rota)

    print(f"\nPreço base pelo volume: R$ {preco_volume:.2f}")
    print(f"Multiplicador pelo peso: {mult_peso}")
    print(f"Multiplicador pela rota: {mult_rota}")
    print(f"Valor total do frete: R$ {total:.2f}")


if __name__ == "__main__":
    main()

# Explicação por meio visual

"""
📦 Sistema de Cálculo de Frete – Documentação Completa

Este programa calcula o valor do frete de uma encomenda com base em três fatores:
- Volume (cm³)
- Peso (kg)
- Rota escolhida

──────────────────────────────────────────────
📊 Tabela de funções

| Função / Parte do código              | O que faz                                                                 | Exemplos práticos                                                                 |
|---------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| calcular_preco_volume(volume)         | Define o preço base de acordo com o volume em cm³.                        | volume=500 → 10.0 ; volume=5000 → 20.0 ; volume=20000 → 30.0 ; volume=80000 → 20.0|
| calcular_multiplicador_peso(peso)     | Define o multiplicador de acordo com o peso em kg.                        | peso=0.05 → 1.0 ; peso=0.5 → 1.5 ; peso=5 → 2.0 ; peso=20 → 3.0                   |
| calcular_multiplicador_rota(rota)     | Define o multiplicador de acordo com a rota escolhida.                    | "RS"/"SR" → 1.0 ; "BS" → 1.2 ; "BR" → 1.5 ; outro → 0.0                           |
| calcular_frete(preco, mult_peso, mult_rota) | Calcula o valor final do frete multiplicando os fatores.          | Ex: preco=20, mult_peso=2.0, mult_rota=1.5 → 20*2*1.5 = 60.0                      |
| main()                                | Fluxo principal: lê dados do usuário, calcula e imprime o resultado.      | Entrada: volume=5000, peso=2, rota="BS" → saída: valor total do frete calculado.  |
| if __name__ == "__main__": main()     | Executa o programa apenas se rodado diretamente.                          | python exercicio3.py → inicia o cálculo de frete.                                 |

──────────────────────────────────────────────
📊 Tabela de valores – calcular_preco_volume

| Volume (cm³) | Faixa aplicada        | Preço base (R$) |
|--------------|-----------------------|-----------------|
| 500          | < 1000                | 10.0            |
| 5000         | 1000 ≤ v < 10000      | 20.0            |
| 20000        | 10000 ≤ v < 30000     | 30.0            |
| 80000        | 30000 ≤ v < 100000    | 20.0            |
| 120000       | ≥ 100000              | 0.0             |

──────────────────────────────────────────────
⚖️ Tabela de valores – calcular_multiplicador_peso

| Peso (kg) | Faixa aplicada      | Multiplicador |
|-----------|---------------------|---------------|
| 0.05      | ≤ 0.1               | 1.0           |
| 0.5       | 0.1 < p ≤ 1         | 1.5           |
| 5         | 1 < p ≤ 10          | 2.0           |
| 20        | 10 < p ≤ 30         | 3.0           |
| 40        | > 30                | 0.0           |

──────────────────────────────────────────────
🚚 Tabela de valores – calcular_multiplicador_rota

| Rota | Descrição                           | Multiplicador |
|------|-------------------------------------|---------------|
| RS   | Rio de Janeiro → São Paulo          | 1.0           |
| SR   | São Paulo → Rio de Janeiro          | 1.0           |
| BS   | Brasília → São Paulo                | 1.2           |
| BR   | Brasília → Rio de Janeiro           | 1.5           |
| XX   | Qualquer outra rota inválida        | 0.0           |

──────────────────────────────────────────────
💰 Exemplos de cálculo final – calcular_frete

Fórmula: frete = preco_volume × multiplicador_peso × multiplicador_rota

| Volume (cm³) | Peso (kg) | Rota | Preço base (R$) | Mult. peso | Mult. rota | Valor final (R$) |
|--------------|-----------|------|-----------------|------------|------------|------------------|
| 5000         | 2         | BS   | 20.0            | 2.0        | 1.2        | 48.0             |
| 20000        | 0.5       | SR   | 30.0            | 1.5        | 1.0        | 45.0             |
| 80000        | 20        | BR   | 20.0            | 3.0        | 1.5        | 90.0             |
| 120000       | 5         | RS   | 0.0             | 2.0        | 1.0        | 0.0              |

──────────────────────────────────────────────
✅ Interpretação:
- O preço base depende do volume.
- O multiplicador depende do peso.
- Outro multiplicador depende da rota.
- O valor final do frete = preço base × multiplicador do peso × multiplicador da rota.
"""

# Explicação por cada linha de código

"""
📦 Sistema de Cálculo de Frete – Documentação linha a linha

def calcular_preco_volume(volume):
    → Define a função que calcula o preço base de acordo com o volume em cm³.

    if volume < 1000:
        → Se o volume for menor que 1000 cm³, retorna preço base de 10.0.

    elif volume < 10000:
        → Se o volume estiver entre 1000 e 9999 cm³, retorna preço base de 20.0.

    elif volume < 30000:
        → Se o volume estiver entre 10000 e 29999 cm³, retorna preço base de 30.0.

    elif volume < 100000:
        → Se o volume estiver entre 30000 e 99999 cm³, retorna preço base de 20.0.

    else:
        → Se o volume for 100000 cm³ ou mais, retorna 0.0 (inválido).

──────────────────────────────────────────────

def calcular_multiplicador_peso(peso):
    → Define a função que calcula o multiplicador de acordo com o peso em kg.

    if peso <= 0.1:
        → Até 100 gramas → multiplicador 1.0.

    elif peso <= 1:
        → Entre 0.1 e 1 kg → multiplicador 1.5.

    elif peso <= 10:
        → Entre 1 e 10 kg → multiplicador 2.0.

    elif peso <= 30:
        → Entre 10 e 30 kg → multiplicador 3.0.

    else:
        → Acima de 30 kg → multiplicador 0.0 (inválido).

──────────────────────────────────────────────

def calcular_multiplicador_rota(rota):
    → Define a função que calcula o multiplicador de acordo com a rota.

    rota = rota.lower()
        → Converte a rota para minúsculas para evitar erros de digitação.

    if rota in ("rs", "sr"):
        → Se rota for RS ou SR → multiplicador 1.0.

    elif rota == "bs":
        → Se rota for BS → multiplicador 1.2.

    elif rota == "br":
        → Se rota for BR → multiplicador 1.5.

    else:
        → Qualquer outra rota → multiplicador 0.0 (inválido).

──────────────────────────────────────────────

def calcular_frete(preco_volume, multiplicador_peso, multiplicador_rota):
    → Define a função que calcula o valor final do frete.

    return preco_volume * multiplicador_peso * multiplicador_rota
        → Multiplica os três fatores e retorna o valor total.

──────────────────────────────────────────────

def main():
    → Função principal que organiza o fluxo do programa.

    print("=== Cálculo de Frete ===")
        → Exibe título do programa.

    volume = float(input("Digite o volume da encomenda (em cm³): "))
        → Solicita ao usuário o volume e converte para número decimal.

    peso = float(input("Digite o peso da encomenda (em kg): "))
        → Solicita ao usuário o peso e converte para número decimal.

    rota = input("Digite a rota (RS, SR, BS, BR): ")
        → Solicita ao usuário a rota.

    preco_volume = calcular_preco_volume(volume)
        → Calcula o preço base pelo volume informado.

    mult_peso = calcular_multiplicador_peso(peso)
        → Calcula o multiplicador pelo peso informado.

    mult_rota = calcular_multiplicador_rota(rota)
        → Calcula o multiplicador pela rota informada.

    total = calcular_frete(preco_volume, mult_peso, mult_rota)
        → Calcula o valor final do frete.

    print(f"\nPreço base pelo volume: R$ {preco_volume:.2f}")
        → Mostra o preço base calculado.

    print(f"Multiplicador pelo peso: {mult_peso}")
        → Mostra o multiplicador do peso.

    print(f"Multiplicador pela rota: {mult_rota}")
        → Mostra o multiplicador da rota.

    print(f"Valor total do frete: R$ {total:.2f}")
        → Mostra o valor final do frete.

──────────────────────────────────────────────

if __name__ == "__main__":
    main()
        → Executa a função principal apenas se o arquivo for rodado diretamente.
"""

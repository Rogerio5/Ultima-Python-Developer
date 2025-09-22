"""Para esta semana, você deve:

1. Acessar a interface do ChatGPT, onde você pode enviar comandos e receber respostas do modelo.

2. Utilizar o ChatGPT como seu “mentor de programação” durante toda a tarefa.

3. Ler atentamente as instruções de cada seção antes de começar a escrever código.

Seção 1: Aprimorar um código existente

Nesta seção, você receberá um trecho de código em Python que possui algumas falhas e precisa ser aprimorado. Use o ChatGPT para identificar erros e fazer melhorias, seguindo as boas práticas de programação.

def calc(numeros):
    s = 0
    for i in numeros:
        soma = s + i
    media = s / len(numeros)
    retornar media
 numeros = [2, 4, 6, 8, 10]
 resultado = calc(numeros)
 print("A média é:", resultado)
– Utilize o ChatGPT para identificar e corrigir os erros no código fornecido.

– Faça melhorias no código, como alterar nomes de variáveis inadequados ou otimizar o cálculo da média.

– Lembre-se de seguir as convenções de nomenclatura adequadas em Python."""

# Explicação do Código no exercicio

"""🔎 Problemas no código original
python
def calc(numeros):
    s = 0
    for i in numeros:
        soma = s + i
    media = s / len(numeros)
    retornar media
 numeros = [2, 4, 6, 8, 10]
 resultado = calc(numeros)
 print("A média é:", resultado)
Erro de lógica no loop

Dentro do for, a variável s nunca é atualizada.

O correto seria s += i, mas o código cria uma variável soma que não é usada.

Palavra reservada incorreta

Em Python usamos return, não retornar.

Indentação incorreta

As últimas linhas (numeros = ...) estão desalinhadas.

Nomes de variáveis pouco claros

s poderia ser soma para ser mais legível.

Otimização possível

Podemos usar a função sum() do Python para calcular a soma diretamente."""

# Resposta 

def calcular_media(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / len(numeros)
    return media

numeros = [2, 4, 6, 8, 10]
resultado = calcular_media(numeros)
print("A média é:", resultado)




"""Seção 2: Debugando código

Nesta seção, você receberá um trecho de código em Python que contém erros. Use o ChatGPT para identificar os erros e corrigi-los.

def calcular_fatorial(numero):
    resultado = 1
    for i em range(numero, 0, -1):
        resultado *= i
    retornar resultado
 numero = 5
 fatorial = calcular_fatorial(numero)
 imprimir("O fatorial de", numero, "é:", fatorial)
– Utilize o ChatGPT para identificar e corrigir os erros no código fornecido.

– Certifique-se de que o código esteja calculando o fatorial corretamente para o número fornecido."""

# Explicação 

"""Principais erros encontrados
for i em → o correto é for i in.

retornar → em Python usamos return.

imprimir → em Python usamos print.

Indentação e espaços no início de linhas fora de funções.

Boa prática: validar entrada não negativa."""

# Resposta 

def calcular_fatorial(numero):
    if numero < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    resultado = 1
    for i in range(numero, 0, -1):
        resultado *= i
    return resultado

numero = 5
fatorial = calcular_fatorial(numero)
print("O fatorial de", numero, "é:", fatorial)



"""Seção 3: Criando um novo código

Nesta seção, você deve criar um novo código Python que atenda aos requisitos fornecidos.

– Crie uma função chamada “calcular_reverso” que receba uma lista de números como parâmetro e retorne uma nova lista contendo os mesmos números, mas na ordem inversa.

– Utilize o ChatGPT para obter sugestões e orientações ao escrever o código.

– Teste a função com pelo menos dois exemplos diferentes para garantir que ela esteja funcionando corretamente."""

def calcular_reverso(numeros):
    """
    Recebe uma lista de números e retorna uma nova lista
    com os elementos na ordem inversa.
    """
    return numeros[::-1]  # usa slicing para inverter a lista


# --- Testes da função ---

# Exemplo 1
lista1 = [1, 2, 3, 4, 5]
print("Lista original:", lista1)
print("Lista invertida:", calcular_reverso(lista1))

# Exemplo 2
lista2 = [10, 20, 30, 40]
print("\nLista original:", lista2)
print("Lista invertida:", calcular_reverso(lista2))

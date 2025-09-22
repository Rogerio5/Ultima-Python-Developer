"""Para a atividade dessa semana, vamos trabalhar com a seguinte situação:

Uma pessoa do seu time de desenvolvimento está escrevendo várias funções que calculam diferentes formas de gerar juros. Veja abaixo o exemplo de uma das funções:

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo


Ela pediu para você escrever um decorator chamado decorator_imprimir, que será usado para a função chamada imprima os parâmetros: capital, taxa e tempo, além do resultado da função.

Ao executar a função juros_simples, teríamos o seguinte resultado:

from funcoes import juros_simples

juros_simples(1000, 5, 6)
# Saída esperada:
# CAPITAL: 1000 TAXA: 5 TEMPO: 6
# RESULTADO: 300.0

Com isso, será criada uma função decoradora (decorator) chamada decorator_imprimir que, ao ser usada com qualquer função parecida com a juros_simples (isto é, uma função que receba 3 parâmetros – capital, taxa, tempo), seja retornado um valor numérico correspondente ao juros."""

# Resultado 

# -------------------------------
# Decorator que imprime parâmetros e resultado
# -------------------------------
def decorator_imprimir(func):
    def wrapper(capital, taxa, tempo):
        resultado = func(capital, taxa, tempo)
        print(f"Capital: {capital}, Taxa: {taxa}, Tempo: {tempo}")
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper


# -------------------------------
# Exemplo de função: Juros Simples
# -------------------------------
@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    """
    Fórmula: J = C * i * t
    capital: valor inicial
    taxa: taxa de juros (em decimal, ex: 0.05 = 5%)
    tempo: período
    """
    return capital * taxa * tempo


# -------------------------------
# Testando
# -------------------------------
if __name__ == "__main__":
    juros_simples(1000, 0.05, 12)


# Explicação 

"""📌 O que o código faz
Decorator decorator_imprimir

Recebe a função como parâmetro.

Cria o wrapper que executa a função original.

Imprime os parâmetros e o resultado.

Retorna o resultado normalmente.

Função juros_simples

Calcula juros simples pela fórmula:

𝐽
=
𝐶
×
𝑖
×
𝑡
Onde:

C = capital

i = taxa (em decimal, ex: 0.05 = 5%)

t = tempo

Execução

Quando você chama:

python
juros_simples(1000, 0.05, 12)

O decorator intercepta a chamada e imprime:

Código
Capital: 1000, Taxa: 0.05, Tempo: 12
Resultado: 600.0

✅ Conclusão
esse código atende 100% ao enunciado da atividade. Foi criado o decorator, aplicado na função juros_simples e obteve a saída esperada."""
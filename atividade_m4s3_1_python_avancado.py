def calcular_valor_total(valor_unitario, quantidade):
    desconto = 1
    if 10 <= quantidade <= 99:
        desconto = 0.95
    elif 100 <= quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade
    return valor_sem_desconto, valor_com_desconto

# Explicando em meio visual 
"""
📊 Tabela de descontos aplicados

Quantidade comprada   | Percentual de desconto | Multiplicador usado | Exemplo (valor unitário = R$10) | Valor sem desconto | Valor com desconto
--------------------- | ---------------------- | ------------------- | ------------------------------- | ------------------ | ------------------
1 a 9                 | 0%                     | 1.00                | 5 unidades                      | 10 × 5 = 50        | 50
10 a 99               | 5%                     | 0.95                | 10 unidades                     | 10 × 10 = 100      | 95
100 a 999             | 10%                    | 0.90                | 100 unidades                    | 10 × 100 = 1000    | 900
1000 ou mais          | 15%                    | 0.85                | 1000 unidades                   | 10 × 1000 = 10000  | 8500

🚀 Como interpretar:
- A função sempre retorna dois valores:
  1. O total sem desconto.
  2. O total com desconto aplicado.
- O desconto é progressivo por quantidade: quanto mais itens você compra, maior o desconto.
- O cálculo é feito multiplicando o preço unitário × quantidade × fator de desconto.
"""


# explicando em cada linha de código

"""
    🔎 O que cada parte faz e como a tabela explica

    desconto = 1  
        → Começa assumindo que não há desconto (100%).  
        → Na tabela, isso corresponde à faixa de 1 a 9 unidades (0% de desconto).

    if 10 <= quantidade <= 99: desconto = 0.95  
        → Se a quantidade está entre 10 e 99, aplica 5% de desconto.  
        → Na tabela, isso aparece como faixa 10 a 99 → 5% → multiplicador 0.95.

    elif 100 <= quantidade <= 999: desconto = 0.90  
        → Se a quantidade está entre 100 e 999, aplica 10% de desconto.  
        → Na tabela, isso aparece como faixa 100 a 999 → 10% → multiplicador 0.90.

    elif quantidade >= 1000: desconto = 0.85  
        → Se a quantidade é 1000 ou mais, aplica 15% de desconto.  
        → Na tabela, isso aparece como faixa 1000+ → 15% → multiplicador 0.85.

    valor_com_desconto = valor_unitario * desconto * quantidade  
        → Calcula o preço final já com o desconto aplicado.  
        → Na tabela, é a coluna “Valor com desconto”.

    valor_sem_desconto = valor_unitario * quantidade  
        → Calcula o preço sem desconto.  
        → Na tabela, é a coluna “Valor sem desconto”.

    return valor_sem_desconto, valor_com_desconto  
        → Retorna os dois valores juntos.  
        → Na tabela, são as duas últimas colunas.

    ✅ Ou seja: a tabela é a explicação prática do código.  
    Ela mostra, com exemplos de quantidade e preço unitário, como cada condição do if/elif é aplicada e qual resultado a função retorna.
    """
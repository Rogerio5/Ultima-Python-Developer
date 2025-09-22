"""Você foi contratado (a) como programador (a) do Ultima-Bank, o melhor banco da América Latina!

O Ultima-Bank ainda é um banco novo, então alguns processos internos ainda estão sendo realizados de maneira manual, com muita papelada envolvida!

Para agilizar os processos internos, você foi encarregado (a) de desenvolver um sistema de cadastro de novos clientes utilizando Python!
Você entregará nesta tarefa apenas um protótipo para o cadastro de 2 clientes, e caso dê certo, expandiremos para todos os milhões de clientes do Ultima-Bank.

Os dados a serem salvos são:

Nome (String)
CPF (String)
Idade (Inteiro)
Dicas:

Você pode criar uma lista para adicionar todos os clientes;
Você pode usar um dicionário para armazenar cada cliente;
Você vai obter os dados pela entrada padrão (usando a função input()).
Extra (Opcional): Desenvolver utilizando classes.
Saída do seu programa:

Você deve mostrar a seguinte mensagem para cada cliente: print(“Cliente:”, cliente[“Nome”], “CPF:”, cliente[“CPF”], “Idade:”, cliente[“Idade”])
Por exemplo: Cliente: John Snow CPF: 963.125.345-78 Idade: 24
Mostre os cinco clientes, um após o outro.

Além disso, desenvolva um programa que receba dados de clientes e armazene-os em uma lista. A saída do seu programa será os dados formatados dos 2 clientes cadastrados."""

print("\nCadastro do cliente 1")
nome = input("Digite o nome: ")
cpf = input("Digite o CPF: ")
idade = int(input("Digite a idade: "))

cliente = {
    "Nome": nome,
    "CPF": cpf,
    "Idade": idade
}
cliente.append(cliente)

print("\nCadastro do cliente 2")
nome = input("Digite o nome: ")
cpf = input("Digite o CPF: ")
idade = int(input("Digite a idade: "))

cliente = {
    "Nome": nome,
    "CPF": cpf,
    "Idade": idade
}
cliente.append(cliente)

print("\nClientes cadastrados:")
for cliente in cliente:
    print("Cliente:", cliente["Nome"], "CPF:", cliente["CPF"], "Idade:", cliente["Idade"])

# Armazeno o nome do usuário
nome = input(str("Insira seu nome: "))
print("Olá, {}. Bem-vindo à sua calculadora." .format(nome))

# Solicito o primeiro número ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))

# Solicito o segundo número ao usuário
num2 = int(input("Digite o segundo número inteiro: "))

# Solicito o tipo de operação ao usuário
op = int(input("Qual o tipo de operação?"
               "\nEscreva 1 para + (adição)"
               "\nEscreva 2 para - (subtração)"
               "\nEscreva 3 para * (multiplicação)"
               "\nEscreva 4 para / (divisão)"
               "\n"))

# Apresento o resultado da conta segundo a operação selecionada
if op == 1:
    print("O resultado da sua conta é {}." .format(int(num1 + num2)))
elif op == 2:
    print("O resultado da sua conta é {}." .format(int(num1 - num2)))
elif op == 3:
    print("O resultado da sua conta é {}." . format(int(num1 * num2)))
elif op == 4:
    if num2 != 0:
        print("O resultado da sua conta é {}." .format(float(num1 / num2)))
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Tente novamente")

# Mensagem para sair
input("Aperte qualquer tecla para sair...")
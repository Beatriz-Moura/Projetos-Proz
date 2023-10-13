def calculadora(num1, num2, op): 
    if(op == 1):
      return  num1 + num2
    elif (op == 2):
        return  num1 - num2
    elif (op == 3):
        return  num1 * num2 
    elif (op == 4):
        return  num1 / num2

print("Escolha uma das seguintes operações")
print("1 - soma ")
print("2 - subtração ")
print("3 - multiplicação ")
print("4 - divisão ")
print("0 - sair ")

escolha = int(input("Digite a opção desejada: "))

while (escolha != 0):
     nume1 = int(input("Digite o primeiro número: "))
     nume2 = int(input("Digite o segundo número: "))
     if (escolha == 1):
         print(calculadora(nume1, nume2, 1))
     elif (escolha == 2):
         print(calculadora(nume1, nume2, 2))
     elif (escolha == 3):
         print(calculadora(nume1, nume2, 3))
     elif (escolha == 4):
         print(calculadora(nume1, nume2, 4))
     else :
         print("Essa opção nao existe ")
     print("Escolha uma das seguintes operações")
     print("1 - soma ")
     print("2 - subtração ")
     print("3 - multiplicação ")
     print("4 - divisão ")
     print("0 - sair ")
     escolha = int(input("Digite a opção desejada: "))
     
print("Operação Encerrada ")
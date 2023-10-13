def calculadora(num1, num2, op): 
    if(op == 1):
      resultado = num1 + num2
      return resultado
    elif(op == 2):
        resultado = num1 - num2
        return resultado
    elif (op == 3):
        resultado = num1 * num2
        return resultado
    elif (op == 4):
        resultado = num1 / num2
        return resultado
    else:
        print(0)
        
nume1 = int(input("Digite o primeiro número: "))
nume2 = int(input("Digite o segundo número: "))
ope = int(input("Digite a operação desejada: "))


operacao_matematica = calculadora(nume1, nume2, ope)
print(operacao_matematica)
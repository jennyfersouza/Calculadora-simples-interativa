n1 = 5
n2 = 2
operacao = 3

def calc(n1, n2, operacao) :
    if operacao == 1 :
        return n1 + n2
    elif operacao == 2 :
        return n1 - n2
    elif operacao == 3 :
        return n1 * n2
    elif operacao == 4 :
        return n1 / n2
    else :
        return 0
    
resultado = calc(n1,n2,operacao)
print(resultado)

executar = True

while (executar == True) :
    print ("O que você deseja fazer?")
    print ("1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão, 0: Sair.")
    operacao = int(input())
    if (operacao < 0) or (operacao > 4) :
        print("Opção inexistente.")
    elif (operacao == 0) :
        executar = False
    else:
        print ("Insira o primeiro número:")
        n1 = int (input())
        print ("Insira o segundo número:")
        n2 = int(input())
        resultado = calc(n1, n2, operacao)
        print("O resultado é:", resultado)
    
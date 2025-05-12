import os


def obter_numero():
    return float()(input("Digite um número: "))

def continuar_calculo():
    x = int(input("\nDigite 0 para continuar "))
    return x

x = 0  
while x == 0:
    os.system("cls")
    print("------------------------")
    print("\nBEM VINDO A CALCULADORA!")
    print("Qual operação você quer fazer? \n")
    print("Adição digite: 1\nSubtração digite: 2\nMultiplicação digite: 3\nDivisão digite: 4\n")
    print("------------------------")

    inf = int(input("Digite a operação desejada: "))  

    if inf == 1:
        num = obter_numero()
        num1 = obter_numero()
        print(f"A soma deles é: {num + num1}")

    elif inf == 2:
        num = obter_numero()
        num1 = obter_numero()
        print(f"A subtração deles é: {num - num1}")

    elif inf == 3:
        num = obter_numero()
        num1 = obter_numero()
        print(f"A multiplicação deles é: {num * num1}")

    elif inf == 4:
        num = obter_numero()
        num1 = obter_numero()
        if num1 != 0:
            print(f"A divisão deles é: {num / num1}")
        else:
            print("Erro: Não é possível dividir por zero!")

    else:
        print("Opção inválida!")

    
    x = continuar_calculo()  
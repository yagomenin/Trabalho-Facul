num = float(input(" Escolha o primeiro numero "))
num_2 = float(input(" Escolha o segundo numero "))
choose = input("Escolha sua operação, M = +, ME = -, D = *, DI * / ")
resultado = num + num_2
resultado_2 = num - num_2
resultado_3 = num * num_2
resultado_4 = num / num_2
if choose == "M":
    print(f'o resultado é {resultado}')
    if resultado % 2 == 0:
        print("par")
    else:
        print("Impar")
    if resultado > 0:
        print( "positivo")
    else:
        print( "negativo")
    if resultado == int(resultado):
        print(" Inteiro")
    else:
        print("Decimal")
elif choose == "ME":
    print(f'o resultado é {resultado_2}')
    if resultado_2 % 2 == 0:
        print("par")
    else:
        print("Impar")
    if resultado_2 > 0:
        print("positivo")
    else:
        print("negativo")
    if resultado_2 == int(resultado_2):
        print(" Inteiro")
    else:
        print("Decimal")
elif choose == "D":
    print(f'o resultado é {resultado_3}')
    if resultado_3 % 2 == 0:
        print("par")
    else:
        print("Impar")
    if resultado_3 > 0:
        print("positivo")
    else:
        print("negativo")
    if resultado_3 == int(resultado_3):
        print(" Inteiro")
    else:
        print("Decimal")
elif choose == "DI":
    print(f'o resultado é {resultado_4}')
    if resultado_4 % 2 == 0:
        print("par")
    else:
        print("Impar")
    if resultado_4 > 0:
        print("positivo")
    else:
        print("negativo")
    if resultado_4 == int(resultado_4):
        print(" Inteiro")
    else:
        print("Decimal")
else:
    print(' voce n escolheu uma das operações possiveis seu Apedeuta')






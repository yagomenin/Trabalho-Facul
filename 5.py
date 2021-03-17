#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litr
Litro_alcool_Gasolina = float(input("Quanto L quer de Alcool ou Gasolina "))
litro_alcool = (1.90 * Litro_alcool_Gasolina)
litro_gasolina = (2.50 * Litro_alcool_Gasolina)
choose = input("escolha A_Alcool ou G_gasolinha ")
if choose == "A":
    if Litro_alcool_Gasolina < 20:
        print(" Desconto de 3% ao litro")
        print(f'Sua conta é de {litro_alcool - ((1.90 * 0.03) * Litro_alcool_Gasolina) }')
    elif Litro_alcool_Gasolina > 20:
        print(" Desconto de %5 ao litro")
        print(f' Sua conta é de {litro_alcool - ((1.90 * 0.05) * Litro_alcool_Gasolina)}')
if choose == "G":
    if Litro_alcool_Gasolina < 20:
        print("O desconto é de 4% ")
        print(f'Sua conta é de {litro_gasolina - ((2.50 * 0.04) * Litro_alcool_Gasolina)}')
    elif Litro_alcool_Gasolina > 20:
        print(" Desconto de %6 ao litro")
        print(f' Sua conta é de {litro_gasolina - ((2.50 * 0.06) * Litro_alcool_Gasolina)}')
else:
    print("Não temos esse combustivel seu Apedeuta")




print("Bem vindo a frutaria!!!!!")
choose = input(" Voce comprou morango_Mo ou maçãs_M, ou ambas as frutas_mm ( M, mo e mm) ")
if choose == "M":
    Maca = float(input("Quantos kgs voce comprou em frutas? "))
    maca_desc = 1.50 * Maca
    valor_da_compra_Ma = Maca * 1.80 or maca_desc
    if Maca <= 5:
        print(f' Sua compra foi de {Maca * 1.80}')
    elif Maca > 5 and Maca <= 8:
        print('Voce ganhou um desconto de 30 centavos')
        print(f'Sua compra foi de {maca_desc}')
    elif Maca > 8 or valor_da_compra_Ma > 25:
        Maca_10 = Maca * 0.10
        print('voce ganha o desconto de 30 centavos + 10%')
        print(f'sua compra foi de {maca_desc - Maca_10}')
if choose == "Mo":
    morango = float(input("Quantos kgssss voce comprou em frutas"))
    morango_desc = 2.20 * morango
    valor_da_compra_Mo = morango * 2.50 or morango * morango_desc
    if morango <=5:
        print(f' Sua compra foi de {morango * 2.50}')
    elif morango > 5 and morango <=8:
        print('Voce ganhou um desconto de 20 centavos')
        print(f'Sua compra foi de {morango_desc}')
    elif morango > 8 or valor_da_compra_Mo:
        morango_10 = morango * 0.10
        print('voce ganha o desconto de 30 centavos + 10%')
        print(f'sua compra foi de {morango_desc - morango_10}')
if choose == 'mm':
    maca_morango = float(input("Quantos kgs de maca voce comprou "))
    morango_maca = float(input("Quantos kgs de morango voce comprou "))
    valor_da_compra_ma= maca_morango * 1.80 + morango_maca * 2.50
    valor_da_compra_desc_MO = maca_morango * 1.80 + morango_maca * 2.20
    valor_da_compra_desc_Ma = maca_morango * 1.50 + morango_maca * 2.50
    valor_da_compra_desc_Ma_Mo = maca_morango * 1.50 + morango_maca * 2.20
    if maca_morango <= 5 and morango_maca <= 5:
        if maca_morango + morango_maca > 8:
            print(f'voce ganhou 10% de desconto, e sua compra fica ')
            print(f'{(morango_maca * 2.50 + maca_morango * 1.80) - valor_da_compra_ma * 0.10}')
        else:
            print(f' o valor da sua compra é de {maca_morango * 1.80 + morango_maca * 2.50}')
    elif maca_morango <= 5 and morango_maca > 5:
        print('Ganhou desconto ao comprar mais de 5 kg de morango. ')
        if maca_morango + morango_maca > 8 or valor_da_compra_desc_MO > 25:
            print('Voce ganhou 10% de desconto ao compra mais de 8 kg de frutas, e sua compra fica ')
            print(f'{(valor_da_compra_desc_MO) - (valor_da_compra_desc_MO * 0.10) }')
        else:
            print(f' O valor de sua compra é de{valor_da_compra_desc_MO} ')
    elif maca_morango > 5 and morango_maca <=5:
        print('Ganhou desconto ao comprar mais 5 Kg de maça!')
        if maca_morango + morango_maca > 8 or valor_da_compra_desc_Ma > 25:
            print('voce ganhou 10% de desconto ao compra mais de 8 kg de frutas, e sua compra fica ')
            print(f'{(valor_da_compra_desc_Ma) - (valor_da_compra_desc_Ma * 0.10)}')
        else:
            print(f'O valor de sua compra é de {valor_da_compra_desc_Ma}')
    elif maca_morango > 5 and morango_maca > 5:
        print('Voce ganhou desconto em ambas as frutas')
        if maca_morango + morango_maca > 8 or valor_da_compra_desc_Ma_Mo > 25:
            print('Voce ganhou de 10% de desconto ao comprar mais de 8 kgs de frutas, e sua compra fica')
            print(f'{(valor_da_compra_desc_Ma_Mo - (valor_da_compra_desc_Ma_Mo * 0.10))} ')
        else:
            print(f'O valor de sua compra é de {valor_da_compra_desc_Ma_Mo}')



















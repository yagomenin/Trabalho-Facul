r_1 = input("Telefonou para a vitima ? (s/n)? ")
r_2 = input("Esteve no local do crime (s/n)? ")
r_3 = input("Mora perto da vitima? (s/n)? ")
r_4 = input("Devia para a vitima (s/n)? ")
r_5 = input("Ja trabalhou com a vitima (s/n)? ")

r = 0

if r_1 == 's':
    r = r + 1
if r_2 == 's':
    r = r + 1
if r_3 == 's':
    r = r + 1
if r_4 == 's':
    r = r + 1
if r_5 == 's':
    r = r + 1
if r == 0:
    print(' Não é suspeito')
elif r == 2 or r == 3:
    print(' Considerado um suspeito pelo Detetive')
elif r == 4:
    print(' Complice do crime cometido')
elif r == 5:
    print(' Achamos o Assasssino !!!!!')


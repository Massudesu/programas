#todos numeros divisiveis por 3 em intervalo qualquer

i = int(input("Numero do começo: "))
o = int(input("Numero do final:  "))

l = list(range(i, o))

for u in l:
    p = u % 3
    if p == 0:
        print(str(u))




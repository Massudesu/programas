

c = int(input("quantas pessoa na fila: "))
c1 = int(input("quantas pessoas passaram no caixa 1:"))
c2 = int(input("quantas pessoas passaram no caixa 2:"))
c3 = int(input("quantas pessoas passaram no caixa 3:"))
t1 = float(input("tempo total do caixa 1: "))
t2 = float(input("tempo total do caixa 2: "))
t3 = float(input("tempo total do caixa 3: "))

tt1 = t1 / c1
tt2 = t2 / c2
tt3 = t3 / c3

r= c1 + c2 + c3

if r > c:
    print('A soma de pessoas para cada fila não pode ser maior do que a quantidade total de pessoas na fila.')

elif r < c:
    print('A soma pessoas para cada fila não pode ser menor do que a quantidade total de pessoas na fila.')

else:
    print(f'A média do tempo de atendimento do caixa 1 foi de {tt1} minutos por pessoa, a do caixa 2 foi {tt2} e a do caixa 3 foi de {tt3}')
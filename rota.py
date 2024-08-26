#n = numero de rotas
#rr = rota + rapida
#trr = tempo rota + rapida
#rd = rota + demorada
#trd = tempo da rota + demorada
#rr = rota + rapida
#t = trechos
#d = distancia
#vm = velocidade media
#tr = tempo da rota
n = int(input("Quantas rotas?  "))

rd = 0
trd = 0
rr = 0
trr = float

for i in range(n):
    print(f"Rota {i+1}:")
    t = int(input("Quantos trechos nesta rota? "))
    tr = 0

    for j in range(t):
        d = float(input(f"Distância do trecho {j+1} (km)? "))
        vm = float(input(f"Velocidade média do trecho {j+1} (km/h)? "))
        tr += d / vm

    if tr > trd:
        trr = tr
        rd = i + 1

    if tr < trr:
        trr = tr
        rr = i + 1

print("A rota mais demorada é a rota " + str(rd) + " com um tempo de " + str(trd) + " horas.")
print("A rota mais rápida é a rota " + str(rr) + " com um tempo de " + str(trr) + " horas.")
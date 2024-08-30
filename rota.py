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
#mp = media podeirada
#vmp = velocidade media pondeirada
n = int(input("Quantas rotas?  "))

rd = 0
trd = float('inf')
#rr = 0
trr = float('inf')
mp = []

for i in range(n):
    print(f"Rota {i+1}:")
    t = int(input("Quantos trechos nesta rota? "))
    tr = 0
    dt = 0

    for j in range(t):
        d = float(input(f"Distância do trecho {j+1} (km)? "))
        vm = float(input(f"Velocidade média do trecho {j+1} (km/h)? "))
        tr += d / vm
        dt += d
    vmp = dt / tr
    mp.append(vmp)

    if tr < trd:  
        trd = tr
        rd = i + 1

if rd > 0:
    print(f"A rota mais rápida é a rota {rd}")
else:
    print("Não foi possível determinar a rota mais rápida.")
for i in range(len(mp)):
    vmp = mp[i]
    print(f"A média ponderada da rota {i+1} é {vmp} km/h")
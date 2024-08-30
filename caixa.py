c = int(input("Quantos caixas: "))

for i in range(c):
    print(f"Caixa {i+1}:")
    c1 = int(input(f"Quantas pessoas foram no caixa {i + 1}: "))
    tc = 0
    for j in range(c1):
        t = float(input(f"Qual o tempo total de atendimento do caixa {j+1} (em minutos): "))
        tc = t / c1
        break
    print(f"O tempo medio de atendimentodo caixa {i + 1} é: {tc} minutos")
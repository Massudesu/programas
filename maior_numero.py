n = int(input("Quantidade de numeros na sequencia: "))

p = 0
p = [int(input("Insira o número: " + str(o+1) + ": ")) for o in range(n)]

maior = 0
for m in p:
    if m > maior:
        maior = m

print("A sequência é: ", p)
print("O maior número é: ", maior)
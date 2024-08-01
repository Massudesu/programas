#enesimo termo da sequencia de Fibonacci

n = int(input("Enesimo termo: "))

if n <= 0:
    print("Precisa ser positivo e inteiro!!")
    print("=============================================")

elif n == 1:
    print("O " + str(n) + " da sequência de Fibonacci é: 0")
    print("=============================================")

elif n == 2:
    print("O " + str(n) + " da sequência de Fibonacci é: 1")
    print("=============================================")
else:
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    print("O " + str(n) + " da sequência de Fibonacci é: " + str(b))
    print("=============================================")
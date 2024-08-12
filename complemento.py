#pegar proximo numero par depois do ultimo primo divisivel por 3.

i = int(input("Numero do começo: "))
o = int(input("Numero do final:  "))

l = list(range(i, o))

for u in l:
    p = u % 3
    if p == 0:
        print(str(u))
        
        
        n = u + 1
        while n % 2 != 0:
            n += 1
            

        r = u * n
        print(str(u) + " * " + str(n) + " = " + str(r))

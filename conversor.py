#c = celsius
#f = fahrenheit
#k = kelvin
#o = opção
#t = true,false
print("Escolha uma das opções: ")
t = True
while t:
    print("1. De Celsius para fahrenheit")
    print("2. De Fahrenheit para celsius")
    print("3. De Celsius para kelvin")
    print("4. De kelvin para celsius")
    print("5. De Fahrenheit para kelvin")
    print("6. De Kelvin para fahrenheit")
    print("7. Terminar")

    o = int(input("Digite a opção: "))
    if o == 1:
        c = float(input("Digite a temperatura em Celsius: "))
        f = (c * 1.8) + 32
        print(str(c)+ "°C é igual a " + str(f) + "°F")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    elif o == 2:
        f = float(input("DIgite a temperatura em Fahrenheit: "))
        c = (f -32) * 5/9
        print(str(f)+ "F é igual a " + str(c) + "°C")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    elif o == 3:
        c = float(input("Digite a temperatura em Celsius: "))
        k = (c + 273)
        print(str(c)+ "°C é igual a " + str(k) + "K")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        

    elif o == 4:
        k = float(input("Digite a temperatura em Kelvin: "))
        c = (k - 273)
        print(str(k)+ "K é igual a " + str(c) + "°C")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    elif o == 5:
        f = float(input("Digite a temperatura em Fahrenheit: "))
        k = (f -32) * 5/9 + 273
        print(str(f)+ "°F é igual a " + str(k) + "K")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    elif o == 6:
        k = float(input("Digite a temperatura em Kelvin: "))
        f = (k -273) * 9/5 + 32
        print(str(k)+ "K é igual a " + str(f) + "°F")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    elif o == 7:
        t = False
        
    else:
        print("Opção inválida.")
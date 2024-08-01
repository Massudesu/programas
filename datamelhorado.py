#Importar o datetime
from datetime import datetime

#pedir informações de data de nascimento
f = (input("Qual seu nome?: "))
g = (input("Qual o seu sobrenome?: "))
d = int(input('Insira dia de nascimento: '))
m = int(input('Insira mes de nascimento: '))
a = int(input('Insira ano de nascimento: '))


#definir variaveis antes 
dn = datetime(a,m,d)
da = datetime.now()

#separar ano, mes e dia
IA = da.year - dn.year
IM = da.month - dn.month
ID = da.day - dn.day

#se maior ou menor de 18 anos
if IA < 18 or (IA == 18 & IM == 0 & ID < 0):
    print("Erro você é menor de idade")
    print("Volte quando tiver +18 anos")
    
else:
    print("acesso liberado")
    print("Você é maior de idade")
#Mostrar a idade completa
print(str(f)+" "+str(g)+ ", você tem "+ str(IA)+ "anos, " + str(IM)+"meses, " + str(ID)+ "dias")
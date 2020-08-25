#Faça um Programa que peça dois números e imprima o maior deles.
lista = []

for n in range(0,int(2)): 
    lista.append(int(input("Digite o número: ")))
    
print ("Maior número é: ", max(lista))    
    

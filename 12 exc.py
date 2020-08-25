#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input("Qual seu sexo? (F)-Feminino, (M)-Masculino: ").upper())
if sexo == "f":
    print("feminino")
elif sexo == 'F':
    print("masculino")
else:
    print("Sexo Inválido.")

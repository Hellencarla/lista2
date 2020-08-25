#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Informe uma letra:").upper())
if letra == "a" or "e" or "i" or "o" or "u":
   print("É uma vogal")
else:
   print("É uma consoante")

import os
import time
 
os.system("cls")

soma = 0
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):

    nota = float(input("Digite sua nota: "))
    soma += nota
    
media = soma / QUANTIDADE_NOTAS
print(f"Media: {media}")
import os
import time
 
os.system("cls")

soma = 0 
QUANTIDADES_NOTAS = 3

for i in range(QUANTIDADES_NOTAS):
    nota = int(input("Digite sua nota: "))
    soma += nota

media = soma / QUANTIDADES_NOTAS

print(f"Media: {media}")

if media >= 7:
    print("APROVADO")
if 4 <= media < 7:
    print("RECUPERAÇÃO")
if media < 4:
    print("REPROVADO")

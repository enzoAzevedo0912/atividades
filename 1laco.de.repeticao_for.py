import os
import time
 
os.system("cls")

num = int(input("Digite um numero: "))

for i in range(1,11):
    resultado = num * i
    print("{} X {} = {}". format(num, i, resultado))

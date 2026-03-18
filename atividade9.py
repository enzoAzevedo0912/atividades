import os 
os.system("cls")

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
terceira_nota = float(input("Digite sua terceira nota: "))
QUANTIDADE = 2

for i in range(QUANTIDADE):
    nota = float(input("Digite sua nota: "))
    if nota >= 0 and nota <= 10:
        nota +=1
        
else:
    print("Tente novamente")
if nota > 7:
    resultado = "APROVADO!!"
elif nota < 6.9:
    resultado = "RECUPERAÇÃO!!"
elif nota < 5:
    resultado = "REPROVADO!!"
    
print(f"Voce esta {resultado}:")
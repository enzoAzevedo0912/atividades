import os 

os.system("cls")

def ler_nota(ordem):
    while True:
        try:
            nota = float(input(f"Digite a {ordem}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

# 1. Leitura das notas com validação
nota1 = ler_nota(1)
nota2 = ler_nota(2)
nota3 = ler_nota(3)

# 2. Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# 3. Verificação do status do aluno
print(f"\nMédia final: {media:.2f}")

if media >= 7:
    print("Situação: APROVADO")
elif 5 <= media < 7:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")
import os 
os.system("Cls")

# CRIANDO UM VETOR.
vetor_notas = []

# ADICIONANDO 3 NOTAS.
for i in range(3):
    nota = float(input(" Digite uma nota."))
    vetor_notas.append(nota)
    
# EXIBINDO AS NOTAS INFORMADAS.
for i in range(3):
    print(f"Nota: {vetor_notas[i]}")
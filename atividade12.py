import os
os.system("Cls")

# INICIALIZAÇÃO DAS VARIÁVEIS DE CONTROLE

total_familias = 0
soma_salarios = 0
soma_filhos = 0 
maior_salario = 0
menor_salario = float('inf')

while True:
    print("\n--- MENU ---")
    print("1 | Adicionar família")
    print("2 | Sair e exibir resultados")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1': 
        # ENTRADA DE DADOS
        salario = float(input("Digite o salário da família: R$ "))
        filhos = float(input("Digite o número de filhos?: "))
        
        # PROCESSAMENTO DE DADOS 
        total_familias += 1
        soma_salarios += salario
        soma_filhos += filhos
        
        # VERIFICAÇÃO DE MAIOR E MENOR SALÁRIO 
        if salario > maior_salario:
            maior_salario = salario
            
        if salario < menor_salario:
            menor_salario = salario
            
    elif opcao == '2':
        # FINALIZA O LOOP
        break
    else: 
        print("Opção inválida! Tente novamente.")
        
    # EXIBIÇÃO DOS RESULTADOS (APENAS SE HOUVER FAMÍLIAS CADASTRADAS)
    if total_familias > 0:
        media_salario = soma_salarios / total_familias
        media_filhos = soma_filhos / total_familias
        
    print("\n" + "="*30)
    print("      RESULTADO DA PESQUISA")
    print("="*30)
    print(f"a) Total de famílias: {total_familias}")
    print(f"b) Média do salário: R$ {media_salario:.2f}")
    print(f"c) Média do número de filhos: {media_filhos:.1f}")
    print(f"d) Maior salário: R$ {maior_salario:.2f}")
    print(f"e) Menor salário: R$ {menor_salario:.2f}")
else:
    print("\nNenhuma família foi registrada.")
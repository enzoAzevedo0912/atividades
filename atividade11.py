import os

os.system("cls")

# Tabela de preços (Cardápio)
cardapio = {
    1: {"prato": "Picanha", "valor": 25.00},
    2: {"prato": "Lasanha", "valor": 20.00},
    3: {"prato": "Strogonoff", "valor": 18.00},
    4: {"prato": "Bife Acebolado", "valor": 15.00},
    5: {"prato": "Pão com ovo", "valor": 5.00}
}

total_conta = 0
pedidos = []

print("--- BEM-VINDO AO RESTAURANTE ---")

while True:
    # Exibição do Menu
    print("\nMENU:")
    for codigo, info in cardapio.items():
        print(f"{codigo} - {info['prato']}: R$ {info['valor']:.2f}")
    
    # Escolha do prato
    try:
        escolha = int(input("\nDigite o código do prato desejado: "))
        
        if escolha in cardapio:
            prato_escolhido = cardapio[escolha]
            total_conta += prato_escolhido['valor']
            pedidos.append(prato_escolhido['prato'])
            print(f"Adicionado: {prato_escolhido['prato']}")
        else:
            print("Código inválido! Tente novamente.")
            continue
            
        # Pergunta se deseja continuar
        continuar = input("Deseja escolher outro prato? (S/N): ").strip().upper()
        if continuar == 'N':
            break
            
    except ValueError:
        print("Erro: Por favor, digite apenas números para o código.")

# Resumo Final
print("\n" + "="*30)
print(f"RESUMO DO PEDIDO: {', '.join(pedidos)}")
print(f"VALOR TOTAL A PAGAR: R$ {total_conta:.2f}")
print("="*30)


import os

os.system("cls")

login_correto = ("Enzo")
senha_correta = ("1443")
contador = 0 

for i in range(3):
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    login_esta_correto = login =login_correto
    senha_esta_correta = senha =senha_correta
    contador += 1
    
    if contador == 3:
        break
    
if login_esta_correto and senha_esta_correta:
    print("Bem-vindo ao sistema!!")
else:
    print("Login ou senha incorreta")
    print("Tente novamente... \n")

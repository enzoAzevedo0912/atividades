import os
os.system("cls")

login_correto = "enziinhoo@gmail.com"
senha_correta = "enzo1234"

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    login_esta_correto = login ==login_correto
    senha_esta_correta = senha ==senha_correta
    
    if login_esta_correto and senha_esta_correta:
        print("Bem-vindo ao sistema!!")
        break
    else:
        print("Login ou senha incorreta")
        print("Tente novamente... \n")
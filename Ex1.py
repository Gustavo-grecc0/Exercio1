import re

def validar_senha(senha):
    
    if not re.search(r'[A-Z]', senha) or not re.search(r'[a-z]', senha) or not re.search(r'[0-9]', senha):
        return False
    
    
    if re.search(r'[^a-zA-Z0-9]', senha):
        return False
    
    
    if len(senha) < 6 or len(senha) > 32:
        return False
    
    return True

while True:
    try:
        senha = input()
        if validar_senha(senha):
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break

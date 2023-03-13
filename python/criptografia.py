

def criptografar(senha):
    s_c = ""
    for i in senha:
        s_c = s_c + chr(ord(i)+15)

    return s_c

def iniciar():
    print(34*"*")
    print(7*"*"+"Cadastro de Usuários"+7*"*")
    print(34*"*")
    print("Siga as instruções para completar o cadastro.")


def cadastrar(usuario, senha):
    cad_usu = usuario
    cad_senha = criptografar(senha)
    return print(f"Usuário Cadastrado:{cad_usu}\nSenha Cadastrada: {cad_senha}")

iniciar()

usu_usu = str(input("Digite o seu usuário\n"))
usu_senha = str(input("Digite sua senha\n"))

cadastrar(usu_usu, usu_senha)

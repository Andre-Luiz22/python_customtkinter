import customtkinter as ctk
from criptografia import criptografar





# ----------------- Configurações da Janela -----------------------
root = ctk.CTk()
root.geometry("700x350")
root.configure(fg_color= "#141110")
root.resizable(False, False)
root.title("Cadastro")
# ----------------- Titulo do "App" -------------------------------

titulo_app = ctk.CTkLabel(root, text="Cadastro de Usuários", font=("Cambria bold", 20), text_color="#dedede")
titulo_app.pack()

desc_app = ctk.CTkLabel(root, text="Digite usuário e senha para completar o cadastro", font=("Cambria",15), text_color="#dedede")
desc_app.pack(pady=40)

usuario = ctk.CTkEntry(root, width= 200, height=30, placeholder_text="usuário", justify="center", border_width= 1, border_color="#000000")
usuario.pack(pady= 0)

senha = ctk.CTkEntry(root, width= 200, height=30, placeholder_text="senha", justify="center", border_width= 1, border_color="#000000", show="*")
senha.pack(pady=20)

def pegar():
    senha_dig = criptografar(senha.get())
    usuario_dig = usuario.get()
    return print(usuario_dig,senha_dig)


button = ctk.CTkButton(root, width= 125, height=30, text="Cadastrar", fg_color="#151311", hover_color="#14100C", border_width= 1, border_color="#000000", command=pegar)
button.pack(pady=20)









root.mainloop()
import customtkinter as ctk




# ----------------- Configurações da Janela -----------------------
root = ctk.CTk()
root.geometry("700x350")
root.configure(fg_color= "#141110")
root.resizable(False, False)
root.title("Cadastro")
# ----------------- Titulo do "App" -------------------------------

titulo_app = ctk.CTkLabel(root, text="Cadastro de Usuários", font=("Cambria bold", 20), text_color="#dedede").pack()

desc_app = ctk.CTkLabel(root, text="Digite usuário e senha para completar o cadastro", font=("Cambria",15), text_color="#dedede").pack(pady=40)

usuario = ctk.CTkEntry(root, width= 200, height=30, placeholder_text="usuário", justify="center", border_width= 1, border_color="#000000").pack(pady= 0)

senha = ctk.CTkEntry(root, width= 200, height=30, placeholder_text="senha", justify="center", border_width= 1, border_color="#000000").pack(pady=20)

def botao_com():
    print(senha.get())
    print(usuario.get())


button = ctk.CTkButton(root, width= 125, height=30, text="Cadastrar", fg_color="#151311", hover_color="#14100C", border_width= 1, border_color="#000000", command=botao_com).pack()







root.mainloop()
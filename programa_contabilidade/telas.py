import customtkinter as ctk

#-------------- Criação e parametros da tela------------
root = ctk.CTk()
root.geometry("1000x550")
root._set_appearance_mode("Dark")
root.configure(fg_color = "#121D3B")
root.resizable(False, False)
root.title("App Situação Financeira")

#------------- Criação dos frames e dos titulos -------------------

frame_situacao = ctk.CTkFrame(root, width = 588, height = 475, fg_color = "#526087" )# criação do frame _sitaacao
frame_situacao.place(x = 10, y = 65)# posição do frame situação

frame_valores = ctk.CTkFrame(root, width = 382, height = 475, fg_color= "#526087")# criação dos frames valores
frame_valores.place(x = 608, y = 65)# posição dos frames valores

frame_titulo = ctk.CTkFrame(root, width = 980, height = 45, fg_color = "#526087")# criação do frme do titulo
frame_titulo.place(x = 10, y = 10)# posição do frame titulo

titulo_app = ctk.CTkLabel(frame_titulo, text = "APP SITUAÇÃO FINANCEIRA DE JANEIRO", font=("Verdana bold" , 25), width = 960, height = 25, fg_color="transparent", bg_color = "transparent" )# criação do tutulo
titulo_app.place(x = 10, y = 10)# posição do titulo

frame_situacao_titulo = ctk.CTkFrame(frame_situacao, width = 568, height = 45, fg_color = "transparent")# criação do frame do titulo situação
frame_situacao_titulo.place(x = 10, y = 10)# posição do frame do titulo situação

titulo_situacao = ctk.CTkLabel(frame_situacao_titulo, text = "SITUAÇÃO", font=("Verdana bold" , 25), width = 548, height = 25, fg_color="transparent")# criação do titulo situação
titulo_situacao.place(x = 10, y = 10)#posição do titulo situação

frame_valores_titulo = ctk.CTkFrame(frame_valores, width = 362, height = 45, fg_color = "transparent")# criação do frame do titulo de valores
frame_valores_titulo.place(x = 10, y = 10)#criação do frame do titulos de valores

titulo_valores = ctk.CTkLabel(frame_valores_titulo, text = "VALORES", font = ("Verdana bold", 25), width = 342, height = 25, fg_color = "transparent")# criação do titulo de valores
titulo_valores.place(x = 10, y = 10)# posição do titulo de valores

frame_inf_situação = ctk.CTkFrame(frame_situacao, width = 568, height = 410, fg_color = "#343333")# Criação do Frame das informaçoes da situação
frame_inf_situação.place(x = 10, y = 55)# Posição do frame de informações da situação

frame_inf_valores = ctk.CTkFrame(frame_valores, width = 362, height = 410, fg_color = "#343333")#  Criação do Frame de informaçoes dos valores
frame_inf_valores.place(x = 10, y = 55)# Posição do frame de informaçoes dos valores

# ---------------------Criação das entradas da caixa de valores---------------------

opcoes_valores = ctk.CTkComboBox(frame_inf_valores, width = 140, height =25 ,values = ["Contas Variáveis", "Valores a Receber"], justify = "center", fg_color = "#47413d", text_color = "#FFFFFF", dropdown_fg_color = "#47413d", dropdown_text_color = "#FFFFFF", dropdown_hover_color = "#3c3b3b", border_width = 1, border_color = "#1d1e1f", button_color = "#1d1e1f", state = "readonly")# Criação da caixa de opçoes da parte de valores
opcoes_valores.set("Escolher opções")# Texto que aparece antes de escolher um opção da caixa de valores
opcoes_valores.place(x = 111, y = 10)# Posição da caixa de opções dentro de valores



#----------------Criação das saidas em Situação--------------------------

tab = ctk.CTkTabview(frame_inf_situação, width = 40, fg_color="#343333", segmented_button_fg_color = "#1d1e1f", segmented_button_unselected_color = "#47413d",text_color = "#FFFFFF", segmented_button_selected_color = "#3c3b3b", segmented_button_unselected_hover_color = "#1d1e1f" ,segmented_button_selected_hover_color = "#3c3b3b", state = "normal")
tab.add("Planilhas")
tab.add("Gráficos")
tab.place(x = 214, y = 0)
tab.tab("Planilhas")



root.mainloop()
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from view import *

# Configurações da janela principal
janela = Tk()
janela.title("Formulário de Consultoria")
janela.geometry('1043x453')
janela.configure(background="#e9edf5")
janela.resizable(width=FALSE, height=FALSE)

# Frames
frameCima = Frame(janela, width=310, height=50, bg="#4fa882", relief="flat")
frameCima.grid(row=0, column=0)
frameBaixo = Frame(janela, width=310, height=403, bg="#feffff", relief="flat")
frameBaixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
frameDireita = Frame(janela, width=588, height=403, bg="#feffff", relief="flat")
frameDireita.grid(row=0, column=1, rowspan=2, pady=0, padx=1, sticky=NSEW)

# Cabeçalho
Label(frameCima, text="Formulário de Consultoria", anchor=NW, font=('Ivy 13 bold'), bg="#4fa882", fg="#feffff").place(x=10, y=20)

# Funções de interação com o banco de dados
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    dia = cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()
    
    lista_inserir = [nome, email, telefone, dia, estado, assunto]
    
    if nome == '':
        messagebox.showerror('Erro', 'Preencha todos os campos')
    else:
        inserir_form(lista_inserir)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')
        mostrar()

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')
        
        e_nome.insert(0, treev_lista[1])
        e_email.insert(0, treev_lista[2])
        e_tel.insert(0, treev_lista[3])
        cal.set_date(treev_lista[4])
        e_estado.insert(0, treev_lista[5])
        e_assunto.insert(0, treev_lista[6])
        
        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_tel.get()
            dia = cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()
            
            lista_atualizar = [nome, email, telefone, dia, estado, assunto, valor]
            
            if nome == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
            else:
                atualizar_form(lista_atualizar)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')
                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_tel.delete(0, 'end')
                cal.delete(0, 'end')
                e_estado.delete(0, 'end')
                e_assunto.delete(0, 'end')
                botao_confirmar.destroy()
                mostrar()
        
        botao_confirmar = Button(frameBaixo, command=update, text="Confirmar", width=10, height=1, bg="#4fa882", fg="#feffff", font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
        botao_confirmar.place(x=105, y=380)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        deletar_form([valor])
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')
        mostrar()
        
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

# Widgets do formulário
Label(frameBaixo, text="Nome *", height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d").place(x=10, y=10)
e_nome = Entry(frameBaixo, width=45, justify='left', relief="solid")
e_nome.place(x=15, y=40)

Label(frameBaixo, text="Email *", height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d").place(x=10, y=70)
e_email = Entry(frameBaixo, width=45, justify='left', relief="solid")
e_email.place(x=15, y=100)

Label(frameBaixo, text="Telefone *", height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d").place(x=10, y=130)
e_tel = Entry(frameBaixo, width=45, justify='left', relief="solid")
e_tel.place(x=15, y=160)

Label(frameBaixo, text="Data da Consulta *", height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d").place(x=10, y=190)
cal = DateEntry(frameBaixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
cal.place(x=15, y=220)

Label(frameBaixo, text="Estado da Consulta *", height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d").place(x=160, y=190)
e_estado = Entry(frameBaixo, width=20, justify='left', relief="solid")
e_estado.place(x=160, y=220)

Label(frameBaixo, text="Consulta sobre *", height=1, anchor=NW, font=('Ivy 10 bold'), bg="#feffff", fg="#403d3d").place(x=10, y=260)
e_assunto = Entry(frameBaixo, width=45, justify='left', relief="solid")
e_assunto.place(x=15, y=290)

# Botões do formulário
Button(frameBaixo, command=inserir, text="Inserir", width=10, height=1, bg="#038cfc", fg="#feffff", font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE).place(x=15, y=340)
Button(frameBaixo, command=atualizar, text="Atualizar", width=10, height=1, bg="#4fa882", fg="#feffff", font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE).place(x=105, y=340)
Button(frameBaixo, command=deletar, text="Deletar", width=10, height=1, bg="#ef5350", fg="#feffff", font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE).place(x=190, y=340)

# Tabela para exibir os dados
def mostrar():
    list_header = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Estado', 'Sobre']
    df_list = selecionar_form()
    
    global tree
    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)
    
    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in df_list:
        tree.insert('', 'end', values=item)
        
mostrar()
janela.mainloop()
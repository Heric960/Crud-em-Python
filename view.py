import sqlite3 as lite

# Criando conexão
con = lite.connect('form.db')

# Inserir formulario
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Deletar formulario
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Formulario WHERE id=?"
        cur.execute(query, i)

# Atualizar formulario
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)

# Selecionar categoria
def selecionar_form():
    lista_form = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Formulario")
        rows = cur.fetchall()
        for row in rows:
            lista_form.append(row)
    return lista_form
import mysql.connector
from tkinter import *

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dani090707*',
    database='dbcrud',
)
cursor = conexao.cursor()

# Funções CRUD
def create():
    nome_produto = entry_nome_produto.get()
    preco_produto = float(entry_preco_produto.get())
    comando = f'INSERT INTO vendas (nome_produto, preco_produto) VALUES ("{nome_produto}", {preco_produto})'
    cursor.execute(comando)
    conexao.commit()  # Edita o banco de dados
    label_resultado.config(text="Produto adicionado com sucesso!")
    limpar_campos()

def read():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # Lê o banco de dados
    resultado_texto = '\n'.join([f"ID: {item[0]} - Produto: {item[1]} - Preço: {item[2]}" for item in resultado])
    label_resultado.config(text=resultado_texto)

def update():
    nome_produto = entry_nome_produto.get()
    preco_produto = float(entry_preco_produto.get())
    comando = f'UPDATE vendas SET preco_produto = {preco_produto} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()  # Edita o banco de dados
    label_resultado.config(text="Produto atualizado com sucesso!")
    limpar_campos()

def delete():
    nome_produto = entry_nome_produto.get()
    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()  # Edita o banco de dados
    label_resultado.config(text="Produto excluído com sucesso!")
    limpar_campos()

def limpar_campos():
    entry_nome_produto.delete(0, END)
    entry_preco_produto.delete(0, END)

# Janela principal
janela_inicial = Tk()
janela_inicial.title("CRUD de Produtos")


# Labels e entradas
label_nome_produto = Label(janela_inicial, text="Nome do Produto:")
label_nome_produto.grid(column=1 ,row=0)
entry_nome_produto = Entry(janela_inicial)
entry_nome_produto.grid(column=1 ,row=1)

label_preco_produto = Label(janela_inicial, text="Preço do Produto:")
label_preco_produto.grid(column=1 ,row=2)
entry_preco_produto = Entry(janela_inicial)
entry_preco_produto.grid(column=1 ,row=3)

# Botões
button_create = Button(janela_inicial, text="Adicionar Produto", command=create)
button_create.grid(column=0 ,row=4, pady=20)

button_read = Button(janela_inicial, text="Mostrar Produtos", command=read)
button_read.grid(column=1 ,row=4, pady=20)

button_update = Button(janela_inicial, text="Atualizar Produto", command=update)
button_update.grid(column=2 ,row=4, pady=20)

button_delete = Button(janela_inicial, text="Excluir Produto", command=delete, bg="red", fg="black")
button_delete.grid(column=1 ,row=5, pady=10)

# Label para exibir resultados
label_resultado = Label(janela_inicial, text="")
label_resultado.grid(column=1 ,row=6)

# Rodando a interface
janela_inicial.mainloop()

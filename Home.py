from os import curdir
from PyQt5 import QtWidgets, uic
import mysql.connector
from mysql.connector import connect, cursor
from reportlab.pdfgen import canvas

valor_id= 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="kbt_system"
)

def editar_dados():
    global valor_id
    linha = listar_dados_produtos.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produto")
    id_lidos = cursor.fetchall()
    id_valor = id_lidos[linha][0]
    cursor.execute("SELECT * FROM produto WHERE id="+str(id_valor))
    produto = cursor.fetchall()
    editar_produto.show()

    valor_id = id_valor

    editar_produto.lineEdit.setText(str(produto[0][0]))
    editar_produto.lineEdit_2.setText(str(produto[0][1]))
    editar_produto.lineEdit_3.setText(str(produto[0][2]))
    editar_produto.lineEdit_4.setText(str(produto[0][3]))
    editar_produto.lineEdit_5.setText(str(produto[0][4]))
    editar_produto.lineEdit_6.setText(str(produto[0][5]))

def salvar_produto_editado():
    # pegar o id
    global valor_id
    # pegar o que foi digitado na linha
    descricao = editar_produto.lineEdit_2.text()
    codigo_de_barras = editar_produto.lineEdit_3.text()
    preco = editar_produto.lineEdit_4.text()
    fornecedor = editar_produto.lineEdit_5.text()
    marca = editar_produto.lineEdit_6.text()
    # atualizar os dados no banco
    salvar = banco.cursor()
    salvar.execute("UPDATE produto SET descricao='{}', codigo_de_barras='{}', preco='{}', fornecedor='{}', marca='{}' WHERE id={}".format(descricao,codigo_de_barras,preco,fornecedor,marca,valor_id))
    #fechar e atualizar dados
    editar_produto.close()
    listar_dados_produtos.close()
    listar_produtos()

def excluir_dados():
    linha = listar_dados_produtos.tableWidget.currentRow()
    listar_dados_produtos.tableWidget.removeRow(linha)

    excluir = banco.cursor()
    excluir.execute("SELECT id FROM produto")
    id_lidos = excluir.fetchall()
    id_valor = id_lidos[linha][0]
    excluir.execute("DELETE FROM produto WHERE id=" + str(id_valor))

def gerar_pdf():
    tb_produtos = banco.cursor()
    comando_SQL = "SELECT * FROM produto"
    tb_produtos.execute(comando_SQL)
    dados_lidos = tb_produtos.fetchall() 
    y = 0
    pdf = canvas.Canvas("Produtos_cadastrados.pdf")
    pdf.setFont("Times-Bold", 12)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 12)

    pdf.drawString(5,750, "ID")
    pdf.drawString(40,750, "DESCRIÇÃO")
    pdf.drawString(160,750, "C. DE BARRA")
    pdf.drawString(280,750, "PREÇO")
    pdf.drawString(360,750, "FORNECEDOR")
    pdf.drawString(520,750, "MARCA")

    for i in range (0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(5,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(60,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(180,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(280,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(390,750 - y, str(dados_lidos[i][4]))
        pdf.drawString(530,750 - y, str(dados_lidos[i][5]))

    pdf.save()
    print("PDF FOI GERADO COM SUCESSO!")

def add_produto():

    descricao = novo_produto_serviço.lineEdit.text()
    codigo_de_barras = novo_produto_serviço.lineEdit_4.text()
    preco = novo_produto_serviço.lineEdit_2.text()
    fornecedor = novo_produto_serviço.lineEdit_3.text()
    marca = novo_produto_serviço.lineEdit_5.text()

    tb_produto = banco.cursor()
    comando_SQL = "INSERT INTO produto (descricao,codigo_de_barras,preco,fornecedor,marca) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(descricao)), str(codigo_de_barras), str((preco)), str((fornecedor)), str((marca))
    tb_produto.execute(comando_SQL, dados)
    banco.commit()

    novo_produto_serviço.lineEdit.setText("")
    novo_produto_serviço.lineEdit_4.setText("")
    novo_produto_serviço.lineEdit_2.setText("")
    novo_produto_serviço.lineEdit_3.setText("")
    novo_produto_serviço.lineEdit_5.setText("")

def add_servico():

    descricao_servico = novo_produto_serviço.lineEdit_6.text()
    preco = novo_produto_serviço.lineEdit_7.text()

    tb_servico = banco.cursor()
    comando_SQL = "INSERT INTO servico (descricao,preco) VALUES (%s,%s)"
    dados = (str(descricao_servico), str(preco))
    tb_servico.execute(comando_SQL, dados)
    banco.commit()

    novo_produto_serviço.lineEdit_6.setText("")
    novo_produto_serviço.lineEdit_7.setText("")

def listar_produtos():
    listar_dados_produtos.show()

    tb_produtos = banco.cursor()
    comando_SQL = "SELECT * FROM produto"
    tb_produtos.execute(comando_SQL)
    dados_lidos = tb_produtos.fetchall()  

    listar_dados_produtos.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_produtos.tableWidget.setColumnCount(6) 

    for i in range (0,len(dados_lidos)):
        for j in range(0, 6):
            listar_dados_produtos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def chamar_cadastro():
    ambiente_cadastro.show()
    ambiente_cadastro.pushButton_3.clicked.connect(chamar_novo_cliente)
    ambiente_cadastro.pushButton_5.clicked.connect(chamar_novo_produto_servico)

def chamar_novo_cliente():
    novo_cliente.show()




def chamar_agenda():
    ambiente_agenda.show()
    ambiente_agenda.pushButton_2.clicked.connect(chamar_novo_agendamento)

def chamar_novo_agendamento():
    novo_agendamento.show()

def chamar_novo_produto_servico():
    novo_produto_serviço.show()



app = QtWidgets.QApplication([])
home = uic.loadUi('Home.ui')
home.pushButton.clicked.connect(chamar_agenda)
home.pushButton_3.clicked.connect(chamar_cadastro)




ambiente_agenda = uic.loadUi('Agenda.ui')

novo_agendamento = uic.loadUi('Novo Agendamento.ui')

ambiente_cadastro = uic.loadUi('Ambiente Cadastro.ui')

novo_cliente = uic.loadUi('Novo Cliente.ui')

listar_dados_produtos = uic.loadUi('Listar dados produtos.ui')

editar_produto = uic.loadUi('Editar produto.ui')

novo_produto_serviço = uic.loadUi('Novo Produto e Serviço.ui')
novo_produto_serviço.pushButton_2.clicked.connect(add_produto)
novo_produto_serviço.pushButton_5.clicked.connect(add_servico)
novo_produto_serviço.pushButton.clicked.connect(listar_produtos)

listar_dados_produtos.pushButton.clicked.connect(gerar_pdf)
listar_dados_produtos.pushButton_2.clicked.connect(excluir_dados)
listar_dados_produtos.pushButton_3.clicked.connect(editar_dados)

editar_produto.pushButton.clicked.connect(salvar_produto_editado)

home.show()
app.exec()

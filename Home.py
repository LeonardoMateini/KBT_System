from PyQt5 import QtWidgets, uic
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="kbt_system"
)

def add_produto():

    linha1 = novo_produto_serviço.lineEdit.text()
    linha2 = novo_produto_serviço.lineEdit_4.text()
    linha3 = novo_produto_serviço.lineEdit_2.text()
    linha4 = novo_produto_serviço.lineEdit_3.text()
    linha5 = novo_produto_serviço.lineEdit_5.text()

    print(linha1)
    print(linha2)
    print(linha3)
    print(linha4)
    print(linha5)
   

    bd_produto = banco.cursor()
    comando_SQL = "INSERT INTO produto (descricao,codigo_de_barras,preco,fornecedor,marca) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5))
    bd_produto.execute(comando_SQL, dados)
    banco.commit()

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

novo_produto_serviço = uic.loadUi('Novo Produto e Serviço.ui')
novo_produto_serviço.pushButton_2.clicked.connect(add_produto)

home.show()
app.exec()

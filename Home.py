from PyQt5 import QtWidgets, uic
import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database="DB_KBT_SYSTEM"
)

cursor = banco.cursor()

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
home.show()



ambiente_agenda = uic.loadUi('Agenda.ui')
novo_agendamento = uic.loadUi('Novo Agendamento.ui')

ambiente_cadastro = uic.loadUi('Ambiente Cadastro.ui')

novo_cliente = uic.loadUi('Novo Cliente.ui')

novo_produto_serviço = uic.loadUi('Novo Produto e Serviço.ui')

app.exec()

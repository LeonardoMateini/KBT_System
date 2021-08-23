from PyQt5 import QtWidgets, uic
import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database="DB_KBT_SYSTEM"
)
# cursor = banco.cursor()
# comando_SQL = """create table SERVICO (
# 	ID INT NOT NULL AUTO_INCREMENT,
# 	DESCRICAO varchar (50),
# 	PRECO DOUBLE,
# 	PRIMARY KEY (id)
# );"""
# cursor.execute(comando_SQL)
# banco.commit()


def chamar_cadastro():
    ambiente_cadastro.show()
    ambiente_cadastro.pushButton_3.clicked.connect(chamar_novo_cliente)
    ambiente_cadastro.pushButton_5.clicked.connect(chamar_novo_produto_servico)
    ambiente_cadastro.pushButton_7.clicked.connect(chamar_plano_de_serviço)


def chamar_novo_cliente():
    novo_cliente.show()


def chamar_agenda():
    ambiente_agenda.show()
    ambiente_agenda.pushButton_2.clicked.connect(chamar_novo_agendamento)


def chamar_novo_agendamento():
    novo_agendamento.show()


def chamar_novo_produto_servico():
    novo_produto_serviço.show()
    novo_produto_serviço.pushButton_2.clicked.connect(adicionar_produto)
    novo_produto_serviço.pushButton_5.clicked.connect(adicionar_servico)

def chamar_plano_de_serviço():
    plano_de_serviço.show()

def adicionar_produto():
    descricao = novo_produto_serviço.lineEdit_2.text()
    codigo_barras = novo_produto_serviço.lineEdit_3.text()
    preco = novo_produto_serviço.lineEdit_4.text()
    fornecedor = novo_produto_serviço.lineEdit_5.text()
    marca = novo_produto_serviço.lineEdit_6.text()

    cursor = banco.cursor()
    # verificacao_id_ja_preenchido = "SELECT TOP 1 * FROM "
    comando_SQL = "INSERT INTO TB_PRODUTO (DESCRICAO, CODIGO_BARRAS, PRECO, FORNECEDOR, MARCA) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(descricao), str(codigo_barras), preco, str(fornecedor), str(marca))
    cursor.execute(comando_SQL, dados)
    banco.commit()

def adicionar_servico():
    descricao = novo_produto_serviço.lineEdit_10.text()
    preco = novo_produto_serviço.lineEdit_11.text()

    cursor = banco.cursor()
    # verificacao_id_ja_preenchido = "SELECT TOP 1 * FROM "
    comando_SQL = "INSERT INTO TB_SERVICO (DESCRICAO, PRECO) VALUES (%s,%s)"
    dados = (str(descricao), str(preco))
    cursor.execute(comando_SQL, dados)
    banco.commit()

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

plano_de_serviço= uic.loadUi('Contratar Plano Serviço.ui')
app.exec()

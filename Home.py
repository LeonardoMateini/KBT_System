from PyQt5 import QtWidgets, uic
import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database="DB_KBT_SYSTEM"
)
cursor = banco.cursor()
comando_SQL = """CREATE TABLE TB_PET(
      	NOME			VARCHAR(50)		NOT NULL
    ,   FK_CONTATO_DONO INT             NOT NULL
	,	IDADE			INT
	,	PORTE			CHAR(1)
	,	SEXO 			CHAR(1)         NOT NULL
	,   CASTRADO        CHAR(1)
	,	RACA			VARCHAR(30)
	,	CONSTRAINT FK_CONTATO_DONO FOREIGN KEY (FK_CONTATO_DONO) REFERENCES TB_CLIENTE (CONTATO)
);"""
cursor.execute(comando_SQL)
banco.commit()


def chamar_cadastro():
    ambiente_cadastro.show()
    ambiente_cadastro.pushButton_3.clicked.connect(chamar_novo_cliente)
    ambiente_cadastro.pushButton_5.clicked.connect(chamar_novo_produto_servico)
    ambiente_cadastro.pushButton_7.clicked.connect(chamar_plano_de_serviço)


def chamar_novo_cliente():
    novo_cliente.show()
    novo_cliente.pushButton_2.clicked.connect(adicionar_cliente)
    novo_cliente.pushButton.clicked.connect(adicionar_pet)

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

def adicionar_cliente():
    nome = novo_cliente.lineEdit_2.text()
    contato = novo_cliente.lineEdit_3.text()
    cep = novo_cliente.lineEdit_4.text()
    bairro = novo_cliente.lineEdit_5.text()
    logradouro = novo_cliente.lineEdit_6.text()
    numero = novo_cliente.lineEdit_8.text()
    complemento = novo_cliente.lineEdit_7.text()


    cursor = banco.cursor()
    comando_SQL = "INSERT INTO TB_CLIENTE (NOME, CONTATO, CEP, BAIRRO, LOGRADOURO, NUMERO, COMPLEMENTO) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(nome), str(contato), cep, str(bairro), str(logradouro), numero, str(complemento))
    cursor.execute(comando_SQL, dados)
    banco.commit()

def adicionar_pet():
    nome = novo_cliente.lineEdit_9.text()
    contato_dono = novo_cliente.lineEdit_12.text()
    idade = novo_cliente.lineEdit_11.text()
    raca = novo_cliente.lineEdit_10.text()
    porte = ''
    sexo = ''
    castrado = ''
    if novo_cliente.radioButton_3.isChecked():
        porte = 'P'
    elif novo_cliente.radioButton_5.isChecked():
        porte = 'M'
    elif novo_cliente.radioButton_4.isChecked():
        porte = 'G'

    if novo_cliente.radioButton_2.isChecked():
        sexo = 'F'
    elif novo_cliente.radioButton.isChecked():
        sexo = 'M'

    if novo_cliente.radioButton_9.isChecked():
        sexo = 'S'
    elif novo_cliente.radioButton_10.isChecked():
        sexo = 'N'

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO TB_CLIENTE (NOME, FK_CONTATO_DONO, IDADE, PORTE, SEXO, CASTRADO, RACA) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(nome), str(contato_dono), str(idade), str(porte), str(sexo), str(castrado), str(raca))
    cursor.execute(comando_SQL, dados)
    banco.commit()

def adicionar_produto():
    descricao = novo_produto_serviço.lineEdit_2.text()
    codigo_barras = novo_produto_serviço.lineEdit_3.text()
    preco = novo_produto_serviço.lineEdit_4.text()
    fornecedor = novo_produto_serviço.lineEdit_5.text()
    marca = novo_produto_serviço.lineEdit_6.text()

    cursor = banco.cursor()
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

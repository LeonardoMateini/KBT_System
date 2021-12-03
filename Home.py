from mysql.connector import connection
from reportlab.pdfgen import canvas
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from random import randint
from datetime import datetime
import mysql.connector


banco = mysql.connector.connect(
    host='localhost',
    user='leonardo',
    passwd='',
    database="DB_KBT_SYSTEM"
)
# banco = mysql.connector.connect(
#     host='localhost:3307',
#     user='root',
#     passwd='',
#     database="mysql-container"
# )

# cursor = banco.cursor()
# comando_SQL = """CREATE TABLE TB_BAIXA_AGENDAMENTO(
#       		ID_AGENDAMENTO		INT		NOT NULL
#       	,	DESCRICAO_PRECO		VARCHAR(400)	NOT NULL
#       	,	VALOR_TOTAL		DECIMAL(15, 2)	NOT NULL
#       	,	FORMA_PAGAMENTO		VARCHAR(20)	NOT NULL
#    	,	PRIMARY KEY		(ID_AGENDAMENTO)
# )"""
# cursor.execute(comando_SQL)
# banco.commit()


def chamar_novo_cliente():
    novo_cliente.show()
    novo_cliente.pushButton_2.clicked.connect(criar_n_cadastro)
    novo_cliente.pushButton.clicked.connect(adicionar_pet)
    novo_cliente.pushButton_3.clicked.connect(listar_clientes)
    novo_cliente.pushButton_4.clicked.connect(listar_clientes_inativos)
    novo_cliente.pushButton_5.clicked.connect(listar_pets)
    novo_cliente.pushButton_6.clicked.connect(listar_pets_inativos)

    listar_dados_clientes.pushButton_3.clicked.connect(editar_dados_cliente)
    listar_dados_clientes.pushButton_2.clicked.connect(desativar_ativar_dados_cliente)
    listar_dados_pets.pushButton_3.clicked.connect(editar_dados_pet)
    listar_dados_pets.pushButton_2.clicked.connect(desativar_ativar_dados_pet)

    editar_cliente.pushButton.clicked.connect(salvar_cliente_editado)
    editar_pet.pushButton.clicked.connect(salvar_pet_editado)



def chamar_novo_produto_servico():
    novo_produto_serviço.show()
    novo_produto_serviço.pushButton_2.clicked.connect(adicionar_produto)
    novo_produto_serviço.pushButton_3.clicked.connect(adicionar_servico)
    novo_produto_serviço.pushButton.clicked.connect(listar_produtos)
    novo_produto_serviço.pushButton_4.clicked.connect(listar_servicos)
    novo_produto_serviço.pushButton_5.clicked.connect(listar_produtos_inativos)
    novo_produto_serviço.pushButton_6.clicked.connect(listar_servicos_inativos)

    listar_dados_produtos.pushButton.clicked.connect(gerar_pdf_produto)
    listar_dados_produtos.pushButton_2.clicked.connect(desativar_ativar_dados_produto)
    listar_dados_produtos.pushButton_3.clicked.connect(editar_dados_produtos)

    listar_dados_servicos.pushButton.clicked.connect(gerar_pdf_servico)
    listar_dados_servicos.pushButton_2.clicked.connect(desativar_ativar_dados_servico)
    listar_dados_servicos.pushButton_3.clicked.connect(editar_dados_servico)

    editar_produto.pushButton.clicked.connect(salvar_produto_editado)
    editar_servico.pushButton.clicked.connect(salvar_servico_editado)


def chamar_plano_serviço():
    plano_serviço.show()

def chamar_novo_agendamento():
    novo_agendamento.show()
    novo_agendamento.pushButton.clicked.connect(verifica_buscar_pet)
    novo_agendamento.pushButton_2.clicked.connect(pegar_descricao_id_tosa_novo_agendamento)
    novo_agendamento.calendarWidget.selectionChanged.connect(exibir_data_novo_agendamento)
    novo_agendamento.pushButton_3.clicked.connect(adicionar_novo_agendamento)

    listar_pets_agendamento.pushButton_3.clicked.connect(exibe_dados_pet_agendamento)



def chamar_agenda():
    listar_agenda()
    listar_dados_agenda.pushButton_3.clicked.connect(listar_agendamento)

    listar_dados_agendamento.pushButton_3.clicked.connect(editar_dados_agendamento)
    listar_dados_agendamento.pushButton_4.clicked.connect(chamar_finalizar_dados_agendamento)

    editar_agendamento.pushButton_2.clicked.connect(pegar_descricao_id_tosa_editar_agendamento)
    editar_agendamento.calendarWidget.selectionChanged.connect(exibir_data_editar_agendamento)
    editar_agendamento.pushButton_3.clicked.connect(salvar_agendamento_editado)

    listar_produtos_baixa_agendamento.pushButton.clicked.connect(buscar_produto_baixa_agendamento_2)
    listar_servicos_baixa_agendamento.pushButton.clicked.connect(buscar_servico_baixa_agendamento_2)

    finalizar_agendamento.pushButton_2.clicked.connect(adicionar_produto_baixa_agendamento)
    finalizar_agendamento.pushButton_3.clicked.connect(adicionar_servico_baixa_agendamento)
    finalizar_agendamento.pushButton_6.clicked.connect(remover_item_finalizacao_agendamento)
    finalizar_agendamento.pushButton_4.clicked.connect(finalizar_dados_agendamento)

def chamar_agenda_finalizados():
    listar_agenda_finalizados()
    listar_dados_agenda.pushButton_3.clicked.connect(listar_agendamento)


def chamar_funcoes_home():
    home.show()
    listar_agenda_home()
    home.pushButton_3.clicked.connect(listar_agendamento)

def chamar_funcoes_login():
    login_tela.show()
    login_tela.pushButton.clicked.connect(verifica_login)

def verifica_login():
    usuario = login_tela.lineEdit.text()
    senha = login_tela.lineEdit_2.text()
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_LOGIN WHERE USUARIO = '{usuario}' AND SENHA = '{senha}'")
    dados_lidos = cursor.fetchall()
    if len(dados_lidos) > 0:
        return chamar_funcoes_home(), login_tela.close()
    else:
        QMessageBox.about(login_tela, 'Erro', 'Usuário ou senha estão incorretos.')


def criar_n_cadastro():
    global n_cadastro
    n_cadastro = randint(1, 10000)
    verificar_existencia_n_cadastro()
    print(n_cadastro)

def verificar_existencia_n_cadastro():
    global n_cadastro
    n_cadastro = n_cadastro
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM TB_CLIENTE WHERE N_CADASTRO = {n_cadastro};')
    dados_lidos = cursor.fetchall()
    if len(dados_lidos) > 0:
        criar_n_cadastro()

    else:
        adicionar_cliente()

def adicionar_cliente():
    global n_cadastro

    n_cadastro = n_cadastro
    nome = novo_cliente.lineEdit_2.text()
    contato = novo_cliente.lineEdit_3.text()
    cep = novo_cliente.lineEdit_4.text()
    bairro = novo_cliente.lineEdit_5.text()
    logradouro = novo_cliente.lineEdit_6.text()
    numero = novo_cliente.lineEdit_8.text()
    complemento = novo_cliente.lineEdit_7.text()

    try:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO TB_CLIENTE (N_CADASTRO, NOME, CONTATO, BAIRRO, LOGRADOURO, COMPLEMENTO) VALUES (%s,%s,%s,%s,%s,%s)"
        dados = (n_cadastro, str(nome), contato, str(bairro), str(logradouro), str(complemento))

        if cep != '' and numero != '':
            comando_SQL = "INSERT INTO TB_CLIENTE (N_CADASTRO, NOME, CONTATO, CEP, BAIRRO, LOGRADOURO, NUMERO, COMPLEMENTO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            dados = (n_cadastro, str(nome), str(contato), cep, str(bairro), str(logradouro), numero, str(complemento))

        elif cep == '' and numero != '':
            comando_SQL = "INSERT INTO TB_CLIENTE (N_CADASTRO, NOME, CONTATO, BAIRRO, LOGRADOURO, NUMERO, COMPLEMENTO) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            dados = (n_cadastro, str(nome), str(contato), str(bairro), str(logradouro), numero, str(complemento))

        elif cep != '' and numero == '':
            comando_SQL = "INSERT INTO TB_CLIENTE (N_CADASTRO, NOME, CONTATO, CEP, BAIRRO, LOGRADOURO, COMPLEMENTO) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            dados = (n_cadastro, str(nome), str(contato), cep, str(bairro), str(logradouro), str(complemento))

        cursor.execute(comando_SQL, dados)
        banco.commit()
        mensagem = (f'Cliente cadastrado com sucesso.\nNº de Cadastro: {n_cadastro}')
        QMessageBox.about(novo_cliente, 'Ação Realizada', mensagem)

    except:
        # se o campo obrigató contato for vazio imprimir essa mensagem
        if contato == '' or nome == '':
            QMessageBox.about(novo_cliente, 'Erro', 'Campos obrigatórios não foram preenchidos.')

        # if (contato != '') and (type(contato) != int()):
        #     QMessageBox.about(novo_cliente, 'Erro', 'Contato deve ter somente números')

    # Após passar pelo except ele vai executar esse bloco
    else:
        novo_cliente.lineEdit_2.setText("")
        novo_cliente.lineEdit_3.setText("")
        novo_cliente.lineEdit_4.setText("")
        novo_cliente.lineEdit_5.setText("")
        novo_cliente.lineEdit_6.setText("")
        novo_cliente.lineEdit_8.setText("")
        novo_cliente.lineEdit_7.setText("")


def adicionar_pet():
    n_cadastro = novo_cliente.lineEdit_14.text()
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
        castrado = 'S'
    elif novo_cliente.radioButton_10.isChecked():
        castrado = 'N'


    try:
        cursor = banco.cursor()
        comando_SQL = (f"INSERT INTO TB_PET (FK_N_CADASTRO, NOME, CONTATO_DONO, IDADE, PORTE, SEXO, CASTRADO, RACA) VALUES ('{n_cadastro}','{nome}','{contato_dono}','{idade}','{porte}','{sexo}','{castrado}','{raca}')")
        cursor.execute(comando_SQL)
        banco.commit()

        QMessageBox.about(novo_cliente, 'Ação Realizada', 'Pet cadastrado com sucesso.')

    except:
        # se o campo obrigató contato for vazio imprimir essa mensagem
        if n_cadastro == '' or contato_dono == '' or nome == '':
            QMessageBox.about(novo_cliente, 'Erro', 'Campos obrigatórios não foram preenchidos.')

        if (contato_dono != '') and (type(contato_dono) != int()):
            QMessageBox.about(novo_cliente, 'Erro', 'Contato cliente deve ter somente números')

        # if type(n_cadastro) == int():
        #     QMessageBox.about(novo_cliente, 'Erro', 'Nº de Cadastro não registrado.')

        QMessageBox.about(novo_cliente, 'Erro', 'Erro genérico ao cadastrar Pet.')



    # Após passar pelo except ele vai executar esse bloco
    else:
        novo_cliente.lineEdit_14.setText("")
        novo_cliente.lineEdit_9.setText("")
        novo_cliente.lineEdit_12.setText("")
        novo_cliente.lineEdit_11.setText("")
        novo_cliente.lineEdit_10.setText("")


def adicionar_produto():
    descricao = novo_produto_serviço.lineEdit.text()
    codigo_barras = novo_produto_serviço.lineEdit_4.text()
    preco = novo_produto_serviço.lineEdit_2.text()
    fornecedor = novo_produto_serviço.lineEdit_3.text()
    marca = novo_produto_serviço.lineEdit_5.text()

    try:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO TB_PRODUTO (DESCRICAO, CODIGO_BARRAS, PRECO, FORNECEDOR, MARCA) VALUES (%s,%s,%s,%s,%s)"
        dados = (str(descricao), str(codigo_barras), preco, str(fornecedor), str(marca))
        cursor.execute(comando_SQL, dados)
        banco.commit()

        QMessageBox.about(novo_cliente, 'Ação Realizada', 'Produto cadastrado com sucesso.')

    except:
        # se o campo obrigató contato for vazio imprimir essa mensagem
        if descricao == '' or codigo_barras == '' or preco == '':
            QMessageBox.about(novo_cliente, 'Erro', 'Campos obrigatórios não foram preenchidos.')

        if codigo_barras != '' and (type(codigo_barras) == int()):
            cursor1 = banco.cursor()
            verifica_chave = (f'SELECT * FROM TB_PET WHERE CONTATO = {codigo_barras};')
            cursor1.execute(verifica_chave)
            dados_lidos = cursor1.fetchall()
            valor_lido = dados_lidos
            if len(dados_lidos) > 0:
                QMessageBox.about(novo_cliente, 'Erro', 'Já existe regisro para esse código de barras.')

        if (codigo_barras != '') and (type(codigo_barras) != int()):
            QMessageBox.about(novo_cliente, 'Erro', 'Código de barras deve ter somente números')

    else:
        novo_produto_serviço.lineEdit.setText("")
        novo_produto_serviço.lineEdit_4.setText("")
        novo_produto_serviço.lineEdit_2.setText("")
        novo_produto_serviço.lineEdit_3.setText("")
        novo_produto_serviço.lineEdit_5.setText("")


def adicionar_servico():
    descricao = novo_produto_serviço.lineEdit_6.text()
    preco = novo_produto_serviço.lineEdit_7.text()

    try:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO TB_SERVICO (DESCRICAO, PRECO) VALUES (%s,%s)"
        dados = (str(descricao), preco)
        cursor.execute(comando_SQL, dados)
        banco.commit()

        QMessageBox.about(novo_cliente, 'Ação Realizada', 'Serviço cadastrado com sucesso.')

    except:
        # se o campo obrigató contato for vazio imprimir essa mensagem
        if descricao == '':
            QMessageBox.about(novo_cliente, 'Erro', 'Campo obrigatório não foi preenchido.')

        if descricao != '' and (type(preco) == str()):
            cursor1 = banco.cursor()
            verifica_chave = (f'SELECT * FROM TB_PET WHERE CONTATO = {descricao};')
            cursor1.execute(verifica_chave)
            dados_lidos = cursor1.fetchall()
            valor_lido = dados_lidos
            if len(dados_lidos) > 0:
                QMessageBox.about(novo_cliente, 'Erro', 'Já existe regisro para essa descrição.')

        if (preco != '') and (type(preco) != float()):
            QMessageBox.about(novo_cliente, 'Erro', 'Preço deve ter somente números')
    else:
        novo_produto_serviço.lineEdit_6.setText("")
        novo_produto_serviço.lineEdit_7.setText("")


def listar_clientes():
    global status_cliente
    listar_dados_clientes.show()

    n_cadastro = novo_cliente.lineEdit_13.text()
    cursor = banco.cursor()
    if n_cadastro != '':
        comando_SQL = (f"SELECT * FROM TB_CLIENTE WHERE STATUS = 'A' AND N_CADASTRO = '{n_cadastro}'")

    else:
        comando_SQL = "SELECT * FROM TB_CLIENTE WHERE STATUS = 'A'"

    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_clientes.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_clientes.tableWidget.setColumnCount(14)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 13):
            listar_dados_clientes.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    status_cliente = 'A'


def listar_clientes_inativos():
    global status_cliente
    listar_dados_clientes.show()

    n_cadastro = novo_cliente.lineEdit_13.text()
    cursor = banco.cursor()
    if n_cadastro != '':
        comando_SQL = (f"SELECT * FROM TB_CLIENTE WHERE STATUS = 'I' AND N_CADASTRO = '{n_cadastro}'")
    else:
        comando_SQL = "SELECT * FROM TB_CLIENTE WHERE STATUS = 'I'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_clientes.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_clientes.tableWidget.setColumnCount(14)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 13):
            listar_dados_clientes.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    status_cliente = 'I'


def listar_pets():
    global status_pet, n_cadastro
    listar_dados_pets.show()
    n_cadastro = novo_cliente.lineEdit_14.text()

    cursor = banco.cursor()
    comando_SQL = (f"SELECT * FROM TB_PET WHERE STATUS = 'A' AND FK_N_CADASTRO = '{n_cadastro}'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    if len(dados_lidos) < 1:
        QMessageBox.about(novo_cliente, 'Atenção', 'Nenhum Pet encontrado para o Nº de cadastro informado.')

    elif len(dados_lidos) > 0 and n_cadastro != '':
        listar_dados_pets.tableWidget.setRowCount(len(dados_lidos))
        listar_dados_pets.tableWidget.setColumnCount(9)

        for i in range(0, len(dados_lidos)):
            for j in range(0, 9):
                listar_dados_pets.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

        status_pet = 'A'


def listar_pets_inativos():
    global status_pet, n_cadastro
    listar_dados_pets.show()
    n_cadastro = novo_cliente.lineEdit_14.text()

    cursor = banco.cursor()
    comando_SQL = (
        f"SELECT * FROM TB_PET WHERE STATUS = 'I' AND FK_N_CADASTRO = '{n_cadastro}'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    if len(dados_lidos) < 1:
        QMessageBox.about(novo_cliente, 'Atenção', 'Nenhum Pet encontrado para o Nº de cadastro informado.')

    else:
        listar_dados_pets.tableWidget.setRowCount(len(dados_lidos))
        listar_dados_pets.tableWidget.setColumnCount(9)

        for i in range(0, len(dados_lidos)):
            for j in range(0, 9):
                listar_dados_pets.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

        status_pet = 'I'


def listar_produtos():
    global status_produto
    listar_dados_produtos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_PRODUTO WHERE STATUS = 'A'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_produtos.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_produtos.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            listar_dados_produtos.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    status_produto = 'A'


def listar_produtos_inativos():
    global status_produto
    listar_dados_produtos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_PRODUTO WHERE STATUS = 'I'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_produtos.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_produtos.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            listar_dados_produtos.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    status_produto = 'I'


def listar_servicos():
    global status_servico
    listar_dados_servicos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_SERVICO WHERE STATUS = 'A'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_servicos.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_servicos.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            listar_dados_servicos.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    status_servico = 'A'


def listar_servicos_inativos():
    global status_servico
    listar_dados_servicos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_SERVICO WHERE STATUS = 'I'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_servicos.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_servicos.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            listar_dados_servicos.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    status_servico = 'I'


def editar_dados_cliente():
    global status_cliente
    linha = listar_dados_clientes.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT N_CADASTRO FROM TB_CLIENTE WHERE STATUS = '{status_cliente}'")
    n_cadastro_lido = cursor.fetchall()
    n_cadastro_valor = n_cadastro_lido[linha][0]
    cursor.execute("SELECT * FROM TB_CLIENTE WHERE N_CADASTRO =" + str(n_cadastro_valor))
    cliente = cursor.fetchall()
    editar_cliente.show()

    editar_cliente.lineEdit_14.setText(str(cliente[0][0]))
    editar_cliente.lineEdit.setText(str(cliente[0][1]))
    editar_cliente.lineEdit_2.setText(str(cliente[0][2]))
    editar_cliente.lineEdit_3.setText(str(cliente[0][3]))
    editar_cliente.lineEdit_4.setText(str(cliente[0][4]))
    editar_cliente.lineEdit_5.setText(str(cliente[0][5]))
    editar_cliente.lineEdit_6.setText(str(cliente[0][6]))
    editar_cliente.lineEdit_7.setText(str(cliente[0][7]))
    editar_cliente.lineEdit_8.setText(str(cliente[0][8]))
    editar_cliente.lineEdit_9.setText(str(cliente[0][9]))
    editar_cliente.lineEdit_10.setText(str(cliente[0][10]))
    editar_cliente.lineEdit_11.setText(str(cliente[0][11]))
    editar_cliente.lineEdit_12.setText(str(cliente[0][12]))


def editar_dados_pet():
    global status_pet, n_cadastro, nome_pet_antes_alteracao
    linha = listar_dados_pets.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_PET WHERE STATUS = '{status_pet}' AND FK_N_CADASTRO = '{n_cadastro}'")
    pets_listados = cursor.fetchall()
    nome_pet_antes_alteracao = pets_listados[linha][2]
    cursor.execute(f"SELECT * FROM TB_PET WHERE FK_N_CADASTRO = '{n_cadastro}' AND NOME = '{nome_pet_antes_alteracao}'")
    pet = cursor.fetchall()
    editar_pet.show()

    editar_pet.lineEdit_9.setText(str(pet[0][0]))
    editar_pet.lineEdit.setText(str(pet[0][1]))
    editar_pet.lineEdit_2.setText(str(pet[0][2]))
    editar_pet.lineEdit_3.setText(str(pet[0][3]))
    editar_pet.lineEdit_4.setText(str(pet[0][4]))
    editar_pet.lineEdit_5.setText(str(pet[0][5]))
    editar_pet.lineEdit_6.setText(str(pet[0][6]))
    editar_pet.lineEdit_7.setText(str(pet[0][7]))
    editar_pet.lineEdit_8.setText(str(pet[0][8]))


def editar_dados_produtos():
    global codigo_barras_valor, status_produto
    linha = listar_dados_produtos.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT CODIGO_BARRAS FROM TB_PRODUTO WHERE STATUS = '{status_produto}'")
    codigo_barras_lido = cursor.fetchall()
    codigo_barras_valor = codigo_barras_lido[linha][0]
    cursor.execute("SELECT * FROM TB_PRODUTO WHERE CODIGO_BARRAS =" + str(codigo_barras_valor))
    produto = cursor.fetchall()
    editar_produto.show()

    editar_produto.lineEdit.setText(str(produto[0][0]))
    editar_produto.lineEdit_2.setText(str(produto[0][1]))
    editar_produto.lineEdit_3.setText(str(produto[0][2]))
    editar_produto.lineEdit_4.setText(str(produto[0][3]))
    editar_produto.lineEdit_5.setText(str(produto[0][4]))
    editar_produto.lineEdit_6.setText(str(produto[0][5]))


def editar_dados_servico():
    global valor_id_servico, status_servico
    linha = listar_dados_servicos.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT ID FROM TB_SERVICO WHERE STATUS ='{status_servico}'")
    id_lidos = cursor.fetchall()
    id_valor = id_lidos[linha][0]
    cursor.execute("SELECT * FROM TB_SERVICO WHERE ID =" + str(id_valor))
    servico = cursor.fetchall()
    editar_servico.show()

    valor_id_servico = id_valor

    editar_servico.lineEdit_3.setText(str(servico[0][0]))
    editar_servico.lineEdit_4.setText(str(servico[0][1]))
    editar_servico.lineEdit_5.setText(str(servico[0][2]))
    editar_servico.lineEdit_6.setText(str(servico[0][3]))


def salvar_cliente_editado():
    global contato_valor, status_cliente

    n_cadastro = editar_cliente.lineEdit_14.text()
    nome = editar_cliente.lineEdit_2.text()
    contato = editar_cliente.lineEdit_3.text()
    cep = editar_cliente.lineEdit_4.text()
    bairro = editar_cliente.lineEdit_5.text()
    logradouro = editar_cliente.lineEdit_6.text()
    numero = editar_cliente.lineEdit_7.text()
    complemento = editar_cliente.lineEdit_8.text()

    cursor = banco.cursor()
    cursor.execute(
        f"UPDATE TB_CLIENTE SET NOME = '{nome}',CONTATO = '{contato}', CEP ='{cep}', BAIRRO = '{bairro}', LOGRADOURO ='{logradouro}', NUMERO= '{numero}', COMPLEMENTO = '{complemento}' WHERE N_CADASTRO={n_cadastro}")
    editar_cliente.close()
    listar_dados_clientes.close()

    if status_cliente == 'A':
        listar_clientes()
    else:
        listar_clientes_inativos()

    banco.commit()


def salvar_pet_editado():
    global status_pet, n_cadastro, nome_pet_antes_alteracao

    nome = editar_pet.lineEdit_2.text()
    contato_dono = editar_pet.lineEdit_3.text()
    idade = editar_pet.lineEdit_4.text()
    porte = editar_pet.lineEdit_5.text()
    sexo = editar_pet.lineEdit_6.text()
    castrado = editar_pet.lineEdit_7.text()
    raca = editar_pet.lineEdit_8.text()

    cursor = banco.cursor()
    comando_SQL = (f"UPDATE TB_PET SET NOME='{nome}',CONTATO_DONO='{contato_dono}',IDADE='{idade}',PORTE='{porte}', SEXO='{sexo}',CASTRADO='{castrado}',RACA='{raca}' WHERE FK_N_CADASTRO='{n_cadastro}' AND NOME ='{nome_pet_antes_alteracao}'")
    cursor.execute(comando_SQL)
    banco.commit()
    editar_pet.close()
    listar_dados_pets.close()

    if status_pet == 'A':
        listar_pets()
    else:
        listar_pets_inativos()


def salvar_produto_editado():
    # pegar o id
    global codigo_barras_valor, status_produto
    # pegar o que foi digitado na linha
    status = editar_produto.lineEdit.text()
    descricao = editar_produto.lineEdit_2.text()
    codigo_barras = editar_produto.lineEdit_3.text()
    preco = editar_produto.lineEdit_4.text()
    fornecedor = editar_produto.lineEdit_5.text()
    marca = editar_produto.lineEdit_6.text()
    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute(
        f"UPDATE TB_PRODUTO SET STATUS = '{status}', DESCRICAO='{descricao}', CODIGO_BARRAS='{codigo_barras}', PRECO='{preco}', FORNECEDOR='{fornecedor}', MARCA='{marca}' WHERE CODIGO_BARRAS={codigo_barras_valor}")
    # fechar e atualizar dados
    editar_produto.close()
    listar_dados_produtos.close()
    if status_produto == 'A':
        listar_produtos()
    else:
        listar_produtos_inativos()


def salvar_servico_editado():
    # pegar o id
    global valor_id_servico
    # pegar o que foi digitado na linha
    descricao = editar_servico.lineEdit_5.text()
    preco = editar_servico.lineEdit_6.text()

    cursor = banco.cursor()
    cursor.execute(f"SELECT STATUS FROM TB_SERVICO WHERE ID = {valor_id_servico}")
    id_lidos = cursor.fetchall()
    valor_status_lido = id_lidos[0][0]

    # atualizar os dados no banco

    try:
        cursor.execute(f"UPDATE TB_SERVICO SET DESCRICAO='{descricao}', PRECO='{preco}' WHERE ID={valor_id_servico}")
        banco.commit()
    # fechar e atualizar dados
    except:

        if (preco != '') and (type(preco) != float()):
            QMessageBox.about(novo_cliente, 'Erro', 'Preço deve ter somente números')
    else:
        editar_servico.close()
        listar_dados_servicos.close()
        if valor_status_lido == 'A':
            listar_servicos()
        else:
            listar_servicos_inativos()


def desativar_ativar_dados_cliente():
    global status_cliente
    linha = listar_dados_clientes.tableWidget.currentRow()
    listar_dados_clientes.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_CLIENTE WHERE STATUS = '{status_cliente}'")
    clientes_lidos = cursor.fetchall()
    n_cadastro_cliente_lido = clientes_lidos[linha][0]
    cursor.execute("SELECT * FROM TB_CLIENTE WHERE N_CADASTRO =" + str(n_cadastro_cliente_lido))
    cliente = cursor.fetchall()

    status_lido = cliente[0][1]

    if status_lido == 'A':
        cursor.execute("UPDATE TB_CLIENTE SET STATUS = 'I' WHERE N_CADASTRO =" + str(n_cadastro_cliente_lido))
        banco.commit()

    elif status_lido == 'I':
        cursor.execute("UPDATE TB_CLIENTE SET STATUS = 'A' WHERE N_CADASTRO =" + str(n_cadastro_cliente_lido))
        banco.commit()


def desativar_ativar_dados_pet():
    global status_pet
    linha = listar_dados_pets.tableWidget.currentRow()
    listar_dados_pets.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_PET WHERE STATUS = '{status_pet}'")
    pets_lidos = cursor.fetchall()
    n_cadastro = pets_lidos[linha][0]
    nome_pet_lido = pets_lidos[linha][2]
    cursor.execute(f"SELECT STATUS FROM TB_PET WHERE FK_N_CADASTRO = {str(n_cadastro)} AND NOME = '{nome_pet_lido}'")
    pet = cursor.fetchall()

    status_lido = pet[0][0]

    if status_lido == 'A':
        cursor.execute(
            f"UPDATE TB_PET SET STATUS = 'I' WHERE FK_N_CADASTRO = {str(n_cadastro)} AND NOME = '{nome_pet_lido}'")
        banco.commit()

    elif status_lido == 'I':
        cursor.execute(
            f"UPDATE TB_PET SET STATUS = 'A' WHERE FK_N_CADASTRO = {str(n_cadastro)} AND NOME = '{nome_pet_lido}'")
        banco.commit()


def desativar_ativar_dados_produto():
    global status_produto
    linha = listar_dados_produtos.tableWidget.currentRow()
    listar_dados_produtos.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_PRODUTO WHERE STATUS = '{status_produto}'")
    produtos_lidos = cursor.fetchall()
    codigo_barras_lido = produtos_lidos[linha][2]
    cursor.execute("SELECT * FROM TB_PRODUTO WHERE CODIGO_BARRAS =" + str(codigo_barras_lido))
    produto = cursor.fetchall()

    status_lido = produto[0][0]

    if status_lido == 'A':
        cursor.execute("UPDATE TB_PRODUTO SET STATUS = 'I' WHERE CODIGO_BARRAS =" + str(codigo_barras_lido))
        banco.commit()

    elif status_lido == 'I':
        cursor.execute("UPDATE TB_PRODUTO SET STATUS = 'A' WHERE CODIGO_BARRAS =" + str(codigo_barras_lido))
        banco.commit()


def desativar_ativar_dados_servico():
    global status_servico
    linha = listar_dados_servicos.tableWidget.currentRow()
    listar_dados_servicos.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_SERVICO WHERE STATUS = '{status_servico}'")
    id_lidos = cursor.fetchall()
    id_valor = id_lidos[linha][0]
    cursor.execute("SELECT * FROM TB_SERVICO WHERE ID =" + str(id_valor))
    servico = cursor.fetchall()

    status_lido = servico[0][1]

    if status_lido == 'A':
        cursor.execute("UPDATE TB_SERVICO SET STATUS = 'I' WHERE ID =" + str(id_valor))
        banco.commit()

    elif status_lido == 'I':
        cursor.execute("UPDATE TB_SERVICO SET STATUS = 'A' WHERE ID =" + str(id_valor))
        banco.commit()


def gerar_pdf_produto():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_PRODUTO"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Produtos_cadastrados.pdf")
    pdf.setFont("Times-Bold", 12)
    pdf.drawString(200, 800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 12)

    pdf.drawString(5, 750, "ID")
    pdf.drawString(40, 750, "DESCRIÇÃO")
    pdf.drawString(160, 750, "C. DE BARRA")
    pdf.drawString(280, 750, "PREÇO")
    pdf.drawString(360, 750, "FORNECEDOR")
    pdf.drawString(520, 750, "MARCA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(5, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(60, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(180, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(280, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(390, 750 - y, str(dados_lidos[i][4]))
        pdf.drawString(530, 750 - y, str(dados_lidos[i][5]))

    pdf.save()
    QMessageBox.about(listar_dados_produtos, 'Ação Realizada', 'PDF gerado com sucesso.')


def gerar_pdf_servico():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_SERVICO"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Serviços_cadastrados.pdf")
    pdf.setFont("Times-Bold", 12)
    pdf.drawString(200, 800, "Serviços cadastrados:")
    pdf.setFont("Times-Bold", 12)

    pdf.drawString(5, 750, "ID")
    pdf.drawString(40, 750, "DESCRIÇÃO")
    pdf.drawString(160, 750, "PREÇO")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(5, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(60, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(180, 750 - y, str(dados_lidos[i][2]))

    pdf.save()
    QMessageBox.about(listar_dados_servicos, 'Ação Realizada', 'PDF gerado com sucesso.')


def contratar_plano_servico():
    contato = plano_serviço.lineEdit_.text()
    plano = ''
    forma_pagamento = ''
    data_contracao = ''
    data_debito = ''


    if plano_serviço.radioButton.isChecked():
        plano = 'Mensal'
    elif plano_serviço.radioButton_2.isChecked():
        plano = 'Semestral'
    elif plano_serviço.radioButton_3.isChecked():
        plano = 'Anual'

    if plano_serviço.radioButton_4.isChecked():
        forma_pagamento = 'Crédito'
    elif plano_serviço.radioButton_5.isChecked():
        forma_pagamento = 'Débito'
    elif plano_serviço.radioButton_6.isChecked():
        forma_pagamento = 'Dinheiro'

    try:
        cursor = banco.cursor()
        comando_SQL = (f"UPDATE TB_CLIENTE SET PLANO_SERVICO='{plano_serviço}', DATA_CONTRATACAO='{data_contracao}', DATA_DEBITO='{data_debito}', FORMA_PAGAMENTO='{forma_pagamento}'  WHERE CONTATO='{contato}';")
        cursor.execute(comando_SQL)
        banco.commit()
        QMessageBox.about(plano_serviço, 'Ação Realizada', 'Plano contratado com sucesso.')

    except:
        # se o campo obrigató contato for vazio imprimir essa mensagem
        if contato == '' and plano == '' and forma_pagamento == '' and data_contracao == '' and data_debito == '':
            QMessageBox.about(novo_cliente, 'Erro', 'Campos obrigatórios não foram preenchidos.')

        # if contato != '' and (type(contato) == int()):
        #     cursor1 = banco.cursor()
        #     verifica_chave = (f'SELECT * FROM TB_CLIENTE WHERE CONTATO = {contato};')
        #     cursor1.execute(verifica_chave)
        #     dados_lidos = cursor1.fetchall()
        #     valor_lido = dados_lidos
        #     if len(dados_lidos) > 0:
        #         QMessageBox.about(novo_cliente, 'Erro', 'Já existe regisro para esse contato')

    else:
        plano_serviço.lineEdit.setText("")


# Verificar se existe algum pet para o nº de cadastro informado
def verifica_buscar_pet():
    listar_pets_agendamento.show()
    n_cadastro = novo_agendamento.lineEdit_17.text()

    cursor = banco.cursor()
    comando_SQL = (
        f"SELECT * FROM TB_PET WHERE STATUS = 'A' AND FK_N_CADASTRO = '{n_cadastro}'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    if len(dados_lidos) < 1:
        QMessageBox.about(novo_agendamento, 'Atenção', 'Nenhum Pet encontrado para o nºde cadastro informado.')

    elif len(dados_lidos) > 0 and n_cadastro != '':
        buscar_pet()

# Função chamada por verifica_buscar_pet
def buscar_pet():
    global status_pet, n_cadastro
    n_cadastro = novo_agendamento.lineEdit_17.text()

    cursor = banco.cursor()
    comando_SQL = (f"SELECT STATUS, NOME, CONTATO_DONO, IDADE, PORTE, SEXO, CASTRADO, RACA FROM TB_PET WHERE STATUS = 'A' AND FK_N_CADASTRO = '{n_cadastro}'")
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_pets_agendamento.tableWidget.setRowCount(len(dados_lidos))
    listar_pets_agendamento.tableWidget.setColumnCount(8)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 8):
            listar_pets_agendamento.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    status_pet = 'A'

# preenche os dados do pet na tela de novo agendamento
def exibe_dados_pet_agendamento():
    global status_pet, n_cadastro, nome_pet
    linha = listar_pets_agendamento.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_PET WHERE STATUS = '{status_pet}' AND FK_N_CADASTRO = '{n_cadastro}'")
    pets_listados = cursor.fetchall()
    nome_pet = pets_listados[linha][2]
    cursor.execute(f"SELECT * FROM TB_PET WHERE FK_N_CADASTRO = '{n_cadastro}' AND NOME = '{nome_pet}'")
    pet = cursor.fetchall()


    listar_pets_agendamento.close()
    novo_agendamento.show()
    #Dados do Pet
    novo_agendamento.lineEdit_2.setText(str(pet[0][3]))
    novo_agendamento.lineEdit_3.setText(str(pet[0][2]))
    novo_agendamento.lineEdit_4.setText(str(pet[0][4]))
    novo_agendamento.lineEdit_5.setText(str(pet[0][5]))
    novo_agendamento.lineEdit_6.setText(str(pet[0][6]))
    novo_agendamento.lineEdit_8.setText(str(pet[0][7]))
    novo_agendamento.lineEdit_7.setText(str(pet[0][8]))

#busca o id e descrição da tosa e joga na tela de novo agendamento
def pegar_descricao_id_tosa_novo_agendamento():
    buscar_tipos_tosa()
    listar_servicos_agendamento.pushButton.clicked.connect(exibe_tipos_tosa)


#busca o id e descrição da tosa e joga na tela de editar agendamento
def pegar_descricao_id_tosa_editar_agendamento():
    buscar_tipos_tosa()
    listar_servicos_agendamento.pushButton.clicked.connect(exibe_tipos_tosa_edicao)


# busca todos os serviçõs que começam com a letra T
def buscar_tipos_tosa():
    listar_servicos_agendamento.show()

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_SERVICO WHERE STATUS = 'A' AND  DESCRICAO LIKE 'T%';")
    dados_lidos = cursor.fetchall()

    listar_servicos_agendamento.tableWidget.setRowCount(len(dados_lidos))
    listar_servicos_agendamento.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            listar_servicos_agendamento.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


# exibe na tela de novo agendamento
def exibe_tipos_tosa():
    linha = listar_servicos_agendamento.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_SERVICO WHERE STATUS = 'A' AND  DESCRICAO LIKE 'T%';")
    servico_listados = cursor.fetchall()
    id_servico = servico_listados[linha][0]
    cursor.execute(f"SELECT * FROM TB_SERVICO WHERE ID = '{id_servico}'")
    id_descricao_tosa = cursor.fetchall()

    listar_servicos_agendamento.close()
    novo_agendamento.lineEdit_11.setText(str(id_descricao_tosa[0][2]))
    novo_agendamento.lineEdit_16.setText(str(id_descricao_tosa[0][0]))


#exibe na tela de edição do agendamento
def exibe_tipos_tosa_edicao():
    linha = listar_servicos_agendamento.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_SERVICO WHERE STATUS = 'A' AND  DESCRICAO LIKE 'T%';")
    servico_listados = cursor.fetchall()
    id_servico = servico_listados[linha][0]
    cursor.execute(f"SELECT * FROM TB_SERVICO WHERE ID = '{id_servico}'")
    servico = cursor.fetchall()

    listar_servicos_agendamento.close()
    editar_agendamento.lineEdit_11.setText(str(servico[0][2]))
    editar_agendamento.lineEdit_16.setText(str(servico[0][0]))


def exibir_data_novo_agendamento():
    global data_para_insert
    data = str(novo_agendamento.calendarWidget.selectedDate())
    retirar_parentese1 = data.split('(')

    sem_parentese1 = retirar_parentese1[1]

    retirar_parentese2 = sem_parentese1.split(')')
    sem_parentese2 = retirar_parentese2[0]

    retirar_virgula = sem_parentese2.split(',')

    dia = retirar_virgula[2]
    mes = retirar_virgula[1]
    ano = retirar_virgula[0]

    dia = dia.strip(' ')
    mes = mes.strip(' ')
    ano = ano.strip(' ')

    data_para_insert = (f'{ano}-{mes}-{dia}')
    data_exibida = (f'{dia}/{mes}/{ano}')
    novo_agendamento.label_20.setText(data_exibida)


def exibir_data_editar_agendamento():
    global data_para_insert_editar_agendamento
    data = str(editar_agendamento.calendarWidget.selectedDate())
    retirar_parentese1 = data.split('(')

    sem_parentese1 = retirar_parentese1[1]

    retirar_parentese2 = sem_parentese1.split(')')
    sem_parentese2 = retirar_parentese2[0]

    retirar_virgula = sem_parentese2.split(',')

    dia = retirar_virgula[2]
    mes = retirar_virgula[1]
    ano = retirar_virgula[0]

    dia = dia.strip(' ')
    mes = mes.strip(' ')
    ano = ano.strip(' ')

    data_para_insert_editar_agendamento = (f'{ano}-{mes}-{dia}')
    data_exibida = (f'{dia}/{mes}/{ano}')
    editar_agendamento.label_22.setText(data_exibida)


def adicionar_novo_agendamento():
    global data_para_insert, id_descricao_tosa
    n_cadastro = novo_agendamento.lineEdit_17.text()
    nome_pet = novo_agendamento.lineEdit_3.text()
    contato = novo_agendamento.lineEdit_2.text()
    idade = novo_agendamento.lineEdit_4.text()
    porte = novo_agendamento.lineEdit_5.text()
    sexo = novo_agendamento.lineEdit_6.text()
    castrado = novo_agendamento.lineEdit_8.text()
    raca = novo_agendamento.lineEdit_7.text()

    tipo_tosa = novo_agendamento.lineEdit_11.text()
    id_tosa = novo_agendamento.lineEdit_16.text()
    observacao = novo_agendamento.lineEdit_19.text()

    hora = novo_agendamento.lineEdit_18.text()
    hora = (f'{hora}:00')

    banho = 'N'
    tosa = 'N'
    taxi_pet = 'N'
    unhas = 'N'

    if novo_agendamento.checkBox.isChecked():
        banho = 'S'
    if novo_agendamento.checkBox_2.isChecked():
        tosa = 'S'
    if novo_agendamento.checkBox_4.isChecked():
        taxi_pet = 'S'
    if novo_agendamento.checkBox_3.isChecked():
        unhas = 'S'

    try:
        cursor = banco.cursor()
        comando_SQL = (f"INSERT INTO TB_AGENDAMENTO (N_CADASTRO, NOME_PET, DATA, HORA, BANHO, TOSA, TAXI_PET, UNHAS, ID_TOSA, TIPO_TOSA, OBSERVACAO, CONTATO_DONO, IDADE, PORTE, SEXO, CASTRADO, RACA) VALUES ('{n_cadastro}','{nome_pet}','{data_para_insert}','{hora}','{banho}','{tosa}','{taxi_pet}','{unhas}','{id_tosa}','{tipo_tosa}','{observacao}','{contato}','{idade}','{porte}','{sexo}','{castrado}','{raca}')")
        cursor.execute(comando_SQL)
        banco.commit()

        QMessageBox.about(novo_agendamento, 'Ação Realizada', 'Agendamento adicionado com sucesso.')
        adicionar_agendamento_na_agenda(n_cadastro, nome_pet, data_para_insert, hora)
        chamar_funcoes_home()

    except:
        # se o campo obrigató contato for vazio imprimir essa mensagem
        if n_cadastro == '' or nome_pet == '':
            QMessageBox.about(novo_agendamento, 'Erro', 'Campos obrigatórios não foram preenchidos.')

    # Após passar pelo except ele vai executar esse bloco
    else:
        novo_agendamento.lineEdit_17.setText("")
        novo_agendamento.lineEdit_3.setText("")
        novo_agendamento.lineEdit_2.setText("")
        novo_agendamento.lineEdit_4.setText("")
        novo_agendamento.lineEdit_5.setText("")
        novo_agendamento.lineEdit_6.setText("")
        novo_agendamento.lineEdit_8.setText("")
        novo_agendamento.lineEdit_7.setText("")
        novo_agendamento.lineEdit_11.setText("")
        novo_agendamento.lineEdit_16.setText("")
        novo_agendamento.lineEdit_18.setText("")
        novo_agendamento.lineEdit_19.setText("")


def adicionar_agendamento_na_agenda(n_cadastro, nome_pet, data, hora):
    cursor = banco.cursor()
    cursor.execute(f"SELECT ID FROM TB_AGENDAMENTO WHERE STATUS = 'A' AND N_CADASTRO = '{n_cadastro}' AND NOME_PET = '{nome_pet}' AND DATA = '{data}' AND HORA = '{hora}';")
    dados_lidos = cursor.fetchall()
    id_agendamento = dados_lidos[0][0]
    cursor.execute(f"INSERT INTO TB_AGENDA (FK_ID_AGENDAMENTO, NOME_PET, DATA, HORA) VALUES ('{id_agendamento}','{nome_pet}','{data}','{hora}')")
    banco.commit()


def listar_agenda():
    global status_agenda
    listar_dados_agenda.show()

    cursor = banco.cursor()
    cursor.execute(f"SELECT DATE_FORMAT(DATA,'%d/%m'), TIME_FORMAT(HORA, '%h:%i'), NOME_PET FROM TB_AGENDA ORDER BY DATA;")

    dados_lidos = cursor.fetchall()

    listar_dados_agenda.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_agenda.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            listar_dados_agenda.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    status_agenda = 'A'

def listar_agenda_home():
    global status_agenda

    cursor = banco.cursor()
    data_atual = datetime.today().strftime('%Y-%m-%d')
    cursor.execute(f"SELECT DATE_FORMAT(DATA,'%d/%m'), TIME_FORMAT(HORA, '%h:%i'), NOME_PET FROM TB_AGENDA WHERE STATUS = 'A' AND DATA = '{data_atual}' ORDER BY HORA ASC")

    dados_lidos = cursor.fetchall()

    home.tableWidget.setRowCount(len(dados_lidos))
    home.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            home.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    status_agenda = 'A'


def alterar_status_agendamento_finalizado():
    global id_valor_lido

    cursor = banco.cursor()
    cursor.execute(f"UPDATE TB_AGENDAMENTO SET STATUS = 'I' WHERE ID ='{id_valor_lido}'")
    banco.commit()
    cursor.execute(f"UPDATE TB_AGENDA SET STATUS = 'I' WHERE FK_ID_AGENDAMENTO ='{id_valor_lido}'")
    banco.commit()

def listar_agenda_finalizados():
    global status_agenda
    listar_dados_agenda.show()
    cursor = banco.cursor()
    cursor.execute(f"SELECT DATE_FORMAT(DATA,'%d/%m'), TIME_FORMAT(HORA, '%h:%i'), NOME_PET FROM TB_AGENDA WHERE STATUS = 'I'ORDER BY DATA;")

    dados_lidos = cursor.fetchall()

    listar_dados_agenda.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_agenda.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            listar_dados_agenda.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    status_agenda = 'I'


def listar_agendamento():
    global status_agenda, dados_editar_agendamento, id_valor_lido
    linha = listar_dados_agenda.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT FK_ID_AGENDAMENTO FROM TB_AGENDA WHERE STATUS = '{status_agenda}'")
    id_agendamento_lido = cursor.fetchall()
    id_valor_lido = id_agendamento_lido[linha][0]
    cursor.execute(f"SELECT * FROM TB_AGENDAMENTO WHERE ID = '{str(id_valor_lido)}'")
    agendamento = cursor.fetchall()
    cursor.execute(f"SELECT DATE_FORMAT(STR_TO_DATE(DATA, '%Y-%m-%d'), '%d/%m/%Y') FROM TB_AGENDAMENTO WHERE ID = '{str(id_valor_lido)}';")
    data_agendamento = cursor.fetchall()
    cursor.execute(f"SELECT CEP, BAIRRO, LOGRADOURO, NUMERO, COMPLEMENTO FROM TB_CLIENTE WHERE N_CADASTRO = '{str(agendamento[0][2])}'")
    cliente = cursor.fetchall()
    #pegar id, status e n_cadastro para mandar para a função editar agendamento
    dados_editar_agendamento = [agendamento[0][0], agendamento[0][1], agendamento[0][2]]
    dados_finalizar_agendamento = agendamento
    listar_dados_agendamento.show()

    #Id, nºcadastro
    listar_dados_agendamento.label_34.setText(str(agendamento[0][0]))
    listar_dados_agendamento.label_35.setText(str(agendamento[0][2]))
    # nome pet, contato
    listar_dados_agendamento.label_41.setText(str(agendamento[0][3]))
    listar_dados_agendamento.label_37.setText(str(agendamento[0][13]))
    # Idade, porte, sexo, castrado, raça
    listar_dados_agendamento.label_38.setText(str(agendamento[0][14]))
    listar_dados_agendamento.label_42.setText(str(agendamento[0][15]))
    listar_dados_agendamento.label_43.setText(str(agendamento[0][16]))
    listar_dados_agendamento.label_44.setText(str(agendamento[0][17]))
    listar_dados_agendamento.label_39.setText(str(agendamento[0][18]))
    # Banho, tosa, taxi pet, unhas, id_tosa, tipo_tosa
    listar_dados_agendamento.label_27.setText(str(agendamento[0][6]))
    listar_dados_agendamento.label_29.setText(str(agendamento[0][7]))
    listar_dados_agendamento.label_26.setText(str(agendamento[0][8]))
    listar_dados_agendamento.label_28.setText(str(agendamento[0][9]))
    listar_dados_agendamento.label_36.setText(str(agendamento[0][10]))
    listar_dados_agendamento.label_57.setText(str(agendamento[0][11]))
    # data, hora
    listar_dados_agendamento.label_25.setText(str(data_agendamento[0][0]))
    listar_dados_agendamento.label_30.setText(str(agendamento[0][5]))
    #obs
    listar_dados_agendamento.label_56.setText(str(agendamento[0][12]))
    #Cep, bairro, logradouro, completemento, número
    listar_dados_agendamento.label_51.setText(str(cliente[0][0]))
    listar_dados_agendamento.label_52.setText(str(cliente[0][1]))
    listar_dados_agendamento.label_53.setText(str(cliente[0][2]))
    listar_dados_agendamento.label_55.setText(str(cliente[0][3]))
    listar_dados_agendamento.label_54.setText(str(cliente[0][4]))

#preciso finalizar
def editar_dados_agendamento():
    #dados_editar_agendamento vem da função listar_agendamento, não sendo necessário fazer select novamente
    global dados_editar_agendamento

    editar_agendamento.show()
    editar_agendamento.label_35.setText(str(dados_editar_agendamento[2]))
    editar_agendamento.label_34.setText(str(dados_editar_agendamento[0]))
    editar_agendamento.label_36.setText(str(dados_editar_agendamento[1]))


def salvar_agendamento_editado():
    global data_para_insert_editar_agendamento, dados_editar_agendamento

    id_agendamento = dados_editar_agendamento[0]
    hora = editar_agendamento.lineEdit_18.text()
    banho = editar_agendamento.lineEdit_3.text()
    tosa = editar_agendamento.lineEdit_4.text()
    taxi_pet = editar_agendamento.lineEdit_5.text()
    unhas = editar_agendamento.lineEdit_3.text()
    tipo_tosa = editar_agendamento.lineEdit_11.text()
    id_tosa = editar_agendamento.lineEdit_16.text()
    observacao = editar_agendamento.lineEdit_7.text()

    try:
        cursor = banco.cursor()
        # comando sql sem banho, tosa, taxi_pet e unhas
        comando_Sql = (f"UPDATE TB_AGENDAMENTO SET DATA = '{data_para_insert_editar_agendamento}',HORA = '{hora}', TIPO_TOSA = '{tipo_tosa}', ID_TOSA = '{id_tosa}', OBSERVACAO = '{observacao}' WHERE ID = '{id_agendamento}'")

        if banho.upper() != '' and (banho.upper() == 'A' or banho.upper() == 'N'):
            comando_Sql = (f"UPDATE TB_AGENDAMENTO SET DATA = '{data_para_insert_editar_agendamento}',HORA = '{hora}', BANHO ='{banho.upper()}', TIPO_TOSA = '{tipo_tosa}', ID_TOSA = '{id_tosa}', OBSERVACAO = '{observacao}' WHERE ID = '{id_agendamento}'")

        elif tosa.upper() != '' and (tosa.upper() == 'A' or tosa.upper() == 'N'):
            comando_Sql = (f"UPDATE TB_AGENDAMENTO SET DATA = '{data_para_insert_editar_agendamento}',HORA = '{hora}', BANHO ='{banho.upper()}', TOSA = '{tosa.upper()}', TIPO_TOSA = '{tipo_tosa}', ID_TOSA = '{id_tosa}', OBSERVACAO = '{observacao}' WHERE ID = '{id_agendamento}'")

        elif taxi_pet.upper() != '' and (taxi_pet.upper() == 'A' or taxi_pet.upper() == 'N'):
            comando_Sql = (f"UPDATE TB_AGENDAMENTO SET DATA = '{data_para_insert_editar_agendamento}',HORA = '{hora}', BANHO ='{banho.upper()}', TOSA = '{tosa.upper()}', TAXI_PET ='{taxi_pet.upper()}', TIPO_TOSA = '{tipo_tosa}', ID_TOSA = '{id_tosa}', OBSERVACAO = '{observacao}' WHERE ID = '{id_agendamento}'")

        elif unhas.upper() != '' and (unhas.upper() == 'A' or unhas.upper() == 'N'):
            comando_Sql = (f"UPDATE TB_AGENDAMENTO SET DATA = '{data_para_insert_editar_agendamento}',HORA = '{hora}', BANHO ='{banho.upper()}', TOSA = '{tosa.upper()}', TAXI_PET ='{taxi_pet.upper()}', UNHAS= '{unhas.upper()}', TIPO_TOSA = '{tipo_tosa}', ID_TOSA = '{id_tosa}', OBSERVACAO = '{observacao}' WHERE ID = '{id_agendamento}'")

        cursor.execute(comando_Sql)
        banco.commit()

        cursor.execute(f"UPDATE TB_AGENDA SET DATA = '{data_para_insert_editar_agendamento}',HORA = '{hora}' WHERE FK_ID_AGENDAMENTO ='{id_agendamento}'")
        banco.commit()
        QMessageBox.about(editar_agendamento, 'Ação realizada', 'Agendamento atualizado com sucesso.')

    except:
        QMessageBox.about(editar_agendamento, 'Erro', 'Uma data deve ser selecionada.')

    else:
        editar_agendamento.close()
        listar_dados_agendamento.close()
        listar_dados_agenda.close()
        listar_dados_agenda.show()
        chamar_funcoes_home()

#vai em listar produtos e joga o produto selecionado na tela de baixa agendamento
def adicionar_produto_baixa_agendamento():
    global contador_linha_produto_servico
    contador_linha_produto_servico = contador_linha_produto_servico + 1
    finalizar_agendamento.tableWidget.setRowCount(contador_linha_produto_servico)

    # ira listar todos os produtos
    buscar_produto_baixa_agendamento()



# ira listar todos os produtos
def buscar_produto_baixa_agendamento():
    listar_produtos_baixa_agendamento.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT DESCRICAO, PRECO FROM TB_PRODUTO WHERE STATUS = 'A'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_produtos_baixa_agendamento.tableWidget.setRowCount(len(dados_lidos))
    listar_produtos_baixa_agendamento.tableWidget.setColumnCount(2)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 2):
            listar_produtos_baixa_agendamento.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

# ira pegar a descricao e preço e jogar na tela de finalização de agendamento
def buscar_produto_baixa_agendamento_2():
    global valor_total, lista_produtos_servicos
    linha = listar_produtos_baixa_agendamento.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT DESCRICAO, PRECO FROM TB_PRODUTO WHERE STATUS = 'A'")
    produtos_listados = cursor.fetchall()
    descricao_produto = produtos_listados[linha][0]

    cursor.execute(f"SELECT DESCRICAO, PRECO FROM TB_PRODUTO WHERE DESCRICAO LIKE '{descricao_produto}'")
    descricao_preco_produto = cursor.fetchall()

    lista_produtos_servicos.append((descricao_preco_produto[0][0], descricao_preco_produto[0][1]))

    for i in range(0, len(lista_produtos_servicos)):
        for j in range(0, 2):
            finalizar_agendamento.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista_produtos_servicos[i][j])))

    valor_total = valor_total + descricao_preco_produto[0][1]
    finalizar_agendamento.label_38.setText(str(valor_total))

    listar_produtos_baixa_agendamento.close()

# chama função buscar_servico_baixa_agendamento e buscar_servico_baixa_agendamento_2
def adicionar_servico_baixa_agendamento():
    global contador_linha_produto_servico
    contador_linha_produto_servico = contador_linha_produto_servico + 1
    finalizar_agendamento.tableWidget.setRowCount(contador_linha_produto_servico)

    # ira listar todos os produtos
    buscar_servico_baixa_agendamento()

# ira listar todos os servicos
def buscar_servico_baixa_agendamento():
    listar_servicos_baixa_agendamento.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT DESCRICAO, PRECO FROM TB_SERVICO WHERE STATUS = 'A'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_servicos_baixa_agendamento.tableWidget.setRowCount(len(dados_lidos))
    listar_servicos_baixa_agendamento.tableWidget.setColumnCount(2)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 2):
            listar_servicos_baixa_agendamento.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

# ira pegar a descricao e preço e jogar na tela de finalização de agendamento
def buscar_servico_baixa_agendamento_2():
    global valor_total, lista_produtos_servicos
    linha = listar_servicos_baixa_agendamento.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT DESCRICAO, PRECO FROM TB_SERVICO WHERE STATUS = 'A'")
    servicos_listados = cursor.fetchall()
    descricao_servico = servicos_listados[linha][0]

    cursor.execute(f"SELECT DESCRICAO, PRECO FROM TB_SERVICO WHERE DESCRICAO LIKE '{descricao_servico}'")
    descricao_preco_servico = cursor.fetchall()

    lista_produtos_servicos.append((descricao_preco_servico[0][0], descricao_preco_servico[0][1]))

    for i in range(0, len(lista_produtos_servicos)):
        for j in range(0, 2):
            finalizar_agendamento.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista_produtos_servicos[i][j])))

    valor_total = valor_total + descricao_preco_servico[0][1]
    finalizar_agendamento.label_38.setText(str(valor_total))

    listar_servicos_baixa_agendamento.close()

def remover_item_finalizacao_agendamento():
    global valor_total, lista_produtos_servicos
    linha = finalizar_agendamento.tableWidget.currentRow()

    valor_total = valor_total - lista_produtos_servicos[linha][1]
    finalizar_agendamento.label_38.setText(str(valor_total))
    finalizar_agendamento.tableWidget.removeRow(linha)

def chamar_finalizar_dados_agendamento():
    global id_valor_lido, contador_linha_produto_servico, valor_total, lista_produtos_servicos
    listar_dados_agendamento.close()
    finalizar_agendamento.show()

    id = id_valor_lido
    contador_linha_produto_servico = 0
    valor_total = 0
    lista_produtos_servicos = []
    listar_produtos_baixa_agendamento.tableWidget.setColumnCount(2)
    finalizar_agendamento.tableWidget.setRowCount(contador_linha_produto_servico)

    cursor = banco.cursor()
    cursor.execute(f"SELECT N_CADASTRO, NOME_PET, DATE_FORMAT(DATA,'%d/%m'), TIME_FORMAT(HORA, '%h:%i')  FROM TB_AGENDAMENTO WHERE ID = '{str(id)}' ORDER BY DATA")
    dados_agendamento = cursor.fetchall()

    # id, NºCadastro, Nome Pet
    finalizar_agendamento.label_34.setText(str(id))
    finalizar_agendamento.label_35.setText(str(dados_agendamento[0][0]))
    finalizar_agendamento.label_41.setText(str(dados_agendamento[0][1]))
    # Data, Hora
    finalizar_agendamento.label_25.setText(str(dados_agendamento[0][2]))
    finalizar_agendamento.label_30.setText(str(dados_agendamento[0][3]))


def finalizar_dados_agendamento():
    global lista_produtos_servicos, valor_total, id_valor_lido
    forma_pagamento = finalizar_agendamento.comboBox.currentText()
    lista = ''
    # tirar os valores da lista e colocar em uma string para fazer insert no banco
    for i in lista_produtos_servicos:
        lista = lista + i[0] + '='
        lista = lista + str(i[1]) + '--'

    try:
        cursor = banco.cursor()
        cursor.execute(f"INSERT INTO TB_BAIXA_AGENDAMENTO (ID_AGENDAMENTO, DESCRICAO_PRECO, VALOR_TOTAL, FORMA_PAGAMENTO) VALUES ('{id_valor_lido}','{lista}','{valor_total}','{str(forma_pagamento)}')")
        banco.commit()

        QMessageBox.about(finalizar_agendamento, 'Ação Realizada', 'Agendamento finalizado com sucesso.')

    except:
        # se o campo obrigató contato for vazio imprimir essa mensagem
        if lista_produtos_servicos == [] or valor_total == 0:
            QMessageBox.about(finalizar_agendamento, 'Erro', 'Campos obrigatórios não foram preenchidos.')

    else:
        finalizar_agendamento.label_38.setText('')
        alterar_status_agendamento_finalizado()
        finalizar_agendamento.close()
        listar_dados_agenda.close()
        chamar_funcoes_home()




app = QtWidgets.QApplication([])

home = uic.loadUi('Home.ui')
home.actionNovo_Cliente_Pet.triggered.connect(chamar_novo_cliente)
home.actionNovo_Produto_Servi_o.triggered.connect(chamar_novo_produto_servico)
home.actionContratar_Plano_de_Servi_o.triggered.connect(chamar_plano_serviço)

home.actionNovo_Agendamento.triggered.connect(chamar_novo_agendamento)
home.actionAgendamentos.triggered.connect(chamar_agenda)
home.actionAgenda_Finalizados.triggered.connect(chamar_agenda_finalizados)

login_tela = uic.loadUi('Login.ui')
chamar_funcoes_login()



novo_agendamento = uic.loadUi('Novo Agendamento.ui')

novo_cliente = uic.loadUi('Novo Cliente.ui')

novo_produto_serviço = uic.loadUi('Novo Produto e Serviço.ui')

plano_serviço = uic.loadUi('Contratar Plano Serviço.ui')

listar_dados_clientes = uic.loadUi('Listar Dados Clientes.ui')

listar_dados_pets = uic.loadUi('Listar Dados Pets.ui')

listar_dados_produtos = uic.loadUi('Listar Dados Produtos.ui')

listar_dados_servicos = uic.loadUi('Listar Dados Servicos.ui')

listar_dados_agendamento = uic.loadUi('Listar Dados Agendamento.ui')

editar_cliente = uic.loadUi('Editar Cliente.ui')

editar_pet = uic.loadUi('Editar Pet.ui')

editar_produto = uic.loadUi('Editar Produto.ui')

editar_servico = uic.loadUi('Editar Servico.ui')

editar_agendamento = uic.loadUi('Editar Agendamento.ui')

listar_pets_agendamento = uic.loadUi('Listar Pets Agendamento.ui')

listar_servicos_agendamento = uic.loadUi('Listar Servicos Agendamento.ui')

listar_dados_agenda = uic.loadUi('Agenda.ui')

finalizar_agendamento = uic.loadUi('Finalizar Agendamento.ui')

listar_produtos_baixa_agendamento = uic.loadUi('Listar Produtos Baixa Agendamento.ui')

listar_servicos_baixa_agendamento = uic.loadUi('Listar Servicos Baixa Agendamento.ui')
app.exec()

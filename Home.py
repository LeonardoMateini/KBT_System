from mysql.connector import connection
from reportlab.pdfgen import canvas
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database="DB_KBT_SYSTEM"
)
# cursor = banco.cursor()
# comando_SQL = """create table TB_SERVICO (
# 	ID INT NOT NULL AUTO_INCREMENT,
# 	STATUS CHAR(1) DEFAULT 'A',
# 	DESCRICAO varchar (50) NOT NULL,
# 	PRECO DOUBLE,
# 	PRIMARY KEY (id)
# );"""
# cursor.execute(comando_SQL)
# banco.commit()

def chamar_cadastro():
    ambiente_cadastro.show()
    ambiente_cadastro.pushButton_3.clicked.connect(chamar_novo_cliente)
    ambiente_cadastro.pushButton_5.clicked.connect(chamar_novo_produto_servico)
    ambiente_cadastro.pushButton_7.clicked.connect(chamar_plano_serviço)


def chamar_novo_cliente():
    novo_cliente.show()
    novo_cliente.pushButton_2.clicked.connect(adicionar_cliente)
    novo_cliente.pushButton.clicked.connect(adicionar_pet)
    novo_cliente.pushButton_3.clicked.connect(listar_clientes)
    novo_cliente.pushButton_4.clicked.connect(listar_clientes_inativos)
    novo_cliente.pushButton_5.clicked.connect(listar_pets)
    novo_cliente.pushButton_6.clicked.connect(listar_pets_inativos)

    listar_dados_clientes.pushButton_2.clicked.connect(desativar_ativar_dados_cliente)
    listar_dados_pets.pushButton_2.clicked.connect(desativar_ativar_dados_pet)

def chamar_agenda():
    ambiente_agenda.show()
    ambiente_agenda.pushButton_2.clicked.connect(chamar_novo_agendamento)


def chamar_novo_agendamento():
    novo_agendamento.show()


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


def adicionar_cliente():
    nome = novo_cliente.lineEdit_2.text()
    contato = novo_cliente.lineEdit_3.text()
    cep = novo_cliente.lineEdit_4.text()
    bairro = novo_cliente.lineEdit_5.text()
    logradouro = novo_cliente.lineEdit_6.text()
    numero = novo_cliente.lineEdit_8.text()
    complemento = novo_cliente.lineEdit_7.text()

    try:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO TB_CLIENTE (NOME, CONTATO, BAIRRO, LOGRADOURO, COMPLEMENTO) VALUES (%s,%s,%s,%s,%s)"
        dados = (str(nome), contato, str(bairro), str(logradouro), str(complemento))

        if cep != '' and numero != '':
            comando_SQL = "INSERT INTO TB_CLIENTE (NOME, CONTATO, CEP, BAIRRO, LOGRADOURO, NUMERO, COMPLEMENTO) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            dados = (str(nome), str(contato), cep, str(bairro), str(logradouro), numero, str(complemento))

        elif cep == '' and numero !='':
            comando_SQL = "INSERT INTO TB_CLIENTE (NOME, CONTATO, BAIRRO, LOGRADOURO, NUMERO, COMPLEMENTO) VALUES (%s,%s,%s,%s,%s,%s)"
            dados = (str(nome), str(contato), str(bairro), str(logradouro), numero, str(complemento))

        elif cep != '' and numero == '':
            comando_SQL = "INSERT INTO TB_CLIENTE (NOME, CONTATO, CEP, BAIRRO, LOGRADOURO, COMPLEMENTO) VALUES (%s,%s,%s,%s,%s,%s)"
            dados = (str(nome), str(contato), cep, str(bairro), str(logradouro), str(complemento))

        cursor.execute(comando_SQL, dados)
        banco.commit()

        QMessageBox.about(novo_cliente, 'Ação Realizada', 'Cliente cadastrado com sucesso.')


    except:
        #se o campo obrigató contato for vazio imprimir essa mensagem
        if contato == '' or nome == '':
            QMessageBox.about(novo_cliente, 'Erro', 'Campos obrigatórios não foram preenchidos.')

        if contato != '' and (type(contato) == int()):
            cursor1 = banco.cursor()
            verifica_chave = (f'SELECT * FROM TB_CLIENTE WHERE CONTATO = {contato};')
            cursor1.execute(verifica_chave)
            dados_lidos = cursor1.fetchall()
            valor_lido = dados_lidos
            if len(dados_lidos) > 0:
                QMessageBox.about(novo_cliente, 'Erro', 'Já existe regisro para esse contato')

        if (contato != '') and (type(contato) != int()):
            QMessageBox.about(novo_cliente, 'Erro', 'Contato deve ter somente números')

    #Após passar pelo except ele vai executar esse bloco
    else:
        novo_cliente.lineEdit_2.setText("")
        novo_cliente.lineEdit_3.setText("")
        novo_cliente.lineEdit_4.setText("")
        novo_cliente.lineEdit_5.setText("")
        novo_cliente.lineEdit_6.setText("")
        novo_cliente.lineEdit_8.setText("")
        novo_cliente.lineEdit_7.setText("")

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
        castrado = 'S'
    elif novo_cliente.radioButton_10.isChecked():
        castrado = 'N'

    try:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO TB_PET (NOME, FK_CONTATO_DONO, IDADE, PORTE, SEXO, CASTRADO, RACA) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        dados = (str(nome), contato_dono, idade, str(porte), str(sexo), str(castrado), str(raca))
        cursor.execute(comando_SQL, dados)
        banco.commit()

        QMessageBox.about(novo_cliente, 'Ação Realizada', 'Pet cadastrado com sucesso.')

    except:
        #se o campo obrigató contato for vazio imprimir essa mensagem
        if contato_dono == '' or nome == '':
            QMessageBox.about(novo_cliente, 'Erro', 'Campos obrigatórios não foram preenchidos.')

        if contato_dono != '' and (type(contato_dono) == int()):
            cursor1 = banco.cursor()
            verifica_chave = (f'SELECT * FROM TB_PET WHERE FK_CONTATO_DONO = {contato_dono};')
            cursor1.execute(verifica_chave)
            dados_lidos = cursor1.fetchall()
            valor_lido = dados_lidos
            if len(dados_lidos) > 0:
                QMessageBox.about(novo_cliente, 'Erro', 'Já existe regisro para esse contato')

        if (contato_dono != '') and (type(contato_dono) != int()):
            QMessageBox.about(novo_cliente, 'Erro', 'Contato_cliente deve ter somente números')

    #Após passar pelo except ele vai executar esse bloco
    else:
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
            QMessageBox.about(novo_cliente, 'Erro', 'Cdigo de barras deve ter somente números')

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

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_CLIENTE WHERE STATUS = 'A'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_clientes.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_clientes.tableWidget.setColumnCount(12)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 11):
            listar_dados_clientes.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    status_cliente = 'A'

def listar_clientes_inativos():
    global status_cliente
    listar_dados_clientes.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_CLIENTE WHERE STATUS = 'I'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_clientes.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_clientes.tableWidget.setColumnCount(12)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 11):
            listar_dados_clientes.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    status_cliente = 'I'

def listar_pets():
    global status_pet
    listar_dados_pets.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_PET WHERE STATUS = 'A'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_pets.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_pets.tableWidget.setColumnCount(9)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 8):
            listar_dados_pets.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    status_pet = 'A'

def listar_pets_inativos():
    global status_pet
    listar_dados_pets.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM TB_PET WHERE STATUS = 'I'"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    listar_dados_pets.tableWidget.setRowCount(len(dados_lidos))
    listar_dados_pets.tableWidget.setColumnCount(9)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 8):
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

def editar_dados_produtos():
    global codigo_barras_valor, status_produto
    linha = listar_dados_produtos.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute(f"SELECT CODIGO_BARRAS FROM TB_PRODUTO WHERE STATUS = '{status_produto}'")
    codigo_barras_lido = cursor.fetchall()
    codigo_barras_valor = codigo_barras_lido[linha][0]
    cursor.execute("SELECT * FROM TB_PRODUTO WHERE CODIGO_BARRAS ="+str(codigo_barras_valor))
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
    cursor.execute("SELECT * FROM TB_SERVICO WHERE ID ="+str(id_valor))
    servico = cursor.fetchall()
    editar_servico.show()

    valor_id_servico = id_valor

    editar_servico.lineEdit_3.setText(str(servico[0][0]))
    editar_servico.lineEdit_4.setText(str(servico[0][1]))
    editar_servico.lineEdit_5.setText(str(servico[0][2]))
    editar_servico.lineEdit_6.setText(str(servico[0][3]))

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
    cursor.execute(f"UPDATE TB_PRODUTO SET STATUS = '{status}', DESCRICAO='{descricao}', CODIGO_BARRAS='{codigo_barras}', PRECO='{preco}', FORNECEDOR='{fornecedor}', MARCA='{marca}' WHERE CODIGO_BARRAS={codigo_barras_valor}")
    #fechar e atualizar dados
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
    #fechar e atualizar dados
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
    contato_cliente_lido = clientes_lidos[linha][2]
    cursor.execute("SELECT * FROM TB_CLIENTE WHERE CONTATO =" + str(contato_cliente_lido))
    cliente = cursor.fetchall()

    status_lido = cliente[0][0]

    if status_lido == 'A':
        cursor.execute("UPDATE TB_CLIENTE SET STATUS = 'I' WHERE CONTATO ="+str(contato_cliente_lido))
        banco.commit()

    elif status_lido == 'I':
        cursor.execute("UPDATE TB_CLIENTE SET STATUS = 'A' WHERE CONTATO ="+str(contato_cliente_lido))
        banco.commit()

def desativar_ativar_dados_pet():
    global status_pet
    linha = listar_dados_pets.tableWidget.currentRow()
    listar_dados_pets.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM TB_PET WHERE STATUS = '{status_pet}'")
    pets_lidos = cursor.fetchall()
    contato_dono_lido = pets_lidos[linha][2]
    nome_pet_lido = pets_lidos[linha][1]
    cursor.execute(f"SELECT * FROM TB_PET WHERE FK_CONTATO_DONO = {str(contato_dono_lido)} AND NOME = '{nome_pet_lido}'")
    pet = cursor.fetchall()

    status_lido = pet[0][0]

    if status_lido == 'A':
        cursor.execute(f"UPDATE TB_PET SET STATUS = 'I' WHERE FK_CONTATO_DONO = {str(contato_dono_lido)} AND NOME = '{nome_pet_lido}'")
        banco.commit()

    elif status_lido == 'I':
        cursor.execute(f"UPDATE TB_PET SET STATUS = 'A' WHERE FK_CONTATO_DONO = {str(contato_dono_lido)} AND NOME = '{nome_pet_lido}'")
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
        cursor.execute("UPDATE TB_PRODUTO SET STATUS = 'I' WHERE CODIGO_BARRAS ="+str(codigo_barras_lido))
        banco.commit()

    elif status_lido == 'I':
        cursor.execute("UPDATE TB_PRODUTO SET STATUS = 'A' WHERE CODIGO_BARRAS ="+str(codigo_barras_lido))
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
        cursor.execute("UPDATE TB_SERVICO SET STATUS = 'I' WHERE ID ="+str(id_valor))
        banco.commit()

    elif status_lido == 'I':
        cursor.execute("UPDATE TB_SERVICO SET STATUS = 'A' WHERE ID ="+str(id_valor))
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
    print("PDF FOI GERADO COM SUCESSO!")

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

plano_serviço = uic.loadUi('Contratar Plano Serviço.ui')

listar_dados_clientes = uic.loadUi('Listar Dados Clientes.ui')

listar_dados_pets = uic.loadUi('Listar Dados Pets.ui')

listar_dados_produtos = uic.loadUi('Listar Dados Produtos.ui')

listar_dados_servicos = uic.loadUi('Listar Dados Servicos.ui')

editar_produto = uic.loadUi('Editar Produto.ui')

editar_servico = uic.loadUi('Editar Servico.ui')
app.exec()

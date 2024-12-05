import tkinter as tk
from tkinter import messagebox
import oracledb

# Função para realizar a conexão com o banco de dados
def conectar_oracle():
    username = ""
    password = ""
    dsn = ""

    try:
        # Conexão no modo Thin Client
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        connection.autocommit = False
        return connection
    except oracledb.Error as e:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao Oracle Database: {e}")
        return None



# Função para criar a tela de inserção com base na tabela selecionada
def criar_formulario_insercao():
    tabela = combo_tabela.get()

    # Limpar tela
    limpar_tela()

    if tabela == "Médico":
        criar_formulario_medico()
    elif tabela == "Treinador":
        criar_formulario_treinador()
    elif tabela == "Esporte":
        criar_formulario_esporte()
    elif tabela == "Time":
        criar_formulario_time()
    elif tabela == "Atleta":
        criar_formulario_atleta()
    elif tabela == "Partida":
        criar_formulario_partida()
    elif tabela == "Estatística de Partida":
        criar_formulario_est_partida()
    elif tabela == "Disputa":
        criar_formulario_disputa()
    elif tabela == "Estatística de Atleta na Partida":
        criar_formulario_est_atleta_partida()
    elif tabela == "Video":
        criar_formulario_video()
    elif tabela == "Exame":
        criar_formulario_exame()
    elif tabela== "Exame Ortopédico":
        criar_formulario_ortopedico()
    elif tabela == "Exame Cardiológico":
        criar_formulario_cardiologico()
    elif tabela == "Mapeamento Genético":
        criar_formulario_mapeamento()
    elif tabela == "Imagem Óssea":
        criar_formulario_Ossea()
    elif tabela == "Genoma":
        criar_formulario_Genoma()
    elif tabela == "Exame Neurológico":
        criar_formulario_Genoma()


def criar_formulario_Neurologico():
    limpar_tela()

    # Campos para armazenar os valores
    entry_protocolo = tk.Entry(root)
    entry_ressonancia = tk.Entry(root)

    # Layout do formulário
    # Coluna 1
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    # Coluna 2
    label_ressonancia = tk.Label(root, text="Link para os dados da Ressonância")
    label_ressonancia.grid(row=0, column=1, padx=20, pady=5)
    entry_ressonancia.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'neurologico',
            'protocolo': entry_protocolo.get().strip().upper(),
            'resssonancia': entry_ressonancia.get().strip()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=2, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=3, column=0, columnspan=2, pady=10)

def criar_formulario_Genoma():
    limpar_tela()

    # Campos para armazenar os valores
    entry_atleta = tk.Entry(root)
    entry_genoma = tk.Entry(root)
    entry_mapeamento = tk.Entry(root)
    # Layout do formulário
    # Coluna 1
    label_mapeamento = tk.Label(root, text="Protocolo do Mapeamento Genético (Formato: XXXXXXXXX-YYY):")
    label_mapeamento.grid(row=0, column=0, padx=20, pady=5)
    entry_mapeamento.grid(row=1, column=0, padx=20, pady=5)

    label_atleta = tk.Label(root, text="CPF do Atleta:")
    label_atleta.grid(row=2, column=0, padx=20, pady=5)
    entry_atleta.grid(row=3, column=0, padx=20, pady=5)

    # Coluna 2
    label_genoma  = tk.Label(root, text="Link para os dados do Genoma")
    label_genoma.grid(row=0, column=1, padx=20, pady=5)
    entry_genoma.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'genoma',
            'protocolo': entry_mapeamento.get().strip().upper(),
            'atleta': entry_atleta.get().strip().strip().upper(),
            'genoma': entry_genoma.get().strip()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)


def criar_formulario_Ossea():
    limpar_tela()

    # Campos para armazenar os valores
    entry_protocolo = tk.Entry(root)
    entry_imagem = tk.Entry(root)
    entry_link = tk.Entry(root)
    # Layout do formulário
    # Coluna 1
    label_protocolo = tk.Label(root, text="Protocolo do Exame Ortopédico (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    label_link = tk.Label(root, text="Protocolo do Exame Ortopédico (Formato: XXXXXXXXX-YYY):")
    label_link.grid(row=2, column=0, padx=20, pady=5)
    entry_link.grid(row=3, column=0, padx=20, pady=5)

    # Coluna 2
    label_imagem  = tk.Label(root, text="Número da Imagem")
    label_imagem.grid(row=0, column=1, padx=20, pady=5)
    entry_imagem.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'imagens',
            'protocolo': entry_protocolo.get().strip().upper(),
            'imagem': entry_imagem.get().strip().upper(),
            'link': entry_link.get().strip()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)

def criar_formulario_mapeamento():
    limpar_tela()

    # Campos para armazenar os valores
    entry_protocolo = tk.Entry(root)
    entry_amostra = tk.Entry(root)

    # Layout do formulário
    # Coluna 1
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    # Coluna 2
    label_amostra = tk.Label(root, text="Link da Amostra Biológica")
    label_amostra.grid(row=0, column=1, padx=20, pady=5)
    entry_amostra.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'mapeamemnto',
            'protocolo': entry_protocolo.get().strip().upper(),
            'amostra': entry_amostra.get().strip()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=2, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=3, column=0, columnspan=2, pady=10)

def criar_formulario_cardiologico():
    limpar_tela()

    # Campos para armazenar os valores
    entry_protocolo = tk.Entry(root)
    entry_ultrassom = tk.Entry(root)

    # Layout do formulário
    # Coluna 1
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    # Coluna 2
    label_ultrassom = tk.Label(root, text="Link do Ultrassom")
    label_ultrassom.grid(row=0, column=1, padx=20, pady=5)
    entry_ultrassom.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'cardiologico',
            'protocolo': entry_protocolo.get().strip().upper(),
            'ultrassom': entry_ultrassom.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=2, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=3, column=0, columnspan=2, pady=10)


def criar_formulario_ortopedico():
    limpar_tela()

    # Campos para armazenar os valores
    entry_protocolo = tk.Entry(root)


    # Layout do formulário
    # Coluna 1
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'ortopedico',
            'protocolo': entry_protocolo.get().strip().upper(),
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=2, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=3, column=0, columnspan=2, pady=10)

def criar_formulario_exame():
    limpar_tela()

    # Campos para armazenar os valores
    entry_protocolo = tk.Entry(root)
    entry_data = tk.Entry(root)
    entry_medico = tk.Entry(root)
    entry_atleta = tk.Entry(root)
    entry_tipo = tk.Entry(root)
    entry_nivelO = tk.Entry(root)
    entry_pressao = tk.Entry(root)
    entry_temp = tk.Entry(root)


    # Layout do formulário
    # Coluna 1
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    label_atleta = tk.Label(root, text="CPF do Atleta:")
    label_atleta.grid(row=2, column=0, padx=20, pady=5)
    entry_atleta.grid(row=3, column=0, padx=20, pady=5)

    label_medico = tk.Label(root, text="Medico:")
    label_medico.grid(row=4, column=0, padx=20, pady=5)
    entry_medico.grid(row=5, column=0, padx=20, pady=5)

    label_data = tk.Label(root, text="Data e Hora:")
    label_data.grid(row=6, column=0, padx=20, pady=5)
    entry_data.grid(row=7, column=0, padx=20, pady=5)

    # Coluna 2 (Campos de endereço)
    label_tipo = tk.Label(root, text="Tipo do Exame:")
    label_tipo.grid(row=0, column=1, padx=20, pady=5)
    entry_tipo.grid(row=1, column=1, padx=20, pady=5)

    label_nivelO = tk.Label(root, text="Nível de Oxigênio do Atleta:")
    label_nivelO.grid(row=2, column=1, padx=20, pady=5)
    entry_nivelO.grid(row=3, column=1, padx=20, pady=5)

    label_pressao = tk.Label(root, text="Pressão Arterial do Atleta:")
    label_pressao.grid(row=4, column=1, padx=20, pady=5)
    entry_pressao.grid(row=5, column=1, padx=20, pady=5)

    label_temp = tk.Label(root, text="Temperatura do Atleta:")
    label_temp.grid(row=6, column=1, padx=20, pady=5)
    entry_temp.grid(row=7, column=1, padx=20, pady=5)


    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'exame',
            'protocolo': entry_protocolo.get().strip().upper(),
            'atleta': entry_atleta.get().strip().upper(),
            'medico': entry_medico.get().strip().upper(),
            'data': entry_data.get().strip().upper(),
            'pressao': entry_pressao.get().strip().upper(),
            'temp': entry_temp.get().strip().upper(),
            'nivelO': entry_nivelO.get().strip().upper(),
            'tipo': entry_tipo.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=8, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=9, column=0, columnspan=2, pady=10)


def criar_formulario_video():
    limpar_tela()

    # Campos para armazenar os valores
    entry_mac = tk.Entry(root)
    entry_data = tk.Entry(root)
    entry_duracao = tk.Entry(root)
    entry_atleta = tk.Entry(root)
    entry_pdata = tk.Entry(root)
    entry_plocal = tk.Entry(root)
    entry_dado = tk.Entry(root)


    # Layout do formulário
    # Coluna 1
    label_mac = tk.Label(root, text=" MAC address (Formato: XX-XX-XX-XX-XX-XX):")
    label_mac.grid(row=0, column=0, padx=20, pady=5)
    entry_mac.grid(row=1, column=0, padx=20, pady=5)

    label_atleta = tk.Label(root, text="CPF do Atleta:")
    label_atleta.grid(row=2, column=0, padx=20, pady=5)
    entry_atleta.grid(row=3, column=0, padx=20, pady=5)

    label_duracao = tk.Label(root, text="Duracao:")
    label_duracao.grid(row=4, column=0, padx=20, pady=5)
    entry_duracao.grid(row=5, column=0, padx=20, pady=5)

    label_data = tk.Label(root, text="Data e Hora:")
    label_data.grid(row=6, column=0, padx=20, pady=5)
    entry_data.grid(row=7, column=0, padx=20, pady=5)

    # Coluna 2 (Campos de endereço)
    label_dado = tk.Label(root, text="Link do video:")
    label_dado.grid(row=0, column=1, padx=20, pady=5)
    entry_dado.grid(row=1, column=1, padx=20, pady=5)

    label_pdata = tk.Label(root, text="Data da Partida:")
    label_pdata.grid(row=2, column=1, padx=20, pady=5)
    entry_pdata.grid(row=3, column=1, padx=20, pady=5)

    label_plocal = tk.Label(root, text="Local da Partida:")
    label_plocal.grid(row=4, column=1, padx=20, pady=5)
    entry_plocal.grid(row=5, column=1, padx=20, pady=5)


    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'video',
            'mac': entry_mac.get().strip().upper(),
            'atleta': entry_atleta.get().strip().upper(),
            'duracao': entry_duracao.get().strip().upper(),
            'data': entry_data.get().strip().upper(),
            'plocal': entry_plocal.get().strip().upper(),
            'pdata': entry_pdata.get().strip().upper(),
            'dado': entry_dado.get().strip()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=6, column=1, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=7, column=1, columnspan=2, pady=10)


def criar_formulario_disputa():
    #Campos para armazenar os valores
    entry_data = tk.Entry(root)
    entry_local = tk.Entry(root)
    entry_time = tk.Entry(root)
    entry_esporte = tk.Entry(root)

    label_data = tk.Label(root, text="Data da Partida")
    label_data.grid(row=0, column=0, padx=20, pady=5)
    entry_data.grid(row=1, column=0, padx=20, pady=5)

    label_time = tk.Label(root, text="Sigla do Time")
    label_time.grid(row=0, column=1, padx=20, pady=5)
    entry_time.grid(row=1, column=1, padx=20, pady=5)

    label_esporte = tk.Label(root, text="Sigla do Esporte (Formato: ABC)")
    label_esporte.grid(row=2, column=0, padx=20, pady=5)
    entry_esporte.grid(row=3, column=0, padx=20, pady=5)

    label_local = tk.Label(root, text="Local da Partida")
    label_local.grid(row=2, column=1, padx=20, pady=5)
    entry_local.grid(row=3, column=1, padx=20, pady=5)


    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'disputa',
            'data': entry_data.get().strip().upper(),
            'time': entry_time.get().strip().upper(),
            'esporte': entry_esporte.get().strip().upper(),
            'local': entry_local.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)

def criar_formulario_est_atleta_partida():
    #Campos para armazenar os valores
    entry_data = tk.Entry(root)
    entry_local = tk.Entry(root)
    entry_criterio = tk.Entry(root)
    entry_valor = tk.Entry(root)
    entry_atleta = tk.Entry(root)

    label_data = tk.Label(root, text="Data da Partida")
    label_data.grid(row=0, column=0, padx=20, pady=5)
    entry_data.grid(row=1, column=0, padx=20, pady=5)

    label_criterio = tk.Label(root, text="Nome da estatística avaliada àquela partida")
    label_criterio.grid(row=0, column=1, padx=20, pady=5)
    entry_criterio.grid(row=1, column=1, padx=20, pady=5)

    label_valor = tk.Label(root, text="Valor")
    label_valor.grid(row=2, column=0, padx=20, pady=5)
    entry_valor.grid(row=3, column=0, padx=20, pady=5)

    label_local = tk.Label(root, text="Local da Partida")
    label_local.grid(row=2, column=1, padx=20, pady=5)
    entry_local.grid(row=3, column=1, padx=20, pady=5)

    label_atleta = tk.Label(root, text="CPF do Atleta")
    label_atleta.grid(row=4, column=0, padx=20, pady=5)
    entry_atleta.grid(row=5, column=0, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'estat_atleta_partida',
            'data': entry_data.get().strip().upper(),
            'criterio': entry_criterio.get().strip().upper(),
            'valor': entry_valor.get().strip().upper(),
            'local': entry_local.get().strip().upper(),
            'atleta': entry_atleta.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=1, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=1, columnspan=2, pady=10)


def criar_formulario_est_partida():
    #Campos para armazenar os valores
    entry_data = tk.Entry(root)
    entry_local = tk.Entry(root)
    entry_criterio = tk.Entry(root)
    entry_valor = tk.Entry(root)

    label_data = tk.Label(root, text="Data da Partida")
    label_data.grid(row=0, column=0, padx=20, pady=5)
    entry_data.grid(row=1, column=0, padx=20, pady=5)

    label_criterio = tk.Label(root, text="Nome da estatística avaliada àquela partida")
    label_criterio.grid(row=0, column=1, padx=20, pady=5)
    entry_criterio.grid(row=1, column=1, padx=20, pady=5)

    label_valor = tk.Label(root, text="Valor")
    label_valor.grid(row=2, column=0, padx=20, pady=5)
    entry_valor.grid(row=3, column=0, padx=20, pady=5)

    label_local = tk.Label(root, text="Local da Partida")
    label_local.grid(row=2, column=1, padx=20, pady=5)
    entry_local.grid(row=3, column=1, padx=20, pady=5)


    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'estat_partida',
            'data': entry_data.get().strip().upper(),
            'criterio': entry_criterio.get().strip().upper(),
            'valor': entry_valor.get().strip().upper(),
            'local': entry_local.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)


def criar_formulario_partida():
    #Campos para armazenar os valores
    entry_data = tk.Entry(root)
    entry_local = tk.Entry(root)
    entry_nome = tk.Entry(root)
    entry_esporte = tk.Entry(root)

    label_data = tk.Label(root, text="Data da Partida")
    label_data.grid(row=0, column=0, padx=20, pady=5)
    entry_data.grid(row=1, column=0, padx=20, pady=5)

    label_nome = tk.Label(root, text="Nome descritivo da Partida")
    label_nome.grid(row=0, column=1, padx=20, pady=5)
    entry_nome.grid(row=1, column=1, padx=20, pady=5)

    label_esporte = tk.Label(root, text="Sigla do Esporte (Formato: ABC)")
    label_esporte.grid(row=2, column=0, padx=20, pady=5)
    entry_esporte.grid(row=3, column=0, padx=20, pady=5)

    label_local = tk.Label(root, text="Local da Partida")
    label_local.grid(row=2, column=1, padx=20, pady=5)
    entry_local.grid(row=3, column=1, padx=20, pady=5)


    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'partida',
            'data': entry_data.get().strip().upper(),
            'nome': entry_nome.get().strip().upper(),
            'esporte': entry_esporte.get().strip().upper(),
            'local': entry_local.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)

def criar_formulario_time():
    #Campos para armazenar os valores
    entry_sigla = tk.Entry(root)
    entry_esporte = tk.Entry(root)
    entry_nome = tk.Entry(root)
    entry_treinador = tk.Entry(root)

    label_sigla = tk.Label(root, text="Sigla do Time (Formato: ABCDE)")
    label_sigla.grid(row=0, column=0, padx=20, pady=5)
    entry_sigla.grid(row=1, column=0, padx=20, pady=5)

    label_nome = tk.Label(root, text="Nome do Time")
    label_nome.grid(row=0, column=1, padx=20, pady=5)
    entry_nome.grid(row=1, column=1, padx=20, pady=5)

    label_esporte = tk.Label(root, text="Sigla do Esporte do Time (Formato: ABC)")
    label_esporte.grid(row=2, column=0, padx=20, pady=5)
    entry_esporte.grid(row=3, column=0, padx=20, pady=5)

    label_treinador = tk.Label(root, text="CPF do treinador")
    label_treinador.grid(row=2, column=1, padx=20, pady=5)
    entry_treinador.grid(row=3, column=1, padx=20, pady=5)


    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'time',
            'sigla': entry_sigla.get().strip().upper(),
            'nome': entry_nome.get().strip().upper(),
            'esporte': entry_esporte.get().strip().upper(),
            'treinador': entry_treinador.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)


def criar_formulario_esporte():

    #Campos para armazenar os valores
    entry_sigla = tk.Entry(root)
    entry_nome = tk.Entry(root)
    entry_qnt = tk.Entry(root)

    label_sigla = tk.Label(root, text="Sigla do Esporte (Formato: ABC)")
    label_sigla.grid(row=0, column=0, padx=20, pady=5)
    entry_sigla.grid(row=1, column=0, padx=20, pady=5)

    label_nome = tk.Label(root, text="Nome do Esporte")
    label_nome.grid(row=0, column=1, padx=20, pady=5)
    entry_nome.grid(row=1, column=1, padx=20, pady=5)

    label_qnt = tk.Label(root, text="Quantidade de times por jogo")
    label_qnt.grid(row=2, column=0, padx=20, pady=5)
    entry_qnt.grid(row=3, column=0, padx=20, pady=5)


    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'esporte',
            'sigla': entry_sigla.get().strip().upper(),
            'nome': entry_nome.get().strip().upper(),
            'qnt': entry_qnt.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)


def criar_formulario_treinador():
    limpar_tela()

    # Campos para armazenar os valores
    entry_cpf = tk.Entry(root)
    entry_cref = tk.Entry(root)
    entry_nome = tk.Entry(root)
    entry_data = tk.Entry(root)
    entry_rua = tk.Entry(root)
    entry_numero = tk.Entry(root)
    entry_bairro = tk.Entry(root)
    entry_cep = tk.Entry(root)
    entry_uf = tk.StringVar()
    entry_uf.set('')  # Valor padrão vazio para o dropdown

    # Layout do formulário
    # Coluna 1
    label_cpf = tk.Label(root, text="CPF (Formato: XXX.XXX.XXX-XX):")
    label_cpf.grid(row=0, column=0, padx=20, pady=5)
    entry_cpf.grid(row=1, column=0, padx=20, pady=5)

    label_cref = tk.Label(root, text="CREF (6 dígitos):")
    label_cref.grid(row=2, column=0, padx=20, pady=5)
    entry_cref.grid(row=3, column=0, padx=20, pady=5)

    label_nome = tk.Label(root, text="Nome:")
    label_nome.grid(row=4, column=0, padx=20, pady=5)
    entry_nome.grid(row=5, column=0, padx=20, pady=5)

    label_data = tk.Label(root, text="Data de Nascimento:")
    label_data.grid(row=6, column=0, padx=20, pady=5)
    entry_data.grid(row=7, column=0, padx=20, pady=5)

    # Coluna 2 (Campos de endereço)
    label_rua = tk.Label(root, text="Rua:")
    label_rua.grid(row=0, column=1, padx=20, pady=5)
    entry_rua.grid(row=1, column=1, padx=20, pady=5)

    label_numero = tk.Label(root, text="Número:")
    label_numero.grid(row=2, column=1, padx=20, pady=5)
    entry_numero.grid(row=3, column=1, padx=20, pady=5)

    label_bairro = tk.Label(root, text="Bairro:")
    label_bairro.grid(row=4, column=1, padx=20, pady=5)
    entry_bairro.grid(row=5, column=1, padx=20, pady=5)

    label_cep = tk.Label(root, text="CEP (Formato: XXXXX-XXX):")
    label_cep.grid(row=6, column=1, padx=20, pady=5)
    entry_cep.grid(row=7, column=1, padx=20, pady=5)

    label_uf = tk.Label(root, text="UF (Estado):")
    label_uf.grid(row=8, column=1, padx=20, pady=5)
    estados = ['', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    menu_uf = tk.OptionMenu(root, entry_uf, *estados)
    menu_uf.grid(row=9, column=1, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'treinador',
            'cpf': entry_cpf.get().strip().upper(),
            'cref': entry_cref.get().strip().upper(),
            'nome': entry_nome.get().strip().upper(),
            'data': entry_data.get().strip().upper(),
            'rua': entry_rua.get().strip().upper(),
            'numero': entry_numero.get().strip().upper(),
            'bairro': entry_bairro.get().strip().upper(),
            'cep': entry_cep.get().strip().upper(),
            'uf': entry_uf.get().strip().upper(),
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=10, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=11, column=0, columnspan=2, pady=10)



def criar_formulario_atleta():
    limpar_tela()

    # Campos para armazenar os valores
    entry_cpf = tk.Entry(root)
    entry_id = tk.Entry(root)
    entry_nome = tk.Entry(root)
    entry_esporte = tk.Entry(root)
    entry_time = tk.Entry(root)
    entry_data = tk.Entry(root)
    entry_rua = tk.Entry(root)
    entry_numero = tk.Entry(root)
    entry_bairro = tk.Entry(root)
    entry_cep = tk.Entry(root)
    entry_uf = tk.StringVar()
    entry_uf.set('')  # Valor padrão vazio para o dropdown

    # Layout do formulário
    # Coluna 1
    label_cpf = tk.Label(root, text="CPF (Formato: XXX.XXX.XXX-XX):")
    label_cpf.grid(row=0, column=0, padx=20, pady=5)
    entry_cpf.grid(row=1, column=0, padx=20, pady=5)

    label_id = tk.Label(root, text="ID (5 dígitos):")
    label_id.grid(row=2, column=0, padx=20, pady=5)
    entry_id.grid(row=3, column=0, padx=20, pady=5)

    label_nome = tk.Label(root, text="Nome:")
    label_nome.grid(row=4, column=0, padx=20, pady=5)
    entry_nome.grid(row=5, column=0, padx=20, pady=5)

    label_esporte = tk.Label(root, text="Sigla do Esporte:")
    label_esporte.grid(row=6, column=0, padx=20, pady=5)
    entry_esporte.grid(row=7, column=0, padx=20, pady=5)

    label_time = tk.Label(root, text="Sigla do time")
    label_time.grid(row=8, column=0, padx=20, pady=5)
    entry_time.grid(row=9, column=0, padx=20, pady=5)


    label_data = tk.Label(root, text="Data de Nascimento:")
    label_data.grid(row=10, column=0, padx=20, pady=5)
    entry_data.grid(row=11, column=0, padx=20, pady=5)

    # Coluna 2 (Campos de endereço)
    label_rua = tk.Label(root, text="Rua:")
    label_rua.grid(row=0, column=1, padx=20, pady=5)
    entry_rua.grid(row=1, column=1, padx=20, pady=5)

    label_numero = tk.Label(root, text="Número:")
    label_numero.grid(row=2, column=1, padx=20, pady=5)
    entry_numero.grid(row=3, column=1, padx=20, pady=5)

    label_bairro = tk.Label(root, text="Bairro:")
    label_bairro.grid(row=4, column=1, padx=20, pady=5)
    entry_bairro.grid(row=5, column=1, padx=20, pady=5)

    label_cep = tk.Label(root, text="CEP (Formato: XXXXX-XXX):")
    label_cep.grid(row=6, column=1, padx=20, pady=5)
    entry_cep.grid(row=7, column=1, padx=20, pady=5)

    label_uf = tk.Label(root, text="UF (Estado):")
    label_uf.grid(row=8, column=1, padx=20, pady=5)
    estados = ['', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    menu_uf = tk.OptionMenu(root, entry_uf, *estados)
    menu_uf.grid(row=9, column=1, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'atleta',
            'cpf': entry_cpf.get().strip().upper(),
            'cref': entry_id.get().strip().upper(),
            'esporte': entry_esporte.get().strip().upper(),
            'time': entry_time.get().strip().upper(),
            'nome': entry_nome.get().strip().upper(),
            'data': entry_data.get().strip().upper(),
            'rua': entry_rua.get().strip().upper(),
            'numero': entry_numero.get().strip().upper(),
            'bairro': entry_bairro.get().strip().upper(),
            'cep': entry_cep.get().strip().upper(),
            'uf': entry_uf.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=10, column=1, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=11, column=1, columnspan=2, pady=10)


# Função para criar o formulário de inserção para MÉDICO
def criar_formulario_medico():
    limpar_tela()

    # Campos para armazenar os valores
    entry_cpf = tk.Entry(root)
    entry_crm = tk.Entry(root)
    entry_nome = tk.Entry(root)
    entry_data = tk.Entry(root)
    entry_rua = tk.Entry(root)
    entry_numero = tk.Entry(root)
    entry_bairro = tk.Entry(root)
    entry_cep = tk.Entry(root)
    entry_uf = tk.StringVar()
    entry_uf.set('')  # Valor padrão vazio para o dropdown

    # Layout do formulário
    # Coluna 1
    label_cpf = tk.Label(root, text="CPF (Formato: XXX.XXX.XXX-XX):")
    label_cpf.grid(row=0, column=0, padx=20, pady=5)
    entry_cpf.grid(row=1, column=0, padx=20, pady=5)

    label_crm = tk.Label(root, text="CRM (6 dígitos):")
    label_crm.grid(row=2, column=0, padx=20, pady=5)
    entry_crm.grid(row=3, column=0, padx=20, pady=5)

    label_nome = tk.Label(root, text="Nome:")
    label_nome.grid(row=4, column=0, padx=20, pady=5)
    entry_nome.grid(row=5, column=0, padx=20, pady=5)

    label_data = tk.Label(root, text="Data de Nascimento:")
    label_data.grid(row=6, column=0, padx=20, pady=5)
    entry_data.grid(row=7, column=0, padx=20, pady=5)

    # Coluna 2 (Campos de endereço)
    label_rua = tk.Label(root, text="Rua:")
    label_rua.grid(row=0, column=1, padx=20, pady=5)
    entry_rua.grid(row=1, column=1, padx=20, pady=5)

    label_numero = tk.Label(root, text="Número:")
    label_numero.grid(row=2, column=1, padx=20, pady=5)
    entry_numero.grid(row=3, column=1, padx=20, pady=5)

    label_bairro = tk.Label(root, text="Bairro:")
    label_bairro.grid(row=4, column=1, padx=20, pady=5)
    entry_bairro.grid(row=5, column=1, padx=20, pady=5)

    label_cep = tk.Label(root, text="CEP (Formato: XXXXX-XXX):")
    label_cep.grid(row=6, column=1, padx=20, pady=5)
    entry_cep.grid(row=7, column=1, padx=20, pady=5)

    label_uf = tk.Label(root, text="UF (Estado):")
    label_uf.grid(row=8, column=1, padx=20, pady=5)
    estados = ['', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    menu_uf = tk.OptionMenu(root, entry_uf, *estados)
    menu_uf.grid(row=9, column=1, padx=20, pady=5)

    # Função para salvar os dados no JSON
    def salvar_dados():
        # Coletar os valores dos campos
        dados = {
            'tabela': 'medico',
            'cpf': entry_cpf.get().strip().upper(),
            'crm': entry_crm.get().strip().upper(),
            'nome': entry_nome.get().strip().upper(),
            'data': entry_data.get().strip().upper(),
            'rua': entry_rua.get().strip().upper(),
            'numero': entry_numero.get().strip().upper(),
            'bairro': entry_bairro.get().strip().upper(),
            'cep': entry_cep.get().strip().upper(),
            'uf': entry_uf.get().strip().upper()
        }
        # Salvar no JSON
        inserir_dados_no_banco(dados)

    # Botão para inserir dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=10, column=0, columnspan=2, pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=11, column=0, columnspan=2, pady=10)

# Função para consultar jogadores por esporte e exibir genoma




# Função para exibir a tela de seleção do esporte
def exibir_selecao():
    limpar_tela()

    # Campos de entrada para o nome do esporte
    entry_esporte = tk.Entry(root)

    def consultar_jogadores_por_esporte():
        try:
            # Obter o nome do esporte
            esporte_nome = entry_esporte.get()

            # Validar se o nome do esporte foi preenchido
            if not esporte_nome:
                messagebox.showerror("Erro", "Por favor, insira o nome do esporte.")
                return

            # Conectar ao banco de dados
            connection = conectar_oracle()
            if connection:
                cursor = connection.cursor()

                # Consulta SQL para buscar jogadores e seus genomas
                query = """
                    SELECT A.CPF, G.GENOMA
                    FROM ATLETA A
                    LEFT JOIN GENOMA G ON A.CPF = G.ATLETA
                    JOIN ESPORTE E ON A.ATL_SIGLA_ESPORTE = E.SIGLA_ESPORTE
                    WHERE E.NOME = :esporte_nome
                """

                cursor.execute(query, {'esporte_nome': esporte_nome})
                results = cursor.fetchall()

                # Exibir os resultados na Listbox
                for row in results:
                    jogador = row[0]
                    genoma = row[1] if row[1] else "Genoma não cadastrado"
                    print(tk.END, f"{jogador} | {genoma}")
                

                if not results:
                    messagebox.showinfo("Resultado", "Nenhum jogador encontrado para esse esporte.")

                cursor.close()
                connection.close()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar dados: {e}")

    # Label e campos para seleção do esporte
    label_esporte = tk.Label(root, text="Selecione o Esporte:")
    label_esporte.grid(row=0, column=0, padx=10, pady=5)
    entry_esporte.grid(row=0, column=1, padx=10, pady=5)

    # Botões
    button_pesquisar = tk.Button(root, text="Pesquisar", command=consultar_jogadores_por_esporte)
    button_pesquisar.grid(row=1, column=0, columnspan=2, pady=10)

# Função para inserir os dados no banco de dados a partir do JSON
def inserir_dados_no_banco(dados):
    try:        
        # Conectar ao banco
        connection = conectar_oracle()
        if connection:
            cursor = connection.cursor()

            # A lógica para inserção no banco é adaptável conforme a tabela
            if dados['tabela'] == "medico":
                query = """INSERT INTO MEDICO (CPF, CRM, NOME, DATA, RUA, NUMERO, BAIRRO, CEP, UF)
                           VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8, :9)"""
                cursor.execute(query, (dados['cpf'], dados['crm'], dados['nome'], dados['data'], dados['rua'], dados['numero'], dados['bairro'], dados['cep'], dados['uf']))
            elif dados['tabela'] == "treinador":
                query = """INSERT INTO TREINADOR (CPF, CREF, NOME, DATA, RUA, NUMERO, BAIRRO, CEP, UF)
                           VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8, :9)"""
                cursor.execute(query, (dados['cpf'], dados['cref'], dados['nome'], dados['data'], dados['rua'], dados['numero'], dados['bairro'], dados['cep'], dados['uf']))
            elif dados['tabela'] == "esporte":
                query = """INSERT INTO ESPORTE (SIGLA_ESPORTE, NOME, QUANT_TIME_POR_JOGO)
                           VALUES (:1, :2, :3)"""
                cursor.execute(query, (dados['sigla'], dados['nome'], dados['qnt']))
            elif dados['tabela'] == "time":
                query = """INSERT INTO TIME (SIGLA_TIME, SIGLA_ESPORTE, NOME, CPF_TREINADOR)
                           VALUES (:1, :2, :3, :4)"""
                cursor.execute(query, (dados['sigla'], dados['esporte'], dados['nome'], dados['treinador']))
            elif dados['tabela'] == "atleta":
                query = """INSERT INTO ATLETA (CPF, ID_ATLETA, NOME, ATL_SIGLA_TIME, ATL_SIGLA_ESPORTE, DATA, RUA, NUMERO, BAIRRO, CEP, UF)
                           VALUES (:1, :2, :3, :4, :5, TO_DATE(:6, 'YYYY-MM-DD'), :7, :8, :9, :10, :11)"""
                cursor.execute(query, (dados['cpf'], dados['id'], dados['nome'], dados['time'], dados['esporte'], dados['data'], dados['rua'], dados['numero'], dados['bairro'], dados['cep'], dados['uf']))
            elif dados['tabela'] == "partida":
                query = """INSERT INTO PARTIDA (DATA, LOCAL, NOME, SIGLA_ESPORTE)
                           VALUES (TO_DATE(:1, 'YYYY-MM-DD'), :2, :3, :4)"""
                cursor.execute(query, (dados['data'], dados['local'], dados['nome'], dados['esporte']))
            elif dados['tabela'] == "estat_partida":
                query = """INSERT INTO ESTAT_PARTIDA (DATA, LOCAL, CRITERIO, VALOR)
                           VALUES (TO_DATE(:1, 'YYYY-MM-DD'), :2, :3, :4)"""
                cursor.execute(query, (dados['data'], dados['local'], dados['criterio'], dados['valor']))
            elif dados['tabela'] == "disputa":
                query = """INSERT INTO ESTAT_PARTIDA (SIGLA_TIME, SIGLA_ESPORTE, EST_DATA, EST_LOCAL)
                           VALUES (TO_DATE(:1, 'YYYY-MM-DD'), :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)"""
                cursor.execute(query, (dados['time'], dados['esporte'], dados['data'], dados['local']))
            elif dados['tabela'] == "estat_atleta_partida":
                query = """INSERT INTO ESTAT_ATLETA_PARTIDA (ATLETA, EST_DATA, EST_LOCAL, CRITERIO, VALOR)
                           VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5)"""
                cursor.execute(query, (dados['atleta'], dados['data'], dados['local'], dados['criterio'], dados['valor']))
            elif dados['tabela'] == "video":
                query = """INSERT INTO VIDEO (MAC_ADDRESS, DATA_HORA, DURACAO, DADO_VIDEO, ATLETA, PARTIDA_DATA, PARTIDA_LOCAL)
                           VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5, TO_DATA(:6, 'YYYY-MM-DD'), :7)"""
                cursor.execute(query, (dados['mac'], dados['data'], dados['duracao'], dados['dado'], dados['atleta']. dados['pdata'], dados['plocal']))
            elif dados['tabela'] == "exame":
                query = """INSERT INTO EXAME (PROTOCOLO, DATA_HORA, MEDICO, ATLETA, TIPO, NIVEL_OXIGENIO, PRESSAO_ATELTA, TEMPERATURA_ATLETA)
                           VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5, :6, :7, :8)"""
                cursor.execute(query, (dados['protocolo'], dados['data'], dados['medico'], dados['atleta'], dados['tipo']. dados['nivelO'], dados['pressao'], dados['temp']))
            elif dados['tabela'] == "ortopedico":
                query = """INSERT INTO ORTOPEDICO (EXAME)
                           VALUES (:1)"""
                cursor.execute(query, (dados['protocolo']))
            elif dados['tabela'] == "cardiologico":
                query = """INSERT INTO CARDIOLOGICO (EXAME, ULTRASSOM)
                           VALUES (:1, :2)"""
                cursor.execute(query, (dados['protocolo'], dados["ultrassom"]))
            elif dados['tabela'] == "neurologico":
                query = """INSERT INTO NEUROLOGICO (EXAME, RESSONANCIA_MAGNETICA)
                           VALUES (:1, :2)"""
                cursor.execute(query, (dados['protocolo'], dados["ressonancia"]))
            elif dados['tabela'] == "mapeamento":
                query = """INSERT INTO MAPEAMENTO_GENETICO (EXAME, AMOSTRA_BIOLOGICA)
                           VALUES (:1, :2)"""
                cursor.execute(query, (dados['protocolo'], dados["amostra"]))
            elif dados['tabela'] == "imagens":
                query = """INSERT INTO IMAGEM_OSSEA (EXAME_ORTOPEDICO, IMAGEM, LINK)
                           VALUES (:1, :2, :3)"""
                cursor.execute(query, (dados['protocolo'], dados["imagem"], dados["link"]))
            elif dados['tabela'] == "genoma":
                query = """INSERT INTO GENOMA (ATLETA, GENOMA, MAPEAMENTO)
                           VALUES (:1, :2, :3)"""
                cursor.execute(query, (dados['atleta'], dados["genoma"], dados["genoma"]))
            connection.commit()
            messagebox.showinfo("Sucesso", "Dados inseridos no banco de dados com sucesso!")
            cursor.close()
            connection.close()
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao inserir dados no banco: {e}")
        connection.rollback()

# Função para exibir o menu de seleção de tabela
def exibir_menu():
    limpar_tela()

    # Tela de Menu
    label_menu = tk.Label(root, text="Menu de Ações", font=("Helvetica", 16))
    label_menu.pack(pady=20)

    button_inserir = tk.Button(root, text="Inserir Dados", command=mostrar_submenu_insercao)
    button_inserir.pack(pady=10)

    button_selecionar = tk.Button(root, text="Selecionar Dados", command=exibir_selecao)
    button_selecionar.pack(pady=10)

    button_editar = tk.Button(root, text="Editar Dados", state=tk.DISABLED)
    button_editar.pack(pady=10)

# Função para exibir o submenu de inserção de dados
def mostrar_submenu_insercao():
    limpar_tela()

    # Combobox para selecionar a tabela onde o usuário deseja inserir dados
    label_selecao = tk.Label(root, text="Escolha a tabela para inserir dados:")
    label_selecao.pack(pady=10)

    global combo_tabela
    combo_tabela = tk.StringVar()
    tabelas = ["Médico", "Treinador", "Esporte", "Time", "Atleta", "Partida", "Estatística de Partida", "Disputa", "Estatística de Atleta na Partida", "Video", "Exame", "Exame Ortopédico", "Exame Cardiológico", "Exame Neurológico", "Mapeamento Genético", "Imagem Óssea", "Genoma"]
    combo_tabela.set(tabelas[0])  # Definindo valor padrão
    dropdown_tabela = tk.OptionMenu(root, combo_tabela, *tabelas)
    dropdown_tabela.pack(pady=10)

    # Botão para ir para o formulário de inserção
    button_confirmar = tk.Button(root, text="Confirmar", command=criar_formulario_insercao)
    button_confirmar.pack(pady=10)

    # Botão de voltar
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.pack(pady=5)

# Função para limpar a tela
def limpar_tela():
    for widget in root.winfo_children():
        widget.destroy()

# Criando a janela principal
root = tk.Tk()
root.title("Menu Principal")

root.geometry("500x700") 
# Exibindo o menu inicial
exibir_menu()

# Rodar a interface gráfica
root.mainloop()
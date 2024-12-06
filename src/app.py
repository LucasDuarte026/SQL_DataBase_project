# Importação das bibliotecas necessárias
import tkinter as tk               # Biblioteca para criar interfaces gráficas
from tkinter import messagebox     # Para exibir caixas de mensagem (ex.: erro ou informações ao usuário)
import oracledb                    # Biblioteca para interação com o Oracle Database
from datetime import datetime, timedelta
# ============================
# Funções Relacionadas à Interface Gráfica
# ============================
# As funções a seguir são responsáveis por criar e gerenciar a interface gráfica da aplicação,
# permitindo a interação do usuário com o sistema através da biblioteca Tkinter.
#
# Cada função é projetada para realizar uma tarefa específica na aplicação, como exibir menus, 
# formularios de inserção de dados, e realizar consultas no banco de dados. Abaixo, são descritas
# as principais funções que compõem a interface gráfica:
#
# 1. **exibir_menu()**:
#    - Exibe o menu principal da aplicação, oferecendo opções como inserir dados, selecionar dados
#      ou editar dados (opção atualmente desabilitada).
#    - Inclui três botões:
#      - "Inserir Dados" para abrir um submenu de inserção de dados.
#      - "Selecionar Dados" para exibir a tela de seleção de esportes e jogadores.
#      - "Editar Dados" (desabilitado no momento).
#
# 2. **mostrar_submenu_insercao()**:
#    - Exibe o submenu onde o usuário pode escolher em qual tabela deseja inserir dados.
#    - Oferece um campo de seleção (ComboBox) com uma lista de tabelas (como Médico, Treinador, Atleta, etc.).
#    - Após a seleção da tabela, um botão "Confirmar" redireciona o usuário para o formulário de inserção correspondente.
#
# 3. **exibir_selecao()**:
#    - Exibe a tela para seleção de esportes. O usuário insere o nome do esporte e clica em "Pesquisar" para buscar dados.
#    - Realiza uma consulta no banco de dados, buscando jogadores e seus genomas associados ao esporte escolhido.
#    - Mostra os resultados em um formato legível ou uma mensagem de erro caso não encontre resultados.
#
# 4. **Funções de Criar Formularios**:
#    - Cria um formulário para inserção de dados relacionados ao cadastro da devida tabela que o usuários escolher no banco de dados.
#    - O formulário coleta dados para a tabela em questão, as salva em um dicionário e quando o usuário clica em enviar, tenta inserir no banco de dados
#    - Possui um botão "Inserir" para salvar os dados no banco e um botão "Voltar ao Menu Principal" para retornar ao menu inicial.
#
# 5. **limpar_tela()**:
#    - Função auxiliar para limpar a tela atual, removendo todos os widgets (botões, labels, campos de texto, etc.) da janela.
#    - Utilizada antes de exibir novas telas ou formulários, para garantir que a interface gráfica não sobrecarregue com componentes antigos.
#
# ============================

# Função para criar a tela de inserção com base na tabela selecionada
def criar_formulario_insercao():
    # Obtém o nome da tabela selecionada na interface gráfica
    tabela = combo_tabela.get()
    
    # Limpa a tela atual antes de criar o novo formulário
    limpar_tela()

    # Verifica qual tabela foi selecionada e chama a função correspondente para criar o formulário
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
    elif tabela == "Exame Ortopédico":
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

# Função para criar o formulário de inserção de dados de Exame Neurológico
def criar_formulario_Neurologico():
    # Limpa a tela atual antes de exibir o novo formulário
    limpar_tela()

    # Criação dos campos de entrada (Entry) para dados de protocolo e ressonância
    entry_protocolo = tk.Entry(root)
    entry_ressonancia = tk.Entry(root)

    # Criação dos rótulos (Labels) para os campos de entrada
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    label_ressonancia = tk.Label(root, text="Link para os dados da Ressonância")
    label_ressonancia.grid(row=0, column=1, padx=20, pady=5)
    entry_ressonancia.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados inseridos
    def salvar_dados():
        # Coleta os dados inseridos nos campos de entrada
        dados = {
            'tabela': 'neurologico',  # Nome da tabela no banco de dados
            'protocolo': entry_protocolo.get().strip().upper(),  # Protocolo em formato específico
            'resssonancia': entry_ressonancia.get().strip()  # Link para os dados da ressonância
        }
        # Chama a função para inserir os dados no banco
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados no banco de dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=2, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=3, column=0, columnspan=2, pady=10)


# Função para criar o formulário de inserção de dados do Genoma
def criar_formulario_Genoma():
    # Limpa a tela atual antes de exibir o novo formulário
    limpar_tela()

    # Campos para armazenar os valores inseridos pelo usuário
    entry_atleta = tk.Entry(root)      # Campo de entrada para o CPF do atleta
    entry_genoma = tk.Entry(root)      # Campo de entrada para o link dos dados do genoma
    entry_mapeamento = tk.Entry(root)  # Campo de entrada para o protocolo do mapeamento genético

    # Layout do formulário:
    # Primeira coluna: Protocolo de Mapeamento Genético e CPF do Atleta
    label_mapeamento = tk.Label(root, text="Protocolo do Mapeamento Genético (Formato: XXXXXXXXX-YYY):")
    label_mapeamento.grid(row=0, column=0, padx=20, pady=5)
    entry_mapeamento.grid(row=1, column=0, padx=20, pady=5)

    label_atleta = tk.Label(root, text="CPF do Atleta:")
    label_atleta.grid(row=2, column=0, padx=20, pady=5)
    entry_atleta.grid(row=3, column=0, padx=20, pady=5)

    # Segunda coluna: Link para os dados do Genoma
    label_genoma = tk.Label(root, text="Link para os dados do Genoma")
    label_genoma.grid(row=0, column=1, padx=20, pady=5)
    entry_genoma.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados inseridos nos campos
    def salvar_dados():
        # Coleta os valores dos campos e organiza em um dicionário
        dados = {
            'tabela': 'genoma',  # Identificador da tabela no banco de dados
            'protocolo': entry_mapeamento.get().strip().upper(),  # Protocolo do mapeamento genético (em maiúsculas)
            'atleta': entry_atleta.get().strip().upper(),  # CPF do atleta (em maiúsculas, caso necessário)
            'genoma': entry_genoma.get().strip()  # Link para os dados do genoma
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados no banco de dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)


# Função para criar o formulário de inserção de dados de Imagem Óssea
def criar_formulario_Ossea():
    # Limpa a tela atual antes de exibir o novo formulário
    limpar_tela()

    # Campos para armazenar os valores inseridos pelo usuário
    entry_protocolo = tk.Entry(root)  # Campo de entrada para o protocolo do exame ortopédico
    entry_imagem = tk.Entry(root)    # Campo de entrada para o número da imagem
    entry_link = tk.Entry(root)      # Campo de entrada para o link do exame ortopédico

    # Layout do formulário:
    # Primeira coluna: Protocolo do Exame Ortopédico e Link
    label_protocolo = tk.Label(root, text="Protocolo do Exame Ortopédico (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    label_link = tk.Label(root, text="Link para o Exame Ortopédico")
    label_link.grid(row=2, column=0, padx=20, pady=5)
    entry_link.grid(row=3, column=0, padx=20, pady=5)

    # Segunda coluna: Número da Imagem
    label_imagem = tk.Label(root, text="Número da Imagem")
    label_imagem.grid(row=0, column=1, padx=20, pady=5)
    entry_imagem.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados inseridos nos campos
    def salvar_dados():
        # Coleta os valores dos campos e organiza em um dicionário
        dados = {
            'tabela': 'imagens',  # Identificador da tabela no banco de dados
            'protocolo': entry_protocolo.get().strip().upper(),  # Protocolo do exame ortopédico (em maiúsculas)
            'imagem': entry_imagem.get().strip().upper(),  # Número da imagem (em maiúsculas, caso necessário)
            'link': entry_link.get().strip()  # Link para o exame ortopédico
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados no banco de dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados do Mapeamento Genético
def criar_formulario_mapeamento():
    # Limpa a tela atual antes de exibir o novo formulário
    limpar_tela()

    # Campos para armazenar os valores inseridos pelo usuário
    entry_protocolo = tk.Entry(root)  # Campo de entrada para o protocolo do mapeamento genético
    entry_amostra = tk.Entry(root)    # Campo de entrada para o link da amostra biológica

    # Layout do formulário:
    # Primeira coluna: Protocolo do Mapeamento Genético
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    # Segunda coluna: Link para a Amostra Biológica
    label_amostra = tk.Label(root, text="Link da Amostra Biológica")
    label_amostra.grid(row=0, column=1, padx=20, pady=5)
    entry_amostra.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados inseridos nos campos
    def salvar_dados():
        # Coleta os valores dos campos e organiza em um dicionário
        dados = {
            'tabela': 'mapeamemnto',  # Identificador da tabela no banco de dados (corrigir erro de digitação: 'mapeamento')
            'protocolo': entry_protocolo.get().strip().upper(),  # Protocolo do mapeamento genético (em maiúsculas)
            'amostra': entry_amostra.get().strip()  # Link para a amostra biológica
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados no banco de dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=2, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=3, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados do Exame Cardiológico
def criar_formulario_cardiologico():
    # Limpa a tela atual antes de exibir o novo formulário
    limpar_tela()

    # Campos para armazenar os valores inseridos pelo usuário
    entry_protocolo = tk.Entry(root)  # Campo de entrada para o protocolo do exame cardiológico
    entry_ultrassom = tk.Entry(root)  # Campo de entrada para o link do ultrassom

    # Layout do formulário:
    # Primeira coluna: Protocolo do Exame Cardiológico
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    # Segunda coluna: Link do Ultrassom
    label_ultrassom = tk.Label(root, text="Link do Ultrassom")
    label_ultrassom.grid(row=0, column=1, padx=20, pady=5)
    entry_ultrassom.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados inseridos nos campos
    def salvar_dados():
        # Coleta os valores dos campos e organiza em um dicionário
        dados = {
            'tabela': 'cardiologico',  # Identificador da tabela no banco de dados
            'protocolo': entry_protocolo.get().strip().upper(),  # Protocolo do exame cardiológico (em maiúsculas)
            'ultrassom': entry_ultrassom.get().strip().upper()  # Link do ultrassom (em maiúsculas, caso necessário)
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados no banco de dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=2, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=3, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados do Exame Ortopédico
def criar_formulario_ortopedico():
    # Limpa a tela atual antes de exibir o novo formulário
    limpar_tela()

    # Campo para armazenar o valor inserido pelo usuário (Protocolo)
    entry_protocolo = tk.Entry(root)  # Campo de entrada para o protocolo do exame ortopédico

    # Layout do formulário:
    # Primeira coluna: Protocolo do Exame Ortopédico
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    # Função para salvar os dados inseridos no campo
    def salvar_dados():
        # Coleta o valor do campo e organiza em um dicionário
        dados = {
            'tabela': 'ortopedico',  # Identificador da tabela no banco de dados
            'protocolo': entry_protocolo.get().strip().upper()  # Protocolo do exame ortopédico (em maiúsculas)
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados no banco de dados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=2, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=3, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados para o Exame Médico
def criar_formulario_exame():
    # Limpa a tela atual antes de exibir o novo formulário
    limpar_tela()

    # Campos para armazenar os valores inseridos pelo usuário
    entry_protocolo = tk.Entry(root)  # Campo para o protocolo do exame
    entry_data = tk.Entry(root)  # Campo para a data e hora do exame
    entry_medico = tk.Entry(root)  # Campo para o nome do médico responsável
    entry_atleta = tk.Entry(root)  # Campo para o CPF do atleta
    entry_tipo = tk.Entry(root)  # Campo para o tipo do exame
    entry_nivelO = tk.Entry(root)  # Campo para o nível de oxigênio do atleta
    entry_pressao = tk.Entry(root)  # Campo para a pressão arterial do atleta
    entry_temp = tk.Entry(root)  # Campo para a temperatura do atleta

    # Layout do formulário:
    # Coluna 1: Campos relacionados aos dados principais do exame
    label_protocolo = tk.Label(root, text="Protocolo (Formato: XXXXXXXXX-YYY):")
    label_protocolo.grid(row=0, column=0, padx=20, pady=5)
    entry_protocolo.grid(row=1, column=0, padx=20, pady=5)

    label_atleta = tk.Label(root, text="CPF do Atleta:")
    label_atleta.grid(row=2, column=0, padx=20, pady=5)
    entry_atleta.grid(row=3, column=0, padx=20, pady=5)

    label_medico = tk.Label(root, text="Médico:")
    label_medico.grid(row=4, column=0, padx=20, pady=5)
    entry_medico.grid(row=5, column=0, padx=20, pady=5)

    label_data = tk.Label(root, text="Data e Hora:")
    label_data.grid(row=6, column=0, padx=20, pady=5)
    entry_data.grid(row=7, column=0, padx=20, pady=5)

    # Coluna 2: Campos relacionados ao exame do atleta
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

    # Função para salvar os dados coletados no banco de dados
    def salvar_dados():
        # Coleta os valores dos campos de entrada e organiza em um dicionário
        dados = {
            'tabela': 'exame',  # Identificador da tabela no banco de dados
            'protocolo': entry_protocolo.get().strip().upper(),  # Protocolo do exame
            'atleta': entry_atleta.get().strip().upper(),  # CPF do atleta
            'medico': entry_medico.get().strip().upper(),  # Nome do médico
            'data': entry_data.get().strip().upper(),  # Data e hora do exame
            'pressao': entry_pressao.get().strip().upper(),  # Pressão arterial
            'temp': entry_temp.get().strip().upper(),  # Temperatura do atleta
            'nivelO': entry_nivelO.get().strip().upper(),  # Nível de oxigênio do atleta
            'tipo': entry_tipo.get().strip().upper()  # Tipo de exame realizado
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=8, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=9, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados de vídeo
def criar_formulario_video():
    # Limpa a tela antes de exibir o novo formulário
    limpar_tela()

    # Campos para armazenar os valores inseridos pelo usuário
    entry_mac = tk.Entry(root)  # Campo para o MAC address do dispositivo
    entry_data = tk.Entry(root)  # Campo para a data e hora do vídeo
    entry_duracao = tk.Entry(root)  # Campo para a duração do vídeo
    entry_atleta = tk.Entry(root)  # Campo para o CPF do atleta
    entry_pdata = tk.Entry(root)  # Campo para a data da partida
    entry_plocal = tk.Entry(root)  # Campo para o local da partida
    entry_dado = tk.Entry(root)  # Campo para o link do vídeo

    # Layout do formulário:
    # Coluna 1: Campos relacionados ao vídeo e ao atleta
    label_mac = tk.Label(root, text=" MAC address (Formato: XX-XX-XX-XX-XX-XX):")
    label_mac.grid(row=0, column=0, padx=20, pady=5)
    entry_mac.grid(row=1, column=0, padx=20, pady=5)

    label_atleta = tk.Label(root, text="CPF do Atleta:")
    label_atleta.grid(row=2, column=0, padx=20, pady=5)
    entry_atleta.grid(row=3, column=0, padx=20, pady=5)

    label_duracao = tk.Label(root, text="Duração:")
    label_duracao.grid(row=4, column=0, padx=20, pady=5)
    entry_duracao.grid(row=5, column=0, padx=20, pady=5)

    label_data = tk.Label(root, text="Data e Hora:")
    label_data.grid(row=6, column=0, padx=20, pady=5)
    entry_data.grid(row=7, column=0, padx=20, pady=5)

    # Coluna 2: Campos relacionados ao vídeo e à partida
    label_dado = tk.Label(root, text="Link do vídeo:")
    label_dado.grid(row=0, column=1, padx=20, pady=5)
    entry_dado.grid(row=1, column=1, padx=20, pady=5)

    label_pdata = tk.Label(root, text="Data da Partida:")
    label_pdata.grid(row=2, column=1, padx=20, pady=5)
    entry_pdata.grid(row=3, column=1, padx=20, pady=5)

    label_plocal = tk.Label(root, text="Local da Partida:")
    label_plocal.grid(row=4, column=1, padx=20, pady=5)
    entry_plocal.grid(row=5, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados no banco de dados
    def salvar_dados():
        # Coleta os valores dos campos de entrada e organiza em um dicionário
        dados = {
            'tabela': 'video',  # Identificador da tabela no banco de dados
            'mac': entry_mac.get().strip().upper(),  # MAC address do dispositivo
            'atleta': entry_atleta.get().strip().upper(),  # CPF do atleta
            'duracao': entry_duracao.get().strip().upper(),  # Duração do vídeo
            'data': entry_data.get().strip().upper(),  # Data e hora do vídeo
            'plocal': entry_plocal.get().strip().upper(),  # Local da partida
            'pdata': entry_pdata.get().strip().upper(),  # Data da partida
            'dado': entry_dado.get().strip()  # Link para o vídeo
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=6, column=1, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=7, column=1, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados de uma disputa
def criar_formulario_disputa():
    # Campos para armazenar os valores inseridos pelo usuário
    entry_data = tk.Entry(root)  # Campo para a data da partida
    entry_local = tk.Entry(root)  # Campo para o local da partida
    entry_time = tk.Entry(root)  # Campo para a sigla do time
    entry_esporte = tk.Entry(root)  # Campo para a sigla do esporte

    # Layout do formulário:
    # Coluna 1: Campos relacionados à partida
    label_data = tk.Label(root, text="Data da Partida")
    label_data.grid(row=0, column=0, padx=20, pady=5)
    entry_data.grid(row=1, column=0, padx=20, pady=5)

    label_esporte = tk.Label(root, text="Sigla do Esporte (Formato: ABC)")
    label_esporte.grid(row=2, column=0, padx=20, pady=5)
    entry_esporte.grid(row=3, column=0, padx=20, pady=5)

    # Coluna 2: Campos relacionados ao time e ao local da partida
    label_time = tk.Label(root, text="Sigla do Time")
    label_time.grid(row=0, column=1, padx=20, pady=5)
    entry_time.grid(row=1, column=1, padx=20, pady=5)

    label_local = tk.Label(root, text="Local da Partida")
    label_local.grid(row=2, column=1, padx=20, pady=5)
    entry_local.grid(row=3, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados no banco de dados
    def salvar_dados():
        # Coleta os valores dos campos de entrada e organiza em um dicionário
        dados = {
            'tabela': 'disputa',  # Identificador da tabela no banco de dados
            'data': entry_data.get().strip().upper(),  # Data da partida
            'time': entry_time.get().strip().upper(),  # Sigla do time
            'esporte': entry_esporte.get().strip().upper(),  # Sigla do esporte
            'local': entry_local.get().strip().upper()  # Local da partida
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados de estatísticas de atleta em uma partida
def criar_formulario_est_atleta_partida():
    # Campos para armazenar os valores inseridos pelo usuário
    entry_data = tk.Entry(root)  # Campo para a data da partida
    entry_local = tk.Entry(root)  # Campo para o local da partida
    entry_criterio = tk.Entry(root)  # Campo para o nome da estatística avaliada
    entry_valor = tk.Entry(root)  # Campo para o valor da estatística
    entry_atleta = tk.Entry(root)  # Campo para o CPF do atleta

    # Layout do formulário:
    # Coluna 1: Campos relacionados à partida e estatística
    label_data = tk.Label(root, text="Data da Partida")
    label_data.grid(row=0, column=0, padx=20, pady=5)
    entry_data.grid(row=1, column=0, padx=20, pady=5)

    label_valor = tk.Label(root, text="Valor")
    label_valor.grid(row=2, column=0, padx=20, pady=5)
    entry_valor.grid(row=3, column=0, padx=20, pady=5)

    label_atleta = tk.Label(root, text="CPF do Atleta")
    label_atleta.grid(row=4, column=0, padx=20, pady=5)
    entry_atleta.grid(row=5, column=0, padx=20, pady=5)

    # Coluna 2: Campos relacionados à estatística e local
    label_criterio = tk.Label(root, text="Nome da estatística avaliada àquela partida")
    label_criterio.grid(row=0, column=1, padx=20, pady=5)
    entry_criterio.grid(row=1, column=1, padx=20, pady=5)

    label_local = tk.Label(root, text="Local da Partida")
    label_local.grid(row=2, column=1, padx=20, pady=5)
    entry_local.grid(row=3, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados no banco de dados
    def salvar_dados():
        # Coleta os valores dos campos de entrada e organiza em um dicionário
        dados = {
            'tabela': 'estat_atleta_partida',  # Identificador da tabela no banco de dados
            'data': entry_data.get().strip().upper(),  # Data da partida
            'criterio': entry_criterio.get().strip().upper(),  # Estatística avaliada
            'valor': entry_valor.get().strip().upper(),  # Valor da estatística
            'local': entry_local.get().strip().upper(),  # Local da partida
            'atleta': entry_atleta.get().strip().upper()  # CPF do atleta
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=1, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=1, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados de estatísticas de uma partida
def criar_formulario_est_partida():
    # Campos para armazenar os valores inseridos pelo usuário
    entry_data = tk.Entry(root)  # Campo para a data da partida
    entry_local = tk.Entry(root)  # Campo para o local da partida
    entry_criterio = tk.Entry(root)  # Campo para o nome da estatística avaliada
    entry_valor = tk.Entry(root)  # Campo para o valor da estatística

    # Layout do formulário:
    # Coluna 1: Campos relacionados à partida e estatística
    label_data = tk.Label(root, text="Data da Partida")
    label_data.grid(row=0, column=0, padx=20, pady=5)
    entry_data.grid(row=1, column=0, padx=20, pady=5)

    label_valor = tk.Label(root, text="Valor")
    label_valor.grid(row=2, column=0, padx=20, pady=5)
    entry_valor.grid(row=3, column=0, padx=20, pady=5)

    # Coluna 2: Campos relacionados à estatística e local
    label_criterio = tk.Label(root, text="Nome da estatística avaliada àquela partida")
    label_criterio.grid(row=0, column=1, padx=20, pady=5)
    entry_criterio.grid(row=1, column=1, padx=20, pady=5)

    label_local = tk.Label(root, text="Local da Partida")
    label_local.grid(row=2, column=1, padx=20, pady=5)
    entry_local.grid(row=3, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados no banco de dados
    def salvar_dados():
        # Coleta os valores dos campos de entrada e organiza em um dicionário
        dados = {
            'tabela': 'estat_partida',  # Identificador da tabela no banco de dados
            'data': entry_data.get().strip().upper(),  # Data da partida
            'criterio': entry_criterio.get().strip().upper(),  # Estatística avaliada
            'valor': entry_valor.get().strip().upper(),  # Valor da estatística
            'local': entry_local.get().strip().upper()  # Local da partida
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados de partida esportiva
def criar_formulario_partida():
    # Campos para armazenar os valores inseridos pelo usuário
    entry_data = tk.Entry(root)  # Campo para a data da partida
    entry_local = tk.Entry(root)  # Campo para o local da partida
    entry_nome = tk.Entry(root)  # Campo para o nome descritivo da partida
    entry_esporte = tk.Entry(root)  # Campo para a sigla do esporte

    # Layout do formulário:
    # Coluna 1: Campos relacionados à partida
    label_data = tk.Label(root, text="Data da Partida")
    label_data.grid(row=0, column=0, padx=20, pady=5)
    entry_data.grid(row=1, column=0, padx=20, pady=5)

    label_esporte = tk.Label(root, text="Sigla do Esporte (Formato: ABC)")
    label_esporte.grid(row=2, column=0, padx=20, pady=5)
    entry_esporte.grid(row=3, column=0, padx=20, pady=5)

    # Coluna 2: Campos relacionados ao nome e local da partida
    label_nome = tk.Label(root, text="Nome descritivo da Partida")
    label_nome.grid(row=0, column=1, padx=20, pady=5)
    entry_nome.grid(row=1, column=1, padx=20, pady=5)

    label_local = tk.Label(root, text="Local da Partida")
    label_local.grid(row=2, column=1, padx=20, pady=5)
    entry_local.grid(row=3, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados no banco de dados
    def salvar_dados():
        # Coleta os valores dos campos de entrada e organiza em um dicionário
        dados = {
            'tabela': 'partida',  # Identificador da tabela no banco de dados
            'data': entry_data.get().strip().upper(),  # Data da partida
            'nome': entry_nome.get().strip().upper(),  # Nome descritivo da partida
            'esporte': entry_esporte.get().strip().upper(),  # Sigla do esporte
            'local': entry_local.get().strip().upper()  # Local da partida
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados de time esportivo
def criar_formulario_time():
    # Campos para armazenar os valores inseridos pelo usuário
    entry_sigla = tk.Entry(root)  # Campo para a sigla do time (identificação curta)
    entry_esporte = tk.Entry(root)  # Campo para a sigla do esporte praticado pelo time
    entry_nome = tk.Entry(root)  # Campo para o nome completo do time
    entry_treinador = tk.Entry(root)  # Campo para o CPF do treinador do time

    # Layout do formulário:
    # Coluna 1: Campos relacionados à identificação e esporte do time
    label_sigla = tk.Label(root, text="Sigla do Time (Formato: ABCDE)")
    label_sigla.grid(row=0, column=0, padx=20, pady=5)
    entry_sigla.grid(row=1, column=0, padx=20, pady=5)

    label_esporte = tk.Label(root, text="Sigla do Esporte do Time (Formato: ABC)")
    label_esporte.grid(row=2, column=0, padx=20, pady=5)
    entry_esporte.grid(row=3, column=0, padx=20, pady=5)

    # Coluna 2: Campos relacionados ao nome e treinador do time
    label_nome = tk.Label(root, text="Nome do Time")
    label_nome.grid(row=0, column=1, padx=20, pady=5)
    entry_nome.grid(row=1, column=1, padx=20, pady=5)

    label_treinador = tk.Label(root, text="CPF do treinador")
    label_treinador.grid(row=2, column=1, padx=20, pady=5)
    entry_treinador.grid(row=3, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados no banco de dados
    def salvar_dados():
        # Coleta os valores dos campos de entrada e organiza-os em um dicionário
        dados = {
            'tabela': 'time',  # Identificador da tabela no banco de dados
            'sigla': entry_sigla.get().strip().upper(),  # Sigla do time
            'nome': entry_nome.get().strip().upper(),  # Nome completo do time
            'esporte': entry_esporte.get().strip().upper(),  # Sigla do esporte praticado
            'treinador': entry_treinador.get().strip().upper()  # CPF do treinador
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados sobre esporte
def criar_formulario_esporte():

    # Campos para armazenar os valores inseridos pelo usuário
    entry_sigla = tk.Entry(root)  # Campo para a sigla do esporte (ex: "FUT")
    entry_nome = tk.Entry(root)  # Campo para o nome completo do esporte (ex: "Futebol")
    entry_qnt = tk.Entry(root)  # Campo para a quantidade de times que jogam por vez

    # Layout do formulário:
    # Coluna 1: Campos relacionados à sigla e quantidade de times do esporte
    label_sigla = tk.Label(root, text="Sigla do Esporte (Formato: ABC)")
    label_sigla.grid(row=0, column=0, padx=20, pady=5)
    entry_sigla.grid(row=1, column=0, padx=20, pady=5)

    label_qnt = tk.Label(root, text="Quantidade de times por jogo")
    label_qnt.grid(row=2, column=0, padx=20, pady=5)
    entry_qnt.grid(row=3, column=0, padx=20, pady=5)

    # Coluna 2: Campo relacionado ao nome do esporte
    label_nome = tk.Label(root, text="Nome do Esporte")
    label_nome.grid(row=0, column=1, padx=20, pady=5)
    entry_nome.grid(row=1, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados
    def salvar_dados():
        # Coleta os valores dos campos e os organiza em um dicionário
        dados = {
            'tabela': 'esporte',  # Identificador da tabela no banco de dados
            'sigla': entry_sigla.get().strip().upper(),  # Sigla do esporte
            'nome': entry_nome.get().strip().upper(),  # Nome completo do esporte
            'qnt': entry_qnt.get().strip().upper()  # Quantidade de times por jogo
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=5, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados sobre o treinador
def criar_formulario_treinador():
    # Limpa a tela antes de criar o novo formulário
    limpar_tela()

    # Campos para armazenar os valores inseridos pelo usuário
    entry_cpf = tk.Entry(root)  # Campo para o CPF do treinador
    entry_cref = tk.Entry(root)  # Campo para o CREF (registro do treinador)
    entry_nome = tk.Entry(root)  # Campo para o nome completo do treinador
    entry_data = tk.Entry(root)  # Campo para a data de nascimento do treinador
    entry_rua = tk.Entry(root)  # Campo para a rua do endereço do treinador
    entry_numero = tk.Entry(root)  # Campo para o número do endereço
    entry_bairro = tk.Entry(root)  # Campo para o bairro do endereço
    entry_cep = tk.Entry(root)  # Campo para o CEP (Código de Endereçamento Postal)
    entry_uf = tk.StringVar()  # Variável para armazenar o estado (UF)
    entry_uf.set('')  # Valor padrão vazio para o dropdown de estados (UF)

    # Layout do formulário:
    # Coluna 1: Campos de dados pessoais do treinador
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

    # Coluna 2: Campos de endereço do treinador
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
    menu_uf = tk.OptionMenu(root, entry_uf, *estados)  # Dropdown para selecionar o estado (UF)
    menu_uf.grid(row=9, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados no formulário
    def salvar_dados():
        # Coleta os valores dos campos do formulário
        dados = {
            'tabela': 'treinador',  # Identificador da tabela no banco de dados
            'cpf': entry_cpf.get().strip().upper(),  # CPF do treinador
            'cref': entry_cref.get().strip().upper(),  # CREF do treinador
            'nome': entry_nome.get().strip().upper(),  # Nome completo do treinador
            'data': entry_data.get().strip().upper(),  # Data de nascimento do treinador
            'rua': entry_rua.get().strip().upper(),  # Rua do endereço
            'numero': entry_numero.get().strip().upper(),  # Número do endereço
            'bairro': entry_bairro.get().strip().upper(),  # Bairro do endereço
            'cep': entry_cep.get().strip().upper(),  # CEP do endereço
            'uf': entry_uf.get().strip().upper(),  # UF (estado) do endereço
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=10, column=0, columnspan=2, pady=10)

    # Botão de voltar para o menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=11, column=0, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados sobre o atleta
def criar_formulario_atleta():
    # Limpa a tela antes de criar o novo formulário
    limpar_tela()

    # Campos para armazenar os valores inseridos pelo usuário
    entry_cpf = tk.Entry(root)  # Campo para o CPF do atleta
    entry_id = tk.Entry(root)  # Campo para o ID do atleta
    entry_nome = tk.Entry(root)  # Campo para o nome completo do atleta
    entry_esporte = tk.Entry(root)  # Campo para a sigla do esporte praticado pelo atleta
    entry_time = tk.Entry(root)  # Campo para a sigla do time do atleta
    entry_data = tk.Entry(root)  # Campo para a data de nascimento do atleta
    entry_rua = tk.Entry(root)  # Campo para a rua do endereço do atleta
    entry_numero = tk.Entry(root)  # Campo para o número do endereço
    entry_bairro = tk.Entry(root)  # Campo para o bairro do endereço
    entry_cep = tk.Entry(root)  # Campo para o CEP (Código de Endereçamento Postal)
    entry_uf = tk.StringVar()  # Variável para armazenar o estado (UF)
    entry_uf.set('')  # Valor padrão vazio para o dropdown de estados (UF)

    # Layout do formulário:
    # Coluna 1: Campos de dados pessoais do atleta
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

    label_time = tk.Label(root, text="Sigla do time:")
    label_time.grid(row=8, column=0, padx=20, pady=5)
    entry_time.grid(row=9, column=0, padx=20, pady=5)

    label_data = tk.Label(root, text="Data de Nascimento:")
    label_data.grid(row=10, column=0, padx=20, pady=5)
    entry_data.grid(row=11, column=0, padx=20, pady=5)

    # Coluna 2: Campos de endereço do atleta
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
    menu_uf = tk.OptionMenu(root, entry_uf, *estados)  # Dropdown para selecionar o estado (UF)
    menu_uf.grid(row=9, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados no formulário
    def salvar_dados():
        # Coleta os valores dos campos do formulário
        dados = {
            'tabela': 'atleta',  # Identificador da tabela no banco de dados
            'cpf': entry_cpf.get().strip().upper(),  # CPF do atleta
            'id': entry_id.get().strip().upper(),  # ID do atleta
            'esporte': entry_esporte.get().strip().upper(),  # Sigla do esporte
            'time': entry_time.get().strip().upper(),  # Sigla do time
            'nome': entry_nome.get().strip().upper(),  # Nome completo do atleta
            'data': entry_data.get().strip().upper(),  # Data de nascimento do atleta
            'rua': entry_rua.get().strip().upper(),  # Rua do endereço
            'numero': entry_numero.get().strip().upper(),  # Número do endereço
            'bairro': entry_bairro.get().strip().upper(),  # Bairro do endereço
            'cep': entry_cep.get().strip().upper(),  # CEP do endereço
            'uf': entry_uf.get().strip().upper(),  # UF (estado) do endereço
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=10, column=1, columnspan=2, pady=10)

    # Botão de voltar para o menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=11, column=1, columnspan=2, pady=10)

# Função para criar o formulário de inserção de dados sobre o MÉDICO
def criar_formulario_medico():
    # Limpa a tela antes de criar o novo formulário
    limpar_tela()

    # Campos para armazenar os valores inseridos pelo usuário
    entry_cpf = tk.Entry(root)  # Campo para o CPF do médico
    entry_crm = tk.Entry(root)  # Campo para o CRM (registro profissional) do médico
    entry_nome = tk.Entry(root)  # Campo para o nome completo do médico
    entry_data = tk.Entry(root)  # Campo para a data de nascimento do médico
    entry_rua = tk.Entry(root)  # Campo para a rua do endereço do médico
    entry_numero = tk.Entry(root)  # Campo para o número do endereço
    entry_bairro = tk.Entry(root)  # Campo para o bairro do endereço
    entry_cep = tk.Entry(root)  # Campo para o CEP (Código de Endereçamento Postal)
    entry_uf = tk.StringVar()  # Variável para armazenar o estado (UF)
    entry_uf.set('')  # Valor padrão vazio para o dropdown de estados (UF)

    # Layout do formulário:
    # Coluna 1: Campos de dados pessoais do médico
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

    # Coluna 2: Campos de endereço do médico
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
    menu_uf = tk.OptionMenu(root, entry_uf, *estados)  # Dropdown para selecionar o estado (UF)
    menu_uf.grid(row=9, column=1, padx=20, pady=5)

    # Função para salvar os dados coletados no formulário
    def salvar_dados():
        # Coleta os valores dos campos do formulário
        dados = {
            'tabela': 'medico',  # Identificador da tabela no banco de dados
            'cpf': entry_cpf.get().strip().upper(),  # CPF do médico
            'crm': entry_crm.get().strip().upper(),  # CRM do médico
            'nome': entry_nome.get().strip().upper(),  # Nome completo do médico
            'data': entry_data.get().strip().upper(),  # Data de nascimento do médico
            'rua': entry_rua.get().strip().upper(),  # Rua do endereço
            'numero': entry_numero.get().strip().upper(),  # Número do endereço
            'bairro': entry_bairro.get().strip().upper(),  # Bairro do endereço
            'cep': entry_cep.get().strip().upper(),  # CEP do endereço
            'uf': entry_uf.get().strip().upper(),  # UF (estado) do endereço
        }
        # Chama a função para inserir os dados no banco de dados
        inserir_dados_no_banco(dados)

    # Botão para inserir os dados coletados
    button_inserir = tk.Button(root, text="Inserir", command=salvar_dados)
    button_inserir.grid(row=10, column=0, columnspan=2, pady=10)

    # Botão de voltar para o menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=11, column=0, columnspan=2, pady=10)

# Função para Exibir o Menu de Seleção de Ação
def exibir_menu():
    # Limpa a tela antes de exibir o menu
    limpar_tela()

    # Cria um label com o título "Menu de Ações" em formato de fonte grande
    label_menu = tk.Label(root, text="Menu de Ações", font=("Helvetica", 16))
    label_menu.pack(pady=20)  # Adiciona o label à interface com espaçamento

    # Cria um botão para inserir dados, que chama a função de exibição do submenu de inserção
    button_inserir = tk.Button(root, text="Inserir Dados", command=mostrar_submenu_insercao)
    button_inserir.pack(pady=10)  # Adiciona o botão à interface com espaçamento

    # Cria um botão para selecionar dados, que chama a função para exibir a tela de seleção
    button_selecionar = tk.Button(root, text="Selecionar Dados", command=exibir_selecao)
    button_selecionar.pack(pady=10)  # Adiciona o botão à interface com espaçamento

# Função para Exibir o Submenu de Inserção de Dados
def mostrar_submenu_insercao():
    # Limpa a tela antes de exibir o submenu de inserção
    limpar_tela()

    # Cria um label que informa ao usuário para escolher uma tabela para inserção de dados
    label_selecao = tk.Label(root, text="Escolha a tabela para inserir dados:")
    label_selecao.pack(pady=10)  # Adiciona o label à interface com espaçamento

    # Cria uma variável global para armazenar a tabela selecionada no combobox
    global combo_tabela
    combo_tabela = tk.StringVar()

    # Lista de tabelas disponíveis para inserção
    tabelas = ["Médico", "Treinador", "Esporte", "Time", "Atleta", "Partida", 
               "Estatística de Partida", "Disputa", "Estatística de Atleta na Partida", 
               "Video", "Exame", "Exame Ortopédico", "Exame Cardiológico", "Exame Neurológico", 
               "Mapeamento Genético", "Imagem Óssea", "Genoma"]

    # Define o valor padrão do combobox para a primeira tabela da lista
    combo_tabela.set(tabelas[0]) 

    # Cria o combobox com as opções de tabelas e adiciona à interface
    dropdown_tabela = tk.OptionMenu(root, combo_tabela, *tabelas)
    dropdown_tabela.pack(pady=10)  # Adiciona o combobox à interface com espaçamento

    # Cria um botão para confirmar a seleção da tabela e criar o formulário de inserção
    button_confirmar = tk.Button(root, text="Confirmar", command=criar_formulario_insercao)
    button_confirmar.pack(pady=10)  # Adiciona o botão à interface com espaçamento

    # Cria um botão para voltar ao menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.pack(pady=5)  # Adiciona o botão à interface com espaçamento


# Função para Limpar a Tela
def limpar_tela():
    # Itera sobre todos os widgets presentes na tela e os destrói, limpando a interface
    for widget in root.winfo_children():
        widget.destroy()

# Função para Inserir Dados no Banco de Dados Oracle
#
# Descrição:
# A função `inserir_dados_no_banco` tem como objetivo inserir dados em várias tabelas de um banco de dados Oracle 
# com base nas informações fornecidas em um dicionário. O dicionário contém dados sobre
# médicos, treinadores, atletas, esportes, partidas, entre outros, e a função adapta a inserção SQL conforme o tipo 
# de dados para realizar a inserção na tabela correspondente.
#
# A função segue os seguintes passos:
# 1. Conecta-se ao banco de dados Oracle usando a função `conectar_oracle`.
# 2. Verifica o valor da chave 'tabela' no dicionário de dados para determinar qual consulta SQL será executada.
# 3. Executa a consulta SQL de inserção de dados na tabela apropriada (por exemplo, "medico", "treinador", "atleta", etc.).
# 4. Após a execução da consulta, a transação é confirmada com `commit`.
# 5. Em caso de sucesso, exibe uma mensagem de confirmação.
# 6. Caso ocorra algum erro, uma mensagem de erro é exibida, e a transação é revertida com `rollback`.
#
# Parâmetros:
# - `dados` (dict): Dicionário contendo as informações a serem inseridas no banco de dados. 
#   O dicionário deve ter a chave 'tabela' que define qual tabela será afetada, e outras chaves 
#   que fornecem os dados específicos para a tabela selecionada.
#
# Exemplo de dicionário `dados`:
# dados = {
#     'tabela': 'medico',
#     'cpf': '123.456.789-00',
#     'crm': '123456',
#     'nome': 'Dr. João Silva',
#     'data': '1980-05-12',
#     'rua': 'Rua A',
#     'numero': '100',
#     'bairro': 'Centro',
#     'cep': '12345-678',
#     'uf': 'SP'
# }
#
# Observações:
# - A função é genérica e pode ser adaptada para inserções em diversas tabelas do banco de dados, 
#   bastando fornecer a chave correta ('medico', 'treinador', 'esporte', etc.) no dicionário `dados`.
# - A função utiliza comandos SQL preparados (com `:1`, `:2`, etc.) para evitar SQL injection.
#
# Exceções:
# - Se ocorrer qualquer erro durante a execução da consulta ou conexão com o banco, a transação é revertida 
#   (rollback) e uma mensagem de erro é exibida ao usuário.

def inserir_dados_no_banco(dados):
    try:        
        # Conectar ao banco de dados Oracle
        connection = conectar_oracle()
        
        # Verifica se a conexão foi bem-sucedida
        if connection:
            cursor = connection.cursor()

            # Dependendo da tabela informada nos dados, a inserção SQL será adaptada
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
                           VALUES (TO_DATE(:1, 'DD/MM/YYYY HH24:MI:SS'), :2, :3, :4)"""
                cursor.execute(query, (dados['data'], dados['local'], dados['nome'], dados['esporte']))
            elif dados['tabela'] == "estat_partida":
                query = """INSERT INTO ESTAT_PARTIDA (DATA, LOCAL, CRITERIO, VALOR)
                           VALUES (TO_DATE(:1, 'YYYY-MM-DD'), :2, :3, :4)"""
                cursor.execute(query, (dados['data'], dados['local'], dados['criterio'], dados['valor']))
            elif dados['tabela'] == "disputa":
                query = """INSERT INTO DISPUTA (SIGLA_TIME, SIGLA_ESPORTE, EST_DATA, EST_LOCAL)
                           VALUES (:1, :2, TO_DATE(:3, 'DD/MM/YYYY HH24:MI:SS'), :4)"""
                cursor.execute(query, (dados['time'], dados['esporte'], dados['data'], dados['local']))
            elif dados['tabela'] == "estat_atleta_partida":
                query = """INSERT INTO ESTAT_ATLETA_PARTIDA (ATLETA, EST_DATA, EST_LOCAL, CRITERIO, VALOR)
                           VALUES (:1, TO_DATE(:2, 'DD/MM/YYYY HH24:MI:SS'), :3, :4, :5)"""
                cursor.execute(query, (dados['atleta'], dados['data'], dados['local'], dados['criterio'], dados['valor']))
            elif dados['tabela'] == "video":
                # Para o caso do vídeo, temos de evitar sobreposição de um vídeo novo começar no meio de outro video
                # Primeiro, cria-se uma consulta SQL para buscar as gravações de vídeo existentes para o mesmo MAC_ADDRESS,
                # data da partida e local da partida. O objetivo é identificar se o novo vídeo se sobrepõe a gravações existentes.
                query_lista_gravacoes = """
                    SELECT V.DATA_HORA, V.DATA_HORA + (V.DURACAO/86400) AS FIM
                    FROM VIDEO V
                    WHERE V.MAC_ADDRESS = :1
                    AND V.PARTIDA_DATA = TO_DATE(:2, 'DD/MM/YYYY HH24:MI:SS')
                    AND V.PARTIDA_LOCAL = :3
                """
                
                cursor.execute(query_lista_gravacoes, (dados['mac'], dados['pdata'], dados['plocal']))
                
                # Obtém todos os resultados da consulta (todas as gravações que correspondem ao MAC_ADDRESS, 
                # data e local fornecidos).
                resultados = cursor.fetchall()
                
                # Converte a data e hora do novo vídeo para um objeto datetime, que será comparado com as gravações existentes.
                data_novo_video = datetime.strptime(dados['data'], '%d/%m/%Y %H:%M:%S')
                
                # Calcula o horário de fim do novo vídeo com base na duração fornecida (em segundos).
                fim_novo_video = data_novo_video + timedelta(seconds=int(dados['duracao']))
                
                # Itera sobre os resultados das gravações existentes para verificar se o novo vídeo se sobrepõe a alguma delas.
                for registro in resultados:
                    data_inicio_gravacao = registro[0]
                    data_fim_gravacao = registro[1]
                    
                    # Verifica se o novo vídeo se sobrepõe a uma gravação existente. A condição é verdadeira se o início
                    # do novo vídeo for antes do fim da gravação existente e o fim do novo vídeo for depois do início da gravação.
                    if (data_novo_video < data_fim_gravacao and fim_novo_video > data_inicio_gravacao):
                        # Se houver sobreposição, lança uma exceção para impedir a inserção do novo vídeo.
                        raise ValueError("Sobreposição de vídeo detectada! Não é possível inserir.")
                
                # Se não houver sobreposição, o novo vídeo pode ser inserido no banco de dados.
                query_insercao = """INSERT INTO VIDEO (MAC_ADDRESS, DATA_HORA, DURACAO, DADO_VIDEO, ATLETA, PARTIDA_DATA, PARTIDA_LOCAL)
                                    VALUES (:1, TO_DATE(:2, 'DD/MM/YYYY HH24:MI:SS'), :3, :4, :5, TO_DATE(:6, 'DD/MM/YYYY HH24:MI:SS'), :7)"""
                
                # Executa a inserção do novo vídeo na tabela "VIDEO" usando os dados fornecidos no dicionário 'dados'.
                cursor.execute(query_insercao, (dados['mac'], dados['data'], dados['duracao'], dados['dado'], dados['atleta'], dados['pdata'], dados['plocal']))


            elif dados['tabela'] == "exame":
                query = """INSERT INTO EXAME (PROTOCOLO, DATA_HORA, MEDICO, ATLETA, TIPO, NIVEL_OXIGENIO, PRESSAO_ATELTA, TEMPERATURA_ATLETA)
                           VALUES (:1, TO_DATE(:2, 'DD/MM/YYYY HH24:MI:SS'), :3, :4, :5, :6, :7, :8)"""
                cursor.execute(query, (dados['protocolo'], dados['data'], dados['medico'], dados['atleta'], dados['tipo'], dados['nivelO'], dados['pressao'], dados['temp']))
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
                cursor.execute(query, (dados['atleta'], dados["genoma"], dados["protocolo"]))
            
            # Confirma a transação
            connection.commit()
            
            # Exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Dados inseridos no banco de dados com sucesso!")
            
            # Fecha o cursor e a conexão com o banco de dados
            cursor.close()
            connection.close()
    
    except Exception as e:
        # Em caso de erro, exibe uma mensagem de erro e faz o rollback da transação
        messagebox.showerror("Erro", f"Erro ao inserir dados no banco: {e}")
        connection.rollback()

# Função para Exibir a Tela de Seleção de Esporte
#
# Descrição:
# A função `exibir_selecao` tem como objetivo exibir uma interface gráfica com Tkinter que permite ao usuário
# consultar jogadores registrados em um esporte específico. O usuário insere o nome do esporte em um campo de 
# texto, e ao clicar no botão "Pesquisar", a função consulta o banco de dados para obter a lista de jogadores 
# relacionados a esse esporte, juntamente com seus respectivos genomas e videos. A busca em questão filtra
# todos os jogadores que possuiram videos em todos os jogos em que seu time jogou
#
# Passos realizados pela função:
# 1. Chama a função `limpar_tela()` para limpar a interface antes de exibir a tela de seleção.
# 2. Exibe um campo de entrada (entry) para o usuário inserir o nome do esporte.
# 3. Define a função `consultar_jogadores_por_esporte`, que é chamada ao clicar no botão "Pesquisar".
# 4. A função de consulta realiza os seguintes passos:
#    - Valida se o nome do esporte foi informado.
#    - Conecta-se ao banco de dados Oracle e executa uma consulta SQL para buscar jogadores e seus genomas 
#      associados ao esporte informado.
#    - Faz a segunda busca, utilizando exclusçao de conjunto para executar a divisão
# 5. Caso não existam jogadores para o esporte especificado, exibe uma mensagem informando que nenhum jogador
#    foi encontrado.
# 6. Exibe mensagens de erro se houver falha na execução da consulta SQL ou problemas de conexão com o banco.
#
# Parâmetros: Nenhum.
#
# Exemplo de uso:
# Quando o usuário digita o nome de um esporte (por exemplo, "Futebol") e clica no botão "Pesquisar",
# a função irá consultar o banco de dados e exibir a lista de jogadores que praticam esse esporte, juntamente
# com seus respectivos genomas (se cadastrados) e videos.
#
# Observações:
# - A função usa o módulo `tkinter` para construir a interface gráfica.
# - Realiza uma consulta SQL com um `LEFT JOIN` para buscar o genoma dos atletas, considerando que um atleta
#   pode não ter um genoma cadastrado.
# - O código assume que a tabela `GENOMA` está associada ao atleta pela chave `ATLETA` (CPF), e que o esporte
#   é associado ao atleta através da chave `ATL_SIGLA_ESPORTE`.
#
# Exceções:
# - Se ocorrer um erro durante a consulta ao banco de dados ou na conexão, uma mensagem de erro será exibida.
# - Caso o nome do esporte não seja informado, uma mensagem de erro será mostrada solicitando o preenchimento.
def exibir_selecao():
    # Limpa a tela para preparar o layout da seleção de esporte
    limpar_tela()

    # Criação de um campo de entrada para o nome do esporte
    entry_esporte = tk.Entry(root)

    # Função para consultar jogadores e seus genomas com base no nome do esporte
    def consultar_jogadores_por_esporte():
        try:
            # Obtém o nome do esporte inserido pelo usuário no campo de entrada
            esporte_nome = entry_esporte.get().strip().upper()

            # Valida se o nome do esporte foi informado
            if not esporte_nome:
                # Exibe uma mensagem de erro caso o campo esteja vazio
                messagebox.showerror("Erro", "Por favor, insira o nome do esporte.")
                return

            # Conecta-se ao banco de dados Oracle
            connection = conectar_oracle()
            if connection:
                # Cria um cursor para executar as consultas no banco
                cursor = connection.cursor()

                # Consulta SQL para buscar jogadores e seus genomas e videos associados ao esporte informado, se cumprir a requisição
                query = """
                    SELECT A.NOME, G.GENOMA, V.DADO_VIDEO
                    FROM ATLETA A
                    LEFT JOIN GENOMA G ON A.CPF = G.ATLETA
                    JOIN ESPORTE E ON A.ATL_SIGLA_ESPORTE = E.SIGLA_ESPORTE
                    LEFT JOIN VIDEO V ON A.CPF = V.ATLETA
                    WHERE E.NOME = :esporte_nome 
                    AND V.DADO_VIDEO IS NOT NULL
                    AND NOT EXISTS (
                        SELECT D.EST_DATA, D.EST_LOCAL
                        FROM DISPUTA D
                        JOIN VIDEO V2 ON D.EST_DATA = V2.PARTIDA_DATA AND D.EST_LOCAL = V2.PARTIDA_LOCAL
                        JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME AND T.SIGLA_ESPORTE = D.SIGLA_ESPORTE
                        WHERE T.SIGLA_TIME = A.ATL_SIGLA_TIME
                        AND T.SIGLA_ESPORTE = A.ATL_SIGLA_ESPORTE
                        MINUS
                        SELECT D.EST_DATA, D.EST_LOCAL
                        FROM DISPUTA D
                        JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME AND T.SIGLA_ESPORTE = D.SIGLA_ESPORTE
                        WHERE T.SIGLA_TIME = A.ATL_SIGLA_TIME
                        AND T.SIGLA_ESPORTE = A.ATL_SIGLA_ESPORTE
                    )
                """

                # Executa a consulta passando o nome do esporte como parâmetro
                cursor.execute(query, {'esporte_nome': esporte_nome})

                # Obtém todos os resultados da consulta
                results = cursor.fetchall()

                # Limpa a área de texto antes de exibir novos resultados
                text_resultados.delete(1.0, tk.END)

                # Exibe os resultados na interface
                if results:
                    for row in results:
                        jogador = row[0]  # CPF do jogador
                        # Se o genoma estiver vazio, exibe "Genoma não cadastrado"
                        genoma = row[1] if row[1] else "Genoma não cadastrado"

                        link = row[2]
                        # Adiciona os resultados na área de texto
                        text_resultados.insert(tk.END, f"{jogador} | {genoma} | {link}\n")
                else:
                    messagebox.showinfo("Resultado", "Nenhum jogador encontrado para esse esporte.")

                # Fecha o cursor e a conexão com o banco de dados
                cursor.close()
                connection.close()

        # Caso ocorra algum erro na consulta ou conexão, exibe a mensagem de erro
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar dados: {e}")

    # Label explicativa para o campo de entrada do esporte
    label_esporte = tk.Label(root, text="Selecione o Esporte:")
    label_esporte.grid(row=0, column=0, padx=10, pady=5)

    # Coloca o campo de entrada para o nome do esporte na interface
    entry_esporte.grid(row=0, column=1, padx=10, pady=5)

    # Criação do botão "Pesquisar", que chama a função de consulta ao banco de dados
    button_pesquisar = tk.Button(root, text="Pesquisar", command=consultar_jogadores_por_esporte)
    button_pesquisar.grid(row=1, column=0, columnspan=2, pady=10)

    # Área de texto para exibir os resultados
    text_resultados = tk.Text(root, width=200, height=50)
    text_resultados.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    # Botão de voltar para o menu principal
    button_voltar = tk.Button(root, text="Voltar ao Menu Principal", command=exibir_menu)
    button_voltar.grid(row=3, column=0, columnspan=2, pady=10)

# ============================
# Função para Conectar ao Banco de Dados Oracle
# ============================
# A função a seguir estabelece uma conexão com o banco de dados Oracle usando a biblioteca 'oracledb'.
# Ela utiliza credenciais fixas (usuário, senha) e o Data Source Name (DSN) para a conexão.
# A função é projetada para:
# 1. Tentar conectar ao banco de dados usando o modo Thin Client.
# 2. Desabilitar o autocommit para permitir controle manual das transações.
# 3. Retornar a conexão bem-sucedida, ou exibir uma mensagem de erro em caso de falha.
#
# Retorno:
# - Retorna o objeto de conexão se bem-sucedido, ou None caso ocorra um erro.
# ============================

def conectar_oracle():
    # Dados de autenticação (usuário e senha) e DSN (Data Source Name) do banco
    username = ""
    password = ""
    dsn = ""
    
    try:
        # Tentativa de conexão com o banco de dados Oracle utilizando o modo Thin Client
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        connection.autocommit = False  # Desabilita o autocommit para controle manual das transações
        return connection  # Retorna a conexão bem-sucedida
        
    except oracledb.Error as e:
        # Exibe uma caixa de mensagem de erro caso a conexão falhe
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao Oracle Database: {e}")
        return None  # Retorna None caso ocorra um erro na conexão

# Criando a janela principal da interface gráfica
root = tk.Tk()

# Definindo o título da janela como "Menu Principal"
root.title("Menu Principal")

# Definindo o tamanho da janela como 500x700 pixels
root.geometry("500x700")

# Exibindo o menu inicial chamando a função 'exibir_menu'
exibir_menu()

# Iniciando o loop principal da interface gráfica, que mantém a janela aberta
root.mainloop()
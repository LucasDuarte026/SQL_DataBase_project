/* 
===================================================================================
Projeto: Sistema de Gestão de dados de Atletas Brasileiros em uma Edição Olímpica  
-----------------------------------------------------------------------------------
Descrição: Este arquivo contém o esquema SQL para a criação e manutenção do banco
           de dados do Sistema de Gestão Olímpica. Ele abrange entidades relacionadas
           a médicos, treinadores, atletas, times, estatísticas, exames, vídeos e
           outros elementos pertinentes ao contexto esportivo.

Criação: 05 de Dezembro de 2024
Última Atualização: 07 de Dezembro de 2024

Autor: Lucas Sales Duarte
Email: lucassalesduarte026@gmail.com
LinkedIn: https://www.linkedin.com/in/lucassalesduarte026/
GitHub: https://github.com/LucasDuarte026/

Licença: Licença MIT
-----------------------------------------------------------------------------------
Direitos Autorais (c) 2024 Lucas Sales Duarte

-----------------------------------------------------------------------------------
Instruções:
- Este arquivo SQL deve ser executado em um ambiente Oracle Database.
- Garanta que você tenha privilégios adequados antes de executar o script.
- Leia atentamente o relatório do projeto para execução ideal das tabelas.
===================================================================================
*/


----------------------- Criação de médico ---------------------
CREATE TABLE MEDICO (
    CPF CHAR (14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    CRM CHAR (6) NOT NULL, -- 6 dígitos para formar um CRM, segundo a Organização Brasileira de Médicos
    NOME VARCHAR2 (50) NOT NULL, -- Espera-se que 50 dígitos sejam suficientes para armazenar um nome
    DATA DATE, -- Data de nascimento do cidadão
    RUA VARCHAR2 (50) , -- nome da rua
    NUMERO NUMBER (4) , -- número da residência (0 à 9999)
    BAIRRO VARCHAR2 (25) , -- Bairro do endereço - espera-se que 25 caracteres seja suficiente para indicar o bairro
    CEP VARCHAR (9) , -- CEP do endereço com um formato especifico de 8 dígitos e 1 traço
    UF CHAR (2) , -- Estado do cidadão 2 caracteres são suficiente para cobrir todos os estados brasileiros
    CONSTRAINT PK_CPF_MEDICO PRIMARY KEY (CPF) , -- declaração de chave primária para o CPF
    CONSTRAINT SK_UNIQUE_MEDICO UNIQUE (CRM) , -- Garantir chave secundária       
    CONSTRAINT CK_CPF_MEDICO CHECK (REGEXP_LIKE (CPF, '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}') ) , -- Formatação de CPF no devido formato
    CONSTRAINT CK_CRM CHECK (REGEXP_LIKE (CRM, '[0-9]{6}') ) , -- Formatação de CRM no devido formato
    CONSTRAINT CK_CEP_MEDICO CHECK (REGEXP_LIKE (CEP, '[0-9]{5}\-[0-9]{3}') ) , -- formatação de CEP sob "XXXXX-YYY"
    CONSTRAINT CK_UF_MEDICO CHECK (UF IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO') ) -- garantir a inserção correta do estado da pessoa
);

----------------------- Criação de treinador ---------------------
CREATE TABLE TREINADOR (
    CPF CHAR (14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    CREF CHAR (6) NOT NULL, -- 6 dígitos para formar um CREF, segundo o concelho do CREF
    NOME VARCHAR2 (50) NOT NULL, -- Espera-se que 50 dígitos sejam suficientes para armazenar um nome
    DATA DATE, -- Data de nascimento do cidadão
    RUA VARCHAR2 (50) , -- nome da rua
    NUMERO NUMBER (4) , -- número da residência (0 à 9999)
    BAIRRO VARCHAR2 (25) , -- Bairro do endereço - espera-se que 25 caracteres seja suficiente para indicar o bairro
    CEP VARCHAR (9) , -- CEP do endereço com um formato especifico de 8 dígitos e 1 traço
    UF CHAR (2) , -- Estado do cidadão 2 caracteres são suficiente para cobrir todos os estados brasileiros
    CONSTRAINT PK_CPF_TREINADOR PRIMARY KEY (CPF) , -- declaração de chave primária para o CPF
    CONSTRAINT SK_UNIQUE_TREINADOR UNIQUE (CREF) , -- Garantir chave secundária       
    CONSTRAINT CK_CPF_TREINADOR CHECK (REGEXP_LIKE (CPF, '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}') ) , -- Formatação de CPF no devido formato
    CONSTRAINT CK_CREF CHECK (REGEXP_LIKE (CREF, '[0-9]{6}') ) , -- Formatação de CREF no devido formato
    CONSTRAINT CK_CEP_TREINADOR CHECK (REGEXP_LIKE (CEP, '[0-9]{5}\-[0-9]{3}') ) , -- formatação de CEP sob "XXXXX-YYY"
    CONSTRAINT CK_UF_TREINADOR CHECK (UF IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO') ) -- garantir a inserção correta do estado da pessoa
);

----------------------- Criação de esporte ---------------------
CREATE TABLE ESPORTE (
    SIGLA_ESPORTE CHAR (3) NOT NULL, -- Sigla única que mapeia até 999 esportes no campeonato, o que é suficiente
    NOME VARCHAR2 (50) NOT NULL, -- Nome do esporte
    QUANT_TIME_POR_JOGO NUMBER (2) NOT NULL, -- Armazena a quantidade de times possíveis em uma competição (99 é mais que suficiente)
    CONSTRAINT CK_ESPORTE PRIMARY KEY (SIGLA_ESPORTE) -- garantia de chave primária
);

----------------------- Criação de time ---------------------
CREATE TABLE TIME (
    SIGLA_TIME CHAR (5) NOT NULL, -- Sigla única que mapeia até 99999 TIMES no campeonato, o que é mais que suficiente
    SIGLA_ESPORTE CHAR (3) NOT NULL, -- Chave estrangeira para esporte
    NOME VARCHAR2 (50) NOT NULL, -- Nome do time
    CPF_TREINADOR CHAR (14) NOT NULL, -- Chave estrangeira para o cpf do treinador
    CONSTRAINT CK_UNIQUE_TIME UNIQUE (CPF_TREINADOR) , -- Garantir chave secundária
    CONSTRAINT PK_TIME PRIMARY KEY (SIGLA_TIME, SIGLA_ESPORTE) , -- Chave primária da tabela
    CONSTRAINT FK_TIME_ESPORTE FOREIGN KEY (SIGLA_ESPORTE) REFERENCES ESPORTE (SIGLA_ESPORTE) ON DELETE CASCADE, -- chave estrangeira para o esporte. Caso seja excluido, o time não faz mais sentido estar na base
    CONSTRAINT FK_TIME_TREINADOR FOREIGN KEY (CPF_TREINADOR) REFERENCES TREINADOR (CPF) -- chave estrangeira para o treinador. Caso o treinador saia, o time deve continuar
);

----------------------- Criação de ATLETA ---------------------
CREATE TABLE ATLETA (
    CPF CHAR (14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    NOME VARCHAR2 (50) NOT NULL, -- Espera-se que 50 dígitos sejam suficientes para armazenar um nome
    ATL_SIGLA_TIME CHAR (5), -- chave estrangeira para a sigla de time
    ATL_SIGLA_ESPORTE CHAR (3), -- Chave estrangeira para sigla esporte de time
    DATA DATE, -- Data de nascimento do cidadão
    RUA VARCHAR2 (50) , -- nome da rua
    NUMERO NUMBER (4) , -- número da residência (0 à 9999)
    BAIRRO VARCHAR2 (25) , -- Bairro do endereço - espera-se que 25 caracteres seja suficiente para indicar o bairro
    CEP VARCHAR (9) , -- CEP do endereço com um formato especifico de 8 dígitos e 1 traço
    UF CHAR (2) , -- Estado do cidadão 2 caracteres são suficiente para cobrir todos os estados brasileiros
    CONSTRAINT PK_CPF_ATLETA PRIMARY KEY (CPF) , -- declaração de chave primária para o CPF
    CONSTRAINT CK_CPF_ATLETA CHECK (REGEXP_LIKE (CPF, '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}') ) , -- Formatação de CPF no devido formato
    CONSTRAINT FK_ATL FOREIGN KEY (ATL_SIGLA_TIME, ATL_SIGLA_ESPORTE) REFERENCES TIME (SIGLA_TIME, SIGLA_ESPORTE) ON DELETE SET NULL, -- caso o time ou o esporte seja removido da Base, as informações do atleta devem permanecer no banco
    CONSTRAINT CK_CEP_ATLETA CHECK (REGEXP_LIKE (CEP, '[0-9]{5}\-[0-9]{3}') ) , -- formatação de CEP sob "XXXXX-YYY"
    CONSTRAINT CK_UF_ATLETA CHECK (UF IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO') ) -- garantir a inserção correta do estado da pessoa
);

----------------------- Criação de PARTIDA ---------------------
CREATE TABLE PARTIDA (
    DATA DATE NOT NULL, -- DATA E HORÁRIO DE COMEÇO DA PARTIDA
    LOCAL VARCHAR (50) NOT NULL, -- NOME DO LOCAL ONDE SERÁ FEITA A COMPETIÇÃO DAQUELE ESPORTE
    NOME VARCHAR2 (100) NOT NULL, -- NOME DESCRITIVO DA PARTIDA
    SIGLA_ESPORTE CHAR (3) NOT NULL, -- nome do esporte o qual joga o time
    CONSTRAINT PK_PAR PRIMARY KEY (DATA, LOCAL) , --  chave primária desta tabela
    CONSTRAINT FK_PAR_ESPORTE FOREIGN KEY (SIGLA_ESPORTE) REFERENCES ESPORTE (SIGLA_ESPORTE) -- FOI ESCOLHIDO não usar CASCADE POIS é interessante manter os dados de histórioco mesmo que uma tupla de esporte seja excluida
);

----------------------- Criação de ESTATISTICA DE PARTIDA ---------------------
CREATE TABLE ESTAT_PARTIDA (
    EST_DATA DATE NOT NULL, -- horario relativo à respectiva partida
    EST_LOCAL VARCHAR2 (50) NOT NULL, -- local respectivo à partida em que essa estatistica foi coletada
    CRITERIO VARCHAR (20) NOT NULL, -- nome da estatística avaliada àquela partida
    VALOR NUMBER (4) NOT NULL, -- Acredita-se que as estátisticas aqui sejam todas suficientes até o valor 9999
    CONSTRAINT PK_ESTAT_PARTIDA PRIMARY KEY (EST_DATA, EST_LOCAL, CRITERIO) , --
    CONSTRAINT FK_ESTAT_DATA FOREIGN KEY (EST_DATA, EST_LOCAL) REFERENCES PARTIDA (DATA, LOCAL) ON DELETE CASCADE -- faz sentido exluir pois não tem sentido guardar a estat caso a partida seja exluida
);

----------------------- Criação de DISPUTA ---------------------
CREATE TABLE DISPUTA (
    SIGLA_TIME CHAR (5) NOT NULL, -- Chave estrangeira para TIME
    SIGLA_ESPORTE CHAR (3) NOT NULL, -- Chave estrangeira para esporte
    EST_DATA DATE NOT NULL, -- Chave estrangeira para DATA E HORA DA PARTIDA
    EST_LOCAL VARCHAR2 (50) NOT NULL, -- Chave estrangeira para LOCAL
    CONSTRAINT PK_DIPUTA PRIMARY KEY (SIGLA_TIME, SIGLA_ESPORTE, EST_DATA, EST_LOCAL) , -- chave primária
    CONSTRAINT FK_DISPUTA_TIME FOREIGN KEY (SIGLA_TIME, SIGLA_ESPORTE) REFERENCES TIME (SIGLA_TIME, SIGLA_ESPORTE) , -- se querer guardar histórico
    CONSTRAINT FK_DISPUTA_DATA FOREIGN KEY (EST_DATA, EST_LOCAL) REFERENCES PARTIDA (DATA, LOCAL) ON DELETE CASCADE -- Aqui já não faz mais sentido guardar caso a partida em si tenha sido excluida
);

----------------------- Criação de ESTÁTISTICA DE ATLETA NA PARTIDA ---------------------
CREATE TABLE ESTAT_ATLETA_PARTIDA (
    ATLETA CHAR (14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    EST_DATA DATE NOT NULL, -- horario relativo à respectiva partida
    EST_LOCAL VARCHAR2 (50) NOT NULL, -- local respectivo à partida em que essa estatistica foi coletada
    CRITERIO VARCHAR (20) NOT NULL, -- nome da estatística avaliada àquela partida
    VALOR NUMBER (4) NOT NULL, -- Acredita-se que as estátisticas aqui sejam todas suficientes até o valor 9999
    CONSTRAINT FK_ESTAT_ATLETA_ATLETA FOREIGN KEY (ATLETA) REFERENCES ATLETA (CPF) ON DELETE CASCADE, -- não faz sentido guardar a estatistica de um atleta que não exista na base
    CONSTRAINT FK_ESTAT_ATLETA_PARTIDA_DATA FOREIGN KEY (EST_DATA, EST_LOCAL) REFERENCES PARTIDA (DATA, LOCAL) , -- é interessante guardar os dados do atleta, mesmo que a partida tenha sido removida
    CONSTRAINT PK_ESTAT_ATLETA_PARTIDA PRIMARY KEY (ATLETA, EST_DATA, EST_LOCAL, CRITERIO) -- chave primária de estatistica atleta partida
);

----------------------- Criação de VIDEO ---------------------
CREATE TABLE VIDEO (
    MAC_ADDRESS CHAR (17) NOT NULL, -- MAC address que segue o formato XX-XX-XX-XX-XX-XX
    DATA_HORA DATE NOT NULL, -- Data e hora de início do vídeo
    DURACAO NUMBER (2) NOT NULL, -- Acredita-se que qualquer vídeo seja menor que 1h39 minutos. Caso necessite de mais tempo, o vídeo deve ser dividido antes de entrar na Base de Dados
    DADO_VIDEO VARCHAR2 (255) , -- é um link para o video armazenado em outro repositório. Esta escolha é feita por escalabilidade, praticidade e custo em uma aplicação real
    ATLETA CHAR (14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    PARTIDA_DATA DATE NOT NULL, -- DATA E HORÁRIO DE COMEÇO DA PARTIDA
    PARTIDA_LOCAL VARCHAR (50) NOT NULL, -- NOME DO LOCAL ONDE SERÁ FEITA A COMPETIÇÃO DAQUELE ESPORTE
    CONSTRAINT PK_VIDEO PRIMARY KEY (MAC_ADDRESS, DATA_HORA) , -- chave Primária desta tabela
    CONSTRAINT FK_VIDEO_ATLETA FOREIGN KEY (ATLETA) REFERENCES ATLETA (CPF) , -- deseja-se que, mesmo que o atleta seja removido, o video continue existindo
    CONSTRAINT FK_VIDEO_PARTIDAHORA FOREIGN KEY (PARTIDA_DATA, PARTIDA_LOCAL) REFERENCES PARTIDA (DATA, LOCAL) , -- deseja-se que, mesmo que o partida seja removido, o video continue existindo
    CONSTRAINT CK_MAC_INSERT CHECK (REGEXP_LIKE (MAC_ADDRESS, '[0-9A-F]{2}\-[0-9A-F]{2}\-[0-9A-F]{2}\-[0-9A-F]{2}\-[0-9A-F]{2}\-[0-9A-F]{2}') ) -- formatar a entrada obrigatoriamente para ser do formato: XX-XX-XXXX-XX-XX
);

----------------------- Criação de EXAME GENÉRICO ---------------------
CREATE TABLE EXAME (
    PROTOCOLO CHAR (13) NOT NULL, -- PROTOCOLO no formato XXXXXXXXX-YYY para armazenar unicamente o protocolo -  9 letras MAIUSCULAS seguidas de 3 digitos numéricos
    DATA_HORA DATE NOT NULL, -- DATA E HORA DO EXAME
    MEDICO CHAR (14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    ATLETA CHAR (14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    TIPO CHAR (1) NOT NULL, -- VALOR CHAR para identificar o tipo do exame em si
    NIVEL_OXIGENIO NUMBER (2) , -- (pode ser nulo) NIVEL DE OXIGÊNIO EM PORCENTAGEM 0 - 99%
    PRESSAO_ATLETA CHAR (7) , -- (pode ser nulo) 2 valores, uma para a pressão baixa e outro para a pressão alta Pressão Arterial Diastólica (PAD) e Pressão Arterial Sistólica (PAS) formato: (XXX/YYY)
    TEMPERATURA_ATLETA CHAR (4) , -- (pode ser nulo) 0.0 a 99.9 é suficiente para armazenar a o valor em ºC de temperatura do cidadão
    CONSTRAINT PK_EXAME PRIMARY KEY (PROTOCOLO) , -- CHAVE PRIMÁRIA DA TABELA
    CONSTRAINT SK_EXAME UNIQUE (DATA_HORA, MEDICO, ATLETA) , -- CHAVE SECUNDÁRIA DA TABELA
    CONSTRAINT CK_EXAME_PROTOCOLO CHECK (REGEXP_LIKE (PROTOCOLO, '[a-zA-Z]{9}\-[0-9]{3}') ) , -- PROTOCOLO DO EXAME SEGUE UM PADRÃO DE IDENTITFICAÇÃO DE 9 LETRAS E 3 DÍGITOS
    CONSTRAINT CK_EXAME_TIPO CHECK (TIPO IN ('S', 'N', 'O', 'C', 'M') ) , -- EXAME PODE SER DE 5 TIPOS S: simples,'N'- NEUROLÓGICO, 'O' - ORTOPÉDICO, 'C' - Cardiaco, 'M' - mapeamento genético
    CONSTRAINT CK_EXAME_PRESSAO CHECK (REGEXP_LIKE (PRESSAO_ATLETA, '[0-9]{3}\/[0-9]{3}') ) , -- Pressão tem que seguir o formato XXX-YYY (PAD-PAS)
    CONSTRAINT CK_EXAME_TEMP CHECK (REGEXP_LIKE (TEMPERATURA_ATLETA, '[0-9]{2}\.[0-9]{1}') ) -- TEMPERATURA tem que seguir o formato XX.X
);

----------------------- Criação de EXAME ESPECIALIZADO ORTOPÉDICO ---------------------
CREATE TABLE ORTOPEDICO (
    EXAME CHAR (13) NOT NULL, -- PROTOCOLO no formato XXXXXXXXX-YYY para armazenar unicamente o protocolo -  9 letras seguidas de 3 digitos numéricos
    CONSTRAINT PK_EXAME_ORTOPEDICO PRIMARY KEY (EXAME) , -- CHAVE PRIMÁRIA DA TABELA
    CONSTRAINT FK_ORTOPEDICO FOREIGN KEY (EXAME) REFERENCES EXAME (PROTOCOLO) ON DELETE CASCADE -- NÃO FAZ SENTIDO EXISTIR O EXAME ESPECIALIZADO ORTOPÉDICO SE O EXAME ORIGINAL TIVER SIDO EXCLUÍDO
);

----------------------- Criação de EXAME ESPECIALIZADO NEUROLÓGICO ---------------------
CREATE TABLE NEUROLOGICO (
    EXAME CHAR (13) NOT NULL, -- PROTOCOLO no formato XXXXXXXXX-YYY para armazenar unicamente o protocolo -  9 letras seguidas de 3 digitos numéricos
    RESSONANCIA_MAGNETICA VARCHAR2 (255) NOT NULL, -- LINK PARA O ENDEREÇO ONDE ESTÁ O ARQUIVO VOLUMOSO DE DADOS DE RESSONCIA MAGNÉTICA DESTE EXAME ESPECIALIZADO
    CONSTRAINT PK_EXAME_NEUROLOGICO PRIMARY KEY (EXAME) , -- CHAVE PRIMÁRIA DA TABELA
    CONSTRAINT FK_NEUROLOGICO FOREIGN KEY (EXAME) REFERENCES EXAME (PROTOCOLO) ON DELETE CASCADE -- NÃO FAZ SENTIDO EXISTIR O EXAME ESPECIALIZADO NEUROLÓGICO SE O EXAME ORIGINAL TIVER SIDO EXCLUÍDO
);

----------------------- Criação de EXAME ESPECIALIZADO CARDIOLÓGICO ---------------------
CREATE TABLE CARDIOLOGICO (
    EXAME CHAR (13) NOT NULL, -- PROTOCOLO no formato XXXXXXXXX-YYY para armazenar unicamente o protocolo -  9 letras seguidas de 3 digitos numéricos
    ULTRASSOM VARCHAR2 (255) NOT NULL, -- LINK PARA O ENDEREÇO ONDE ESTÁ O ARQUIVO VOLUMOSO DE DADOS DA ULTRASSOM DESTE EXAME ESPECIALIZADO
    CONSTRAINT PK_EXAME_CARDIOLOGICO PRIMARY KEY (EXAME) , -- CHAVE PRIMÁRIA DA TABELA
    CONSTRAINT FK_CARDIOLOGICO FOREIGN KEY (EXAME) REFERENCES EXAME (PROTOCOLO) ON DELETE CASCADE -- NÃO FAZ SENTIDO EXISTIR O EXAME ESPECIALIZADO CARDIOLÓGICO SE O EXAME ORIGINAL TIVER SIDO EXCLUÍDO
);

----------------------- Criação de EXAME ESPECIALIZADO MAPEAMENTO_GENETICO ---------------------
CREATE TABLE MAPEAMENTO_GENETICO (
    EXAME CHAR (13) NOT NULL, -- PROTOCOLO no formato XXXXXXXXX-YYY para armazenar unicamente o protocolo -  9 letras seguidas de 3 digitos numéricos
    AMOSTRA_BIOLOGICA VARCHAR2 (255) NOT NULL, -- LINK PARA O ENDEREÇO ONDE ESTÁ O ARQUIVO VOLUMOSO DE DADOS DA AMOSTRA BIOLOGICA DESTE EXAME ESPECIALIZADO
    CONSTRAINT PK_EXAME_MAPEAMENTO_GENETICO PRIMARY KEY (EXAME) , -- CHAVE PRIMÁRIA DA TABELA
    CONSTRAINT FK_MAPEAMENTO_GENETICO FOREIGN KEY (EXAME) REFERENCES EXAME (PROTOCOLO) ON DELETE CASCADE -- NÃO FAZ SENTIDO EXISTIR O EXAME ESPECIALIZADO MAPEAMENTO GENÉTICO SE O EXAME ORIGINAL TIVER SIDO EXCLUÍDO
);

----------------------- Criação de GENOMA ---------------------
CREATE TABLE GENOMA (
    ATLETA CHAR (14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    GENOMA VARCHAR2 (255) NOT NULL, -- LINK PARA O ENDEREÇO ONDE ESTÁ O ARQUIVO VOLUMOSO DE DADOS DO GENOMA DO ATLETA
    MAPEAMENTO CHAR (13) NOT NULL, -- PROTOCOLO no formato XXXXXXXXX-YYY para armazenar unicamente o protocolo -  9 letras seguidas de 3 digitos numéricos
    CONSTRAINT PK_GENOMA PRIMARY KEY (ATLETA) , -- NÃO FAZ SENTIDO EXISTIR O GENOMA DEputa grupo heterogêneo UMA ATLETA FORA DA BASE DE DADOS
    CONSTRAINT FK_GENOMA_ATLETA FOREIGN KEY (ATLETA) REFERENCES ATLETA (CPF) ON DELETE CASCADE, -- NÃO FAZ SENTIDO EXISTIR O GENOMA DEputa grupo heterogêneo UMA ATLETA FORA DA BASE DE DADOS
    CONSTRAINT UNIQUE_MAP UNIQUE (MAPEAMENTO) , -- só pode haver um mapeamento relacionado com um genoma, pois é único
    CONSTRAINT FK_GENOMA_MAPEAMENTO FOREIGN KEY (MAPEAMENTO) REFERENCES MAPEAMENTO_GENETICO (EXAME) ON DELETE CASCADE -- NÃO FAZ SENTIDO EXISTIR O GENOMA DE UMA ATLETA FORA DA BASE DE DADOS
);

----------------------- Criação de IMAGEM ÓSSEA ---------------------
CREATE TABLE IMAGEM_OSSEA (
    EXAME_ORTOPEDICO CHAR (13) NOT NULL, -- PROTOCOLO no formato XXXXXXXXX-YYY para armazenar unicamente o protocolo -  9 letras seguidas de 3 digitos numéricos
    IMAGEM NUMBER (2) NOT NULL, -- espera-se que haja até 99 imagens por exame ortopédico ao máximo
    LINK VARCHAR2 (255) NOT NULL, -- LINK PARA O ENDEREÇO ONDE ESTÁ O ARQUIVO VOLUMOSO DE DADOS DA ULTRASSOM DESTE EXAME ESPECIALIZADO
    CONSTRAINT PK_IMAGEM_OSSEA PRIMARY KEY (EXAME_ORTOPEDICO, IMAGEM) , -- CHAVE PRIMÁRIA DA TABELA
    CONSTRAINT FK_IMAGEM_OSSEA FOREIGN KEY (EXAME_ORTOPEDICO) REFERENCES ORTOPEDICO (EXAME) ON DELETE CASCADE -- NÃO FAZ SENTIDO EXISTIR O EXAME ESPECIALIZADO CARDIOLÓGICO SE O EXAME ORIGINAL TIVER SIDO EXCLUÍDO
);

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- Caso se queira eliminar as tabelas  -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- -- Tabelas que dependem de outras (child tables)

-- DROP TABLE ESTAT_ATLETA_PARTIDA CASCADE CONSTRAINTS;
-- DROP TABLE DISPUTA CASCADE CONSTRAINTS;
-- DROP TABLE ESTAT_PARTIDA CASCADE CONSTRAINTS;
-- DROP TABLE ATLETA CASCADE CONSTRAINTS;

-- -- Tabelas que servem como referência para outras (parent tables)
-- DROP TABLE TIME CASCADE CONSTRAINTS;
-- DROP TABLE PARTIDA CASCADE CONSTRAINTS;
-- DROP TABLE ESPORTE CASCADE CONSTRAINTS;
-- DROP TABLE TREINADOR CASCADE CONSTRAINTS;
-- DROP TABLE MEDICO CASCADE CONSTRAINTS;

-- DROP TABLE video CASCADE CONSTRAINTS;
-- DROP TABLE EXAME CASCADE CONSTRAINTS;
-- DROP TABLE ORTOPEDICO CASCADE CONSTRAINTS;
-- DROP TABLE NEUROLOGICO CASCADE CONSTRAINTS;
-- DROP TABLE CARDIOLOGICO CASCADE CONSTRAINTS;
-- DROP TABLE MAPEAMENTO_GENETICO CASCADE CONSTRAINTS;
-- DROP TABLE GENOMA CASCADE CONSTRAINTS;
-- DROP TABLE IMAGEM_OSSEA CASCADE CONSTRAINTS;

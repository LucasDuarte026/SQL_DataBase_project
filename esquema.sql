----------------------- Criação de médico ---------------------
CREATE TABLE MEDICO (
    CPF CHAR(14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    CRM CHAR(6) NOT NULL, -- 6 dígitos para formar um CRM, segundo a Organização Brasileira de Médicos
    NOME VARCHAR2(50) NOT NULL, -- Espera-se que 50 dígitos sejam suficientes para armazenar um nome
    DATA DATE, -- Data de nascimento do cidadão
    RUA VARCHAR2(50), -- nome da rua
    NUMERO NUMBER(4), -- número da residência
    BAIRRO VARCHAR2(25), -- Bairro do endereço
    CEP VARCHAR(9), -- CEP do endereço
    UF CHAR(2), -- Estado do cidadão
    CONSTRAINT PK_CPF_MEDICO PRIMARY KEY(CPF), -- declaração de chave primária para o CPF
    CONSTRAINT CK_CPF_MEDICO CHECK(REGEXP_LIKE(CPF, '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}')), -- Formatação de CPF no devido formato
    CONSTRAINT CK_CRM CHECK(REGEXP_LIKE(CRM, '[0-9]{6}')), -- Formatação de CRM no devido formato
    CONSTRAINT CK_CEP_MEDICO CHECK (REGEXP_LIKE(CEP, '[0-9]{5}\-[0-9]{3}')), -- formatação de CEP sob "XXXXX-YYY"
    CONSTRAINT CK_UF_MEDICO CHECK( UF IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'))
);

----------------------- Criação de treinador ---------------------
CREATE TABLE TREINADOR (
    CPF CHAR(14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    CREF CHAR(6) NOT NULL, -- 6 dígitos para formar um CREF, segundo o concelho do CREF
    NOME VARCHAR2(50) NOT NULL, -- Espera-se que 50 dígitos sejam suficientes para armazenar um nome
    DATA DATE, -- Data de nascimento do cidadão
    RUA VARCHAR2(50), -- nome da rua
    NUMERO NUMBER(4), -- número da residência
    BAIRRO VARCHAR2(25), -- Bairro do endereço
    CEP VARCHAR(9), -- CEP do endereço
    UF CHAR(2), -- Estado do cidadão
    CONSTRAINT PK_CPF_TREINADOR PRIMARY KEY(CPF), -- declaração de chave primária para o CPF
    CONSTRAINT CK_CPF_TREINADOR CHECK(REGEXP_LIKE(CPF, '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}')), -- Formatação de CPF no devido formato
    CONSTRAINT CK_CREF CHECK(REGEXP_LIKE(CREF, '[0-9]{6}')), -- Formatação de CREF no devido formato
    CONSTRAINT CK_CEP_TREINADOR CHECK (REGEXP_LIKE(CEP, '[0-9]{5}\-[0-9]{3}')), -- formatação de CEP sob "XXXXX-YYY"
    CONSTRAINT CK_UF_TREINADOR CHECK( UF IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'))
);

----------------------- Criação de esporte ---------------------
CREATE TABLE ESPORTE (
    SIGLA_ESPORTE CHAR(3) NOT NULL, -- Sigla única que mapeia até 999 esportes no campeonato, o que é suficiente
    NOME VARCHAR2(50) NOT NULL, -- Nome do esporte
    QUANT_TIME_POR_JOGO NUMBER(2) NOT NULL, -- Armazena a quantidade de times possíveis em uma competição (99 é mais que suficiente)
    CONSTRAINT CK_ESPORTE PRIMARY KEY(SIGLA_ESPORTE)
);

----------------------- Criação de time ---------------------
CREATE TABLE TIME (
    SIGLA_TIME CHAR(5) NOT NULL, -- Sigla única que mapeia até 99999 TIMES no campeonato, o que é mais que suficiente
    SIGLA_ESPORTE CHAR(3) NOT NULL, -- Chave estrangeira para esporte
    NOME VARCHAR2(50) NOT NULL, -- Nome do time
    CPF_TREINADOR CHAR(14) NOT NULL, -- Chave estrangeira para o cpf do treinador
    CONSTRAINT CK_UNIQUE_TIME UNIQUE(CPF_TREINADOR),
    CONSTRAINT PK_TIME PRIMARY KEY (SIGLA_TIME, SIGLA_ESPORTE),
    CONSTRAINT FK_TIME_ESPORTE FOREIGN KEY(SIGLA_ESPORTE) REFERENCES ESPORTE(SIGLA_ESPORTE) ON DELETE CASCADE,
    CONSTRAINT FK_TIME_TREINADOR FOREIGN KEY(CPF_TREINADOR) REFERENCES TREINADOR(CPF) ON DELETE CASCADE
);

----------------------- Criação de ATLETA ---------------------
CREATE TABLE ATLETA (
    CPF CHAR(14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    ID_ATLETA CHAR(5) NOT NULL, -- 5 digitos para identificação unitária do atleta dentro do campeonato da olimpíada
    NOME VARCHAR2(50) NOT NULL, -- Espera-se que 50 dígitos sejam suficientes para armazenar um nome
    ATL_SIGLA_TIME CHAR(5) NOT NULL, -- chave estrangeira para a sigla de time
    ATL_SIGLA_ESPORTE CHAR(3) NOT NULL, -- Chave estrangeira para sigla esporte de time
    DATA DATE, -- Data de nascimento do cidadão
    RUA VARCHAR2(50), -- nome da rua
    NUMERO NUMBER(4), -- número da residência
    BAIRRO VARCHAR2(25), -- Bairro do endereço
    CEP VARCHAR(9), -- CEP do endereço
    UF CHAR(2), -- Estado do cidadão
    CONSTRAINT PK_CPF_ATLETA PRIMARY KEY(CPF), -- declaração de chave primária para o CPF
    CONSTRAINT CK_CPF_ATLETA CHECK(REGEXP_LIKE(CPF, '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}')), -- Formatação de CPF no devido formato
    CONSTRAINT CK_ID CHECK(REGEXP_LIKE(ID_ATLETA, '[0-9]{5}')), -- Formatação de CPF no devido formato
    CONSTRAINT FK_ATL FOREIGN KEY(ATL_SIGLA_TIME, ATL_SIGLA_ESPORTE) REFERENCES TIME(SIGLA_TIME, SIGLA_ESPORTE) ON DELETE SET NULL,
    CONSTRAINT CK_CEP_ATLETA CHECK (REGEXP_LIKE(CEP, '[0-9]{5}\-[0-9]{3}')), -- formatação de CEP sob "XXXXX-YYY"
    CONSTRAINT CK_UF_ATLETA CHECK( UF IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'))
);

----------------------- Criação de PARTIDA ---------------------
CREATE TABLE PARTIDA (
    DATA DATE NOT NULL, -- DATA E HORÁRIO DE COMEÇO DA PARTIDA
    LOCAL VARCHAR(50) NOT NULL, -- NOME DO LOCAL ONDE SERÁ FEITA A COMPETIÇÃO DAQUELE ESPORTE
    NOME VARCHAR2(100) NOT NULL, -- NOME DESCRITIVO DA PARTIDA (AMISTOSO ENTRE SÃO PAULO E PALMEIRAS)
    SIGLA_ESPORTE CHAR(3) NOT NULL,
    CONSTRAINT PK_PAR PRIMARY KEY(DATA, LOCAL), --  chave primária desta tabela
    CONSTRAINT FK_PAR_ESPORTE FOREIGN KEY (SIGLA_ESPORTE) REFERENCES ESPORTE(SIGLA_ESPORTE) -- FOI ESCOLHIDO não usar CASCADE POIS é interessante manter os dados de histórioco mesmo que uma tupla de esporte seja excluida
);

----------------------- Criação de ESTATISTICA DE PARTIDA ---------------------
CREATE TABLE ESTAT_PARTIDA (
    EST_DATA DATE NOT NULL, -- horario relativo à respectiva partida
    EST_LOCAL VARCHAR2(50) NOT NULL, -- local respectivo à partida em que essa estatistica foi coletada
    CRITERIO VARCHAR(20) NOT NULL, -- nome da estatística avaliada àquela partida
    VALOR NUMBER(4) NOT NULL, -- Acredita-se que as estátisticas aqui sejam todas suficientes até o valor 9999
    CONSTRAINT PK_ESTAT_PARTIDA PRIMARY KEY(EST_DATA, EST_LOCAL, CRITERIO),
    CONSTRAINT FK_ESTAT_DATA FOREIGN KEY(EST_DATA, EST_LOCAL) REFERENCES PARTIDA(DATA, LOCAL) ON DELETE CASCADE -- faz sentido exluir pois não tem sentido guardar a estat caso a partida seja exluida  
);

----------------------- Criação de DISPUTA ---------------------
CREATE TABLE DISPUTA (
    SIGLA_TIME CHAR(5) NOT NULL, -- Chave estrangeira para TIME
    SIGLA_ESPORTE CHAR(3) NOT NULL, -- Chave estrangeira para esporte
    EST_DATA DATE NOT NULL, -- Chave estrangeira para DATA E HORA DA PARTIDA
    EST_LOCAL VARCHAR2(50) NOT NULL, -- Chave estrangeira para LOCAL
    CONSTRAINT PK_DIPUTA PRIMARY KEY (SIGLA_TIME, SIGLA_ESPORTE, EST_DATA, EST_LOCAL),
    CONSTRAINT FK_DISPUTA_TIME FOREIGN KEY (SIGLA_TIME, SIGLA_ESPORTE) REFERENCES TIME(SIGLA_TIME, SIGLA_ESPORTE), -- Time faz sentido não cascade pois quer guardar histórico
    CONSTRAINT FK_DISPUTA_DATA FOREIGN KEY (EST_DATA, EST_LOCAL) REFERENCES PARTIDA(DATA, LOCAL) ON DELETE CASCADE -- Aqui já não faz mais sentido guardar
);

----------------------- Criação de ESTÁTISTICA DE ATLETA NA PARTIDA ---------------------
CREATE TABLE ESTAT_ATLETA_PARTIDA (
    ATLETA CHAR(14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    EST_DATA DATE NOT NULL, -- horario relativo à respectiva partida
    EST_LOCAL VARCHAR2(50) NOT NULL, -- local respectivo à partida em que essa estatistica foi coletada
    CRITERIO VARCHAR(20) NOT NULL, -- nome da estatística avaliada àquela partida
    VALOR NUMBER(4) NOT NULL, -- Acredita-se que as estátisticas aqui sejam todas suficientes até o valor 9999
    CONSTRAINT PK_ESTAT_ATLETA_PARTIDA PRIMARY KEY(EST_DATA, EST_LOCAL, CRITERIO),
    CONSTRAINT FK_ESTAT_ATLETA_PARTIDA_DATA FOREIGN KEY(EST_DATA, EST_LOCAL) REFERENCES PARTIDA(DATA, LOCAL) ON DELETE CASCADE
);

DELETE
    FROM PARTIDA A
    WHERE A.SIGLA_ESPORTE ='222';

SELECT *
    FROM PARTIDA A
    WHERE A.SIGLA_ESPORTE ='222';


DROP TABLE PARTIDA  CASCADE CONSTRAINTS;
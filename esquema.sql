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
    CPF_TREINADOR char(14) NOT NULL, -- Chave estrangeira para o cpf do treinador
    CONSTRAINT PK_TIME PRIMARY KEY (SIGLA_TIME),
    CONSTRAINT FK_TIME_ESPORTE FOREIGN KEY(SIGLA_ESPORTE) REFERENCES ESPORTE(SIGLA_ESPORTE) ON DELETE CASCADE,
    CONSTRAINT FK_TIME_TREINADOR FOREIGN KEY(CPF_TREINADOR) REFERENCES TREINADOR(CPF) ON DELETE CASCADE
);

CREATE TABLE ATLETA (
    CPF CHAR(14) NOT NULL, -- 11 dígitos para o cpf e 4 para ponto e hífen
    ID_ATLETA CHAR(5) NOT NULL -- 5 digitos para identificação unitária do atleta dentro do campeonato da olimpíada
    NOME VARCHAR2(50) NOT NULL, -- Espera-se que 50 dígitos sejam suficientes para armazenar um nome
    TIME ESPORTE DATA DATE, -- Data de nascimento do cidadão
    RUA VARCHAR2(50), -- nome da rua
    NUMERO NUMBER(4), -- número da residência
    BAIRRO VARCHAR2(25), -- Bairro do endereço
    CEP VARCHAR(9), -- CEP do endereço
    UF CHAR(2), -- Estado do cidadão
    CONSTRAINT PK_CPF_ATLETA PRIMARY KEY(CPF), -- declaração de chave primária para o CPF
    CONSTRAINT CK_CPF_ATLETA CHECK(REGEXP_LIKE(CPF, '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}')), -- Formatação de CPF no devido formato
    CONSTRAINT CK_ID CHECK(REGEXP_LIKE(ID_ATLETA, '[0-9]{5}')), -- Formatação de CPF no devido formato
    CONSTRAINT CK_CEP_ATLETA CHECK (REGEXP_LIKE(CEP, '[0-9]{5}\-[0-9]{3}')), -- formatação de CEP sob "XXXXX-YYY"
    CONSTRAINT CK_UF_ATLETA CHECK( UF IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'))
);

DROP TABLE MEDICO;
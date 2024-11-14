CREATE TABLE MEDICO (
    CPF CHAR(14) NOT NULL,  -- 11 dígitos para o cpf e 4 para ponto e hífen
    CRM CHAR(6) NOT NULL,   -- 6 dígitos para formar um CRM, segundo a Organização Brasileira de Médicos
    NOME CHAR(50) NOT NULL, -- Espera-se que 50 dígitos sejam suficientes para armazenar um nome
    DATA DATE,  
    RUA VARCHAR(50),
    NUMERO NUMBER(4),
    BAIRRO VARCHAR2(25),
    CEP VARCHAR(9),
    UF CHAR(2),
    CONSTRAINT PK_CPF PRIMARY KEY(CPF),
    CONSTRAINT CK_CEP CHECK (REGEXP_LIKE(CEP, '[0-9]{5}\-[0-9]{3}')),
    CONSTRAINT CK_CPF CHECK(REGEXP_LIKE(CPF, '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}')), -- Formatação de CPF no devido formato
    CONSTRAINT CK_CRM CHECK(REGEXP_LIKE(CRM, '[0-9]{6}')),-- Formatação de CPF no devido formato
    CONSTRAINT CK_UF CHECK( UF IN ('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'))

);

DROP TABLE MEDICO;
-- inserts com UPPER(TRIM()) EM TODOS OS NOMES
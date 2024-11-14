----------------------- Inserções de médico ---------------------
INSERT INTO MEDICO(
    CPF,
    CRM,
    NOME,
    DATA,
    RUA,
    NUMERO,
    BAIRRO,
    CEP,
    UF
) VALUES (
    '111.222.333-44',
    '123456',
    UPPER(TRIM('Daniel Uemeda Kuhn')),
    TO_DATE('19/04/2003', 'DD/MM/YYYY'),
    UPPER(TRIM('rua alfredo maffei')),
    123,
    UPPER(TRIM('Lutfala')),
    '12345-678',
    UPPER(TRIM('SP'))
);

INSERT INTO MEDICO(
    CPF,
    CRM,
    NOME,
    DATA,
    RUA,
    NUMERO,
    BAIRRO,
    CEP,
    UF
) VALUES (
    '222.333.444-55',
    '234567',
    UPPER(TRIM(' Daniel Diaz Filhe ')),
    TO_DATE('16/02/2003', 'DD/MM/YYYY'),
    UPPER(TRIM('rua adorfo castoni')),
    336,
    UPPER(TRIM('macarenco')),
    '22545-678',
    UPPER(TRIM('GO'))
);

----------------------- Inserções de esporte ---------------------
INSERT INTO ESPORTE(
    SIGLA_ESPORTE,
    NOME,
    QUANT_TIME_POR_JOGO
) VALUES (
    '111',
    UPPER(TRIM('futebol')),
    2
);

INSERT INTO ESPORTE(
    SIGLA_ESPORTE,
    NOME,
    QUANT_TIME_POR_JOGO
) VALUES (
    '112',
    UPPER(TRIM('futebol FEMININO')),
    2
);


INSERT INTO ESPORTE(
    SIGLA_ESPORTE,
    NOME,
    QUANT_TIME_POR_JOGO
) VALUES (
    '222',
    UPPER(TRIM('voleibol')),
    2
);

INSERT INTO ESPORTE(
    SIGLA_ESPORTE,
    NOME,
    QUANT_TIME_POR_JOGO
) VALUES (
    '333',
    UPPER(TRIM('atletismo')),
    8
);

----------------------- Inserções de treinador ---------------------
INSERT INTO TREINADOR(
    CPF,
    CREF,
    NOME,
    DATA,
    RUA,
    NUMERO,
    BAIRRO,
    CEP,
    UF
) VALUES (
    '445.555.111-77',
    '449354',
    UPPER(TRIM('Philliph Rigolão')),
    TO_DATE('17/05/2006', 'DD/MM/YYYY'),
    UPPER(TRIM('rua ibatexas do norte')),
    123,
    UPPER(TRIM('Longe do sul')),
    '55555-678',
    UPPER(TRIM(' Am'))
);

INSERT INTO TREINADOR(
    CPF,
    CREF,
    NOME,
    DATA,
    RUA,
    NUMERO,
    BAIRRO,
    CEP,
    UF
) VALUES (
    '234.565.211-17',
    '917382',
    UPPER(TRIM('Arthur Leme')),
    TO_DATE('17/05/2006', 'DD/MM/YYYY'),
    UPPER(TRIM('rua juazeiro jo norte')),
    12,
    UPPER(TRIM('Longe do sul')),
    '84213-121',
    UPPER(TRIM(' MG'))
);

----------------------- Inserções de time ---------------------
INSERT INTO TIME (
    SIGLA_TIME,
    SIGLA_ESPORTE,
    NOME,
    CPF_TREINADOR
) VALUES(
    '999',
    '111',
    UPPER(TRIM('FUTEBOL MASCULINO BRASIL')),
    '445.555.111-77'
);

INSERT INTO TIME (
    SIGLA_TIME,
    SIGLA_ESPORTE,
    NOME,
    CPF_TREINADOR
) VALUES(
    '989',
    '112',
    UPPER(TRIM('FUTEBOL FEMININO BRASIL')),
    '234.565.211-17'
);

----------------------- Inserções de atleta ---------------------

-- inserts com UPPER(TRIM()) EM TODOS OS NOMES
-- DELETE FROM MEDICO WHERE CRM = 123456
----------------------- Inserções de médico ---------------------
INSERT INTO MEDICO(
    CPF, CRM, NOME, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '111.222.333-44', '123456', UPPER(TRIM('Daniel Uemeda Kuhn ')), TO_DATE('19/04/2003', 'DD/MM/YYYY'), UPPER(TRIM('rua alfredo maffei')), 123, UPPER(TRIM('Lutfala')), '12345-678', UPPER(TRIM('SP'))
);

INSERT INTO MEDICO(
    CPF, CRM, NOME, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '222.333.444-55', '234567', UPPER(TRIM(' Daniel Diaz Filhe ')), TO_DATE('16/02/2003', 'DD/MM/YYYY'), UPPER(TRIM('rua adorfo castoni')), 336, UPPER(TRIM('macarenco')), '22545-678', UPPER(TRIM('GO'))
);

----------------------- Inserções de esporte ---------------------
INSERT INTO ESPORTE(
    SIGLA_ESPORTE, NOME, QUANT_TIME_POR_JOGO
)VALUES(
    '111', UPPER(TRIM('futebol')), 2
);

INSERT INTO ESPORTE(
    SIGLA_ESPORTE, NOME, QUANT_TIME_POR_JOGO
)VALUES(
    '112', UPPER(TRIM('futebol FEMININO')), 2
);

INSERT INTO ESPORTE(
    SIGLA_ESPORTE, NOME, QUANT_TIME_POR_JOGO
)VALUES(
    '222', UPPER(TRIM('voleibol')), 2
);

INSERT INTO ESPORTE(
    SIGLA_ESPORTE, NOME, QUANT_TIME_POR_JOGO
)VALUES(
    '333', UPPER(TRIM('atletismo')), 8
);

----------------------- Inserções de treinador ---------------------
INSERT INTO TREINADOR(
    CPF, CREF, NOME, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '445.555.111-77', '449354', UPPER(TRIM('Philliph Rigolão')), TO_DATE('17/08/1964', 'DD/MM/YYYY'), UPPER(TRIM('rua ibatexas do norte')), 123, UPPER(TRIM('Longe do sul')), '55555-678', UPPER(TRIM(' Am'))
);

INSERT INTO TREINADOR(
    CPF, CREF, NOME, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '234.565.211-17', '917382', UPPER(TRIM('Arthur Leme')), TO_DATE('17/10/1988', 'DD/MM/YYYY'), UPPER(TRIM('rua juazeiro jo norte')), 12, UPPER(TRIM('PACAEMBI')), '84213-121', UPPER(TRIM(' MG'))
);

INSERT INTO TREINADOR(
    CPF, CREF, NOME, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '222.635.213-17', '117382', UPPER(TRIM('RODRIGO FARO Leme')), TO_DATE('17/05/1966', 'DD/MM/YYYY'), UPPER(TRIM('rua ENTRADA FORA')), 12, UPPER(TRIM('Longe do NORTE')), '84213-121', UPPER(TRIM(' PA'))
);

INSERT INTO TREINADOR(
    CPF, CREF, NOME, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '121.312.111-32', '132798', UPPER(TRIM('DONIZETE FATO')), TO_DATE('01/05/1968', 'DD/MM/YYYY'), UPPER(TRIM('rua AMBIGUO VASCONCELOS')), 12, UPPER(TRIM('ASA DA ENTRADA')), '84213-121', UPPER(TRIM(' BA'))
);

----------------------- Inserções de time ---------------------
INSERT INTO TIME(
    SIGLA_TIME, SIGLA_ESPORTE, NOME, CPF_TREINADOR
)VALUES(
    '999', '111', UPPER(TRIM('FUTEBOL MASCULINO BRASIL')), '445.555.111-77'
);

INSERT INTO TIME(
    SIGLA_TIME, SIGLA_ESPORTE, NOME, CPF_TREINADOR
)VALUES(
    '997', '111', UPPER(TRIM('FUTEBOL MASCULINO ITALIA')), '121.312.111-32'
);

INSERT INTO TIME(
    SIGLA_TIME, SIGLA_ESPORTE, NOME, CPF_TREINADOR
)VALUES(
    '988', '112', UPPER(TRIM('FUTEBOL FEMININO ITALIA')), '222.635.213-17'
);

INSERT INTO TIME(
    SIGLA_TIME, SIGLA_ESPORTE, NOME, CPF_TREINADOR
)VALUES(
    '989', '112', UPPER(TRIM('FUTEBOL FEMININO BRASIL')), '234.565.211-17'
);

----------------------- Inserções de atleta ---------------------
INSERT INTO ATLETA(
    CPF, ID_ATLETA, NOME, ATL_SIGLA_TIME, ATL_SIGLA_ESPORTE, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '454.888.123-09', '25555', UPPER(TRIM('Guilherme Adame Guimarães')), '999', '111', TO_DATE('08/08/2000', 'DD-MM-YYYY'), UPPER(TRIM('rua algusta ferreira batista')), 10, UPPER(TRIM('aracy 2')), '12478-992', UPPER(TRIM('mg'))
);

INSERT INTO ATLETA(
    CPF, ID_ATLETA, NOME, ATL_SIGLA_TIME, ATL_SIGLA_ESPORTE, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '575.147.963-25', '12347', UPPER(TRIM('jOÃO GUILHERME')), '989', '112', TO_DATE('12/12/2001', 'DD-MM-YYYY'), UPPER(TRIM('rua ADOLFO CATANU=I')), 11, UPPER(TRIM('LUTFALA')), '12458-938', UPPER(TRIM('AL'))
);

----------------------- Inserções de Partida ---------------------

-- INSERT INTO PARTIDA (
--     DATA,LOCAL,NOME,PAR_ESPORTE
-- ) VALUES (
--     TO_DATE('10/10/2024','DD-MM-YYYY') ,UPPER(TRIM('PRAÇA DA LIBERDADE ') ) ,UPPER(TRIM('AMISTOSO: BRASIL X alemanha') ) ,UPPER(TRIM('111') )
-- );

INSERT INTO PARTIDA(
    DATA, LOCAL, NOME, SIGLA_ESPORTE
)VALUES(
    TO_DATE('11/10/2024 14:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('FUTEBOL MASCULINO BRASIL X ITALIA')), UPPER(TRIM('111'))
);

INSERT INTO PARTIDA(
    DATA, LOCAL, NOME, SIGLA_ESPORTE
)VALUES(
    TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('FUTEBOL FEMININO BRASIL X ITALIA')), UPPER(TRIM('222'))
);

----------------------- Inserções de ATLETA ---------------------

INSERT INTO ATLETA(
    CPF, ID_ATLETA, NOME, ATL_SIGLA_TIME, ATL_SIGLA_ESPORTE, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '114.118.113-19', '11112', UPPER(TRIM('RODRIGO ALVAREZ GONZALES')), '999', '111', TO_DATE('11/11/2001', 'DD-MM-YYYY'), UPPER(TRIM('rua LUIZ VELTRONI')), 10, UPPER(TRIM('EMBARE')), '11128-333', UPPER(TRIM('SP'))
);

INSERT INTO ATLETA(
    CPF, ID_ATLETA, NOME, ATL_SIGLA_TIME, ATL_SIGLA_ESPORTE, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '222.228.133-09', '11155', UPPER(TRIM('JULIA FERNANDES')), '999', '111', TO_DATE('22/02/2002', 'DD-MM-YYYY'), UPPER(TRIM('rua coqueiros dos laranjais')), 11, UPPER(TRIM('COQUEIROS')), '12478-992', UPPER(TRIM('PA'))
);

INSERT INTO ATLETA(
    CPF, ID_ATLETA, NOME, ATL_SIGLA_TIME, ATL_SIGLA_ESPORTE, DATA, RUA, NUMERO, BAIRRO, CEP, UF
)VALUES(
    '113.133.333-22', '12125', UPPER(TRIM('PEdro alvarez albuquerque')), '989', '112', NULL, NULL, NULL, NULL, NULL, NULL
);

----------------------- Criação de ESTATISTICA DE PARTIDA ---------------------
INSERT INTO ESTAT_PARTIDA(
    EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('GOLS')), UPPER(TRIM(' 111')) /* ERRADO DE PROPÓSITO PARA INCENTIVAR O USO DO UPDATE*/
);

-- EXEMPLO DE UPDATE
UPDATE ESTAT_PARTIDA ES
SET
    ES.VALOR = '3'
WHERE
    ES.VALOR = '111';

INSERT INTO ESTAT_PARTIDA(
    EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('PENALTS')), UPPER(TRIM('2'))
);

INSERT INTO ESTAT_PARTIDA(
    EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('FALTAS')), UPPER(TRIM('8'))
);

INSERT INTO ESTAT_PARTIDA(
    EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('TEMPO_EXTRA')), UPPER(TRIM('9'))
);

----------------------- Inserções de DISPUTA ---------------------
INSERT INTO DISPUTA(
    SIGLA_TIME, SIGLA_ESPORTE, EST_DATA, EST_LOCAL
)VALUES(
    '999', '111', TO_DATE('11/10/2024 14:30:00', 'DD/MM/YYYY HH24:MI:SS'), 'PRAÇA DA LIBERDADE'
);

INSERT INTO DISPUTA(
    SIGLA_TIME, SIGLA_ESPORTE, EST_DATA, EST_LOCAL
)VALUES(
    '997', '111', TO_DATE('11/10/2024 14:30:00', 'DD/MM/YYYY HH24:MI:SS'), 'PRAÇA DA LIBERDADE'
);

INSERT INTO DISPUTA(
    SIGLA_TIME, SIGLA_ESPORTE, EST_DATA, EST_LOCAL
)VALUES(
    '989', '112', TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), 'PRAÇA DA LIBERDADE'
);

INSERT INTO DISPUTA(
    SIGLA_TIME, SIGLA_ESPORTE, EST_DATA, EST_LOCAL
)VALUES(
    '988', '112', TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), 'PRAÇA DA LIBERDADE'
);

----------------------- Inserções de ESTATÍSTICA DE ATLETA EM PARTIDA ---------------------

-- ATLETA 1
INSERT INTO ESTAT_ATLETA_PARTIDA(
    ATLETA, EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    '454.888.123-09', TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('GOLS')), UPPER(TRIM(' 111')) /* ERRADO DE PROPÓSITO PARA INCENTIVAR O USO DO UPDATE*/
);

-- UPDATE PARA CORRIGIR A INSERÇÃO INCORRETA DE GOLS=111 PARA GOLS=0
UPDATE ESTAT_ATLETA_PARTIDA
SET
    VALOR = 0
WHERE
    CRITERIO = 'GOLS'
    AND VALOR = 111
    AND ATLETA = '454.888.123-09';

INSERT INTO ESTAT_ATLETA_PARTIDA(
    ATLETA, EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    '454.888.123-09', TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('FALTAS')), UPPER(TRIM(' 2'))
);

INSERT INTO ESTAT_ATLETA_PARTIDA(
    ATLETA, EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    '454.888.123-09', TO_DATE('12/10/2024 10:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('KM')), UPPER(TRIM(' 13'))
);

-- ATLETA 2
INSERT INTO ESTAT_ATLETA_PARTIDA(
    ATLETA, EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    '575.147.963-25', TO_DATE('11/10/2024 14:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('KM')), UPPER(TRIM(' 12'))
);

INSERT INTO ESTAT_ATLETA_PARTIDA(
    ATLETA, EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    '575.147.963-25', TO_DATE('11/10/2024 14:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('FALTAS')), UPPER(TRIM(' 0'))
);

INSERT INTO ESTAT_ATLETA_PARTIDA(
    ATLETA, EST_DATA, EST_LOCAL, CRITERIO, VALOR
)VALUES(
    '575.147.963-25', TO_DATE('11/10/2024 14:30:00', 'DD/MM/YYYY HH24:MI:SS'), UPPER(TRIM('PRAÇA DA LIBERDADE ')), UPPER(TRIM('GOLS')), UPPER(TRIM(' 0'))
);
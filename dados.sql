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

DELETE FROM MEDICO WHERE CRM = 123456

-- inserts com UPPER(TRIM()) EM TODOS OS NOMES
SELECT * -- ESTA OK
FROM MEDICO 

SELECT A.CPF,T.NOME
    FROM ATLETA A
    JOIN TIME T
    ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
SELECT
    A.CPF,T.NOME
FROM
    ATLETA A
    JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME;

SELECT
    *
FROM
    ATLETA A
    JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
ORDER BY
    A.NOME;

SELECT
    COUNT (*)
FROM
    ATLETA A
    LEFT JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
ORDER BY
    A.NOME;

SELECT
    *
FROM
    ESTAT_PARTIDA;

SELECT
    E.EST_LOCAL,MIN (E.VALOR) ,SUM (E.VALOR) -- E.CRITERIO,E.VALOR --,MIN(ATL_SIGLA_ESPORTE) , count(*)
FROM
    ESTAT_PARTIDA E
GROUP BY
    E.EST_LOCAL
HAVING
    SUM (E.VALOR) >10;

SELECT
    *
FROM
    ATLETA
ORDER BY
    DATA;

SELECT
    *
FROM
    ATLETA A
WHERE
    A.DATA > (
        SELECT
            MIN (DATA)
        FROM
            ATLETA
    )
ORDER BY
    A.DATA;

SELECT
    *
FROM
    TREINADOR;

SELECT
    *
FROM
    TIME;

SELECT
    *
FROM
    PARTIDA;

SELECT
    *
FROM
    DISPUTA;

DELETE 
FROM PARTIDA P
WHERE P.LOCAL ='PRAÇA DA LIBERDADE';

DELETE FROM PARTIDA P WHERE P."LOCAL"='PRAÇA DA LIBERDADE'
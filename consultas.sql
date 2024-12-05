SELECT A.CPF, T.NOME
FROM ATLETA A
    JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME;

SELECT *
FROM ATLETA A
    JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
ORDER BY A.NOME;

SELECT COUNT ( * )
FROM ATLETA A
    LEFT JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
ORDER BY A.NOME;

SELECT *
FROM ESTAT_PARTIDA;

SELECT E.EST_LOCAL, MIN (E.VALOR) , SUM (E.VALOR) -- E.CRITERIO,E.VALOR --,MIN(ATL_SIGLA_ESPORTE) , count(*)
FROM ESTAT_PARTIDA E
GROUP BY E.EST_LOCAL
HAVING SUM (E.VALOR) > 10;

SELECT *
FROM ATLETA
ORDER BY DATA;

SELECT *
FROM ATLETA A
WHERE A.DATA > (
        SELECT MIN (DATA)
        FROM ATLETA
    )
ORDER BY A.DATA;

SELECT *
FROM TREINADOR;

SELECT *
FROM TIME;

SELECT *
FROM PARTIDA;

SELECT *
FROM DISPUTA;

SELECT T.SIGLA_ESPORTE, T.NOME, A.NOME, A.CPF, TO_CHAR (P."DATA", 'DD/MM/YYYY HH24:MI:SS') AS DATA, P."LOCAL"
FROM DISPUTA D
    JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
    AND T.SIGLA_ESPORTE = D.SIGLA_ESPORTE
    JOIN PARTIDA P ON D.EST_DATA = P.DATA
    AND D.EST_LOCAL = P.LOCAL
    JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
ORDER BY T.NOME, A.NOME;

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 1  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --


/*  Todos os nomes das partidas com seu ano de acontecimento e dos respectivos nomes dos
    atletas brasileiros do esporte futebol (masculino ou feminino) que jogaram em na praça da
    liberdade entre os meses julho e novembro do ano da ediçao da olimpíada. 
    Caso exista, apresente os dados do atleta. */


SELECT P.NOME AS PARTIDA, EXTRACT (MONTH FROM P.DATA) AS MÊS, A.NOME AS ATLETA, A.DATA AS ANIVERSARIO_ATLETA, A.RUA, A.NUMERO, A.BAIRRO, A.CEP, A.UF
FROM PARTIDA P
    JOIN DISPUTA D ON P.DATA = D.EST_DATA
    AND P.LOCAL = D.EST_LOCAL
    JOIN TIME T ON D.SIGLA_ESPORTE = T.SIGLA_ESPORTE
    AND T.SIGLA_TIME = D.SIGLA_TIME
    RIGHT JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
WHERE (P.SIGLA_ESPORTE = '111'
    OR P.SIGLA_ESPORTE = '222')
    AND (P.LOCAL = 'PRAÇA DA LIBERDADE')
    AND (EXTRACT (MONTH FROM P.DATA) BETWEEN 6
    AND 11);

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 2  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Atletas do futebol masculino que possuem vídeos em TODAS as suas partidas, 
    e se tiver seu genoma cadastrado, imprimir ele também */

/*
atleta - video 

atleta - time - disputa - partida 

--
(cpf, mac_address,data_hora_video,partida_hora, partica_local)
agrupar por cpf
(cpf,sigla_time,esporte,partida_hora, partica_local)
agrupar por cpf

--

(cpf, partida_hora, partica_local)
/
(partida_hora, partica_local)

*/
 (
    SELECT A.CPF, V.PARTIDA_DATA, V.PARTIDA_LOCAL
    FROM ATLETA A
        JOIN VIDEO V ON A.CPF = V.ATLETA
);

-- GROUP BY A.CPF,V.PARTIDA_DATA,V.PARTIDA_LOCAL;


 (
    SELECT A.CPF, D.EST_DATA, D.EST_LOCAL
    FROM ATLETA A
        JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
        JOIN DISPUTA D ON D.SIGLA_TIME = T.SIGLA_TIME
        AND D.SIGLA_ESPORTE = T.SIGLA_ESPORTE
 -- JOIN PARTIDA P ON P.DATA=D.EST_DATA AND P.LOCAL= D.EST_LOCAL                      -- NÃO PRECISA
);

SELECT A.CPF, V.PARTIDA_DATA, V.PARTIDA_LOCAL
FROM ATLETA A
    JOIN VIDEO V ON A.CPF = V.ATLETA
GROUP BY A.CPF, V.PARTIDA_DATA, V.PARTIDA_LOCAL
HAVING COUNT (A.CPF) = ( -- Verifica se todos os CPFs estão presentes na combinação de partida
        SELECT COUNT (DISTINCT A.CPF)
        FROM ATLETA A
            JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
            JOIN DISPUTA D ON D.SIGLA_TIME = T.SIGLA_TIME
            AND D.SIGLA_ESPORTE = T.SIGLA_ESPORTE
        WHERE D.EST_DATA = V.PARTIDA_DATA
            AND D.EST_LOCAL = V.PARTIDA_LOCAL
    );

(
    SELECT A.CPF, V.PARTIDA_DATA, V.PARTIDA_LOCAL
    FROM ATLETA A
        JOIN VIDEO V ON A.CPF = V.ATLETA
    GROUP BY
);

-- GROUP BY A.CPF,V.PARTIDA_DATA,V.PARTIDA_LOCAL;


 (
    SELECT A.CPF, D.EST_DATA, D.EST_LOCAL
    FROM ATLETA A
        JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
        JOIN DISPUTA D ON D.SIGLA_TIME = T.SIGLA_TIME
        AND D.SIGLA_ESPORTE = T.SIGLA_ESPORTE
 -- JOIN PARTIDA P ON P.DATA=D.EST_DATA AND P.LOCAL= D.EST_LOCAL                      -- NÃO PRECISA
);

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 3  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Apresente os exames que tenham nivel de oxigenio maior que 79 e temperatura entre 36 e 37 graus existem no banco de dados. 
    Caso seja um exame especializado em cardiologia, apresentar o link para a ultrassom. Apresente todos os dados do exame, assim 
    como o nome do médico que operou o exame, o nome do atleta o qual está nessas condições e a data de execução do teste e o link caso seja cardiológico*/

SELECT E.PROTOCOLO, E.DATA_HORA, M.NOME AS MÉDICO, A.NOME AS ATLETA, E.NIVEL_OXIGENIO, E.PRESSAO_ATLETA, E.TEMPERATURA_ATLETA, C.ULTRASSOM
FROM EXAME E
    JOIN MEDICO M ON E.MEDICO = M.CPF
    JOIN ATLETA A ON E.ATLETA = A.CPF
    LEFT JOIN CARDIOLOGICO C ON C.EXAME = E.PROTOCOLO
WHERE E.NIVEL_OXIGENIO > 79
    AND TO_NUMBER (E.TEMPERATURA_ATLETA) BETWEEN 36 AND 37
ORDER BY E.TIPO;

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 4  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Qual time da Base de Dados que contém a maior quantidade de jogadores menores 
    de 30 anos tendo ao menos 2 dos jogadores com essa faixa etaria? 
    */
SELECT T.NOME AS MODALIDADE, T.SIGLA_TIME, COUNT ( * ) AS QUANT_PESSOAS_MAIORDE30
FROM TIME T
    JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
    AND A.ATL_SIGLA_ESPORTE = T.SIGLA_ESPORTE
WHERE TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) > 30
GROUP BY T.NOME, T.SIGLA_TIME;

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 5  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Selecione a sigla e o nome do time que jogou pelo menos 2 partidas que houveram 
    menos do que 2 gols por partida. A seleção deve tanto mostrar a sigla e o nome do time em questão
    como apresentar a quantidade de partidas em que houve essa ocasião */

SELECT T.SIGLA_TIME, T.NOME, COUNT ( * ) AS PARTIDAS
FROM ESTAT_PARTIDA E
    JOIN PARTIDA P ON P.DATA = E.EST_DATA
    AND P.LOCAL = E.EST_LOCAL
    JOIN DISPUTA D ON P.DATA = D.EST_DATA
    AND P.LOCAL = D.EST_LOCAL
    RIGHT JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
    AND T.SIGLA_ESPORTE = D.SIGLA_ESPORTE
WHERE P.SIGLA_ESPORTE = '222'
    AND E.CRITERIO = 'GOLS'
    AND E.VALOR > 1
GROUP BY T.SIGLA_TIME, T.NOME
HAVING COUNT (E.VALOR) > 2;

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 6  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Selecione as partidas com maior saldo de gols por esporte em que tenha acontecido 
    ou na Praça da Liberdade ou na Coronel Cervantes. OBS: saldos de menos de 3 gols não devem ser selecionados 
    Apresentar o  nome do esporte, nome da partida, data e hora, local e saldo de	gols e nome do esporte*/

SELECT P.SIGLA_ESPORTE, ES.NOME AS ESPORTE, P.NOME AS NOME_PARTIDA, MAX (E.VALOR) AS MAX_VALOR
FROM PARTIDA P
    JOIN ESTAT_PARTIDA E ON P.DATA = E.EST_DATA
    AND P.LOCAL = E.EST_LOCAL
    JOIN ESPORTE ES ON ES.SIGLA_ESPORTE = P.SIGLA_ESPORTE
WHERE E.CRITERIO = 'GOLS'
    AND (P.LOCAL = 'PRAÇA DA LIBERDADE'
    OR P.LOCAL = 'CORONEL CERVANTES')
GROUP BY P.SIGLA_ESPORTE, ES.NOME, P.NOME
HAVING MAX (E.VALOR) >= 4;

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 7  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Apresente todos os cpf, os nomes, os times, os esportes e, caso haja, todos os dados pessoais do atleta mais velho de 
    cada partida que tenha acontecido na competição anual da Olimpíada */
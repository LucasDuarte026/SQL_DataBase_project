/*
    Objetivo: Este arquivo contém uma série de consultas SQL para recuperar dados relacionados ao
    esporte, atletas, partidas e exames. As consultas são baseadas em um sistema esportivo que
    inclui informações como partidas de futebol, vídeos de atletas, exames médicos e estatísticas de jogos.

    Última Modificação: 07-12-2024
    Autor: Lucas Sales Duarte
    Licença de Uso: MIT
    Direitos autorais reservados ao autor.
    
    Descrição das Consultas:
    1. Consulta 1: Exibe informações sobre partidas de futebol na Praça da Liberdade entre julho e novembro de um ano olímpico.
    2. Consulta 2: Mostra os atletas de futebol masculino com vídeos em todas as partidas.
    3. Consulta 3: Exibe exames com níveis de oxigênio acima de 79 e temperaturas entre 36 e 37 graus, com links para exames cardiológicos.
    4. Consulta 4: Exibe o time da base de dados com mais jogadores menores de 30 anos.
    5. Consulta 5: Exibe times com pelo menos 2 partidas com menos de 2 gols por jogo.
    6. Consulta 6: Exibe partidas com o maior saldo de gols em esportes que ocorreram na Praça da Liberdade ou Coronel Cervantes.
    7. Consulta 7: Exibe informações detalhadas sobre o atleta mais velho de cada partida olímpica.
*/

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 1  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --


/*  Apresente todos os nomes das partidas com seu ano de acontecimento e dos respectivos nomes dos
    atletas brasileiros do esporte futebol (masculino ou feminino) que jogaram na Praça da
    Liberdade entre os meses Julho e Novembro do ano da ediçao da olimpíada. 
    Caso exista, apresente o genoma (LINK) do atleta. */


SELECT P.NOME AS PARTIDA, EXTRACT (MONTH FROM P.DATA) AS MÊS, A.NOME AS ATLETA, A.DATA AS ANIVERSARIO_ATLETA, A.RUA, A.NUMERO, A.BAIRRO, A.CEP, A.UF, G.GENOMA
FROM PARTIDA P
    JOIN DISPUTA D ON P.DATA = D.EST_DATA
    AND P.LOCAL = D.EST_LOCAL
    JOIN TIME T ON D.SIGLA_ESPORTE = T.SIGLA_ESPORTE
    AND T.SIGLA_TIME = D.SIGLA_TIME
    JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
    LEFT JOIN GENOMA G ON G.ATLETA = A.CPF
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
SELECT A.NOME AS ATLETA, A.CPF AS CPF_ATLETA, G.GENOMA AS LINK_GENOMA
FROM ATLETA A
    LEFT JOIN GENOMA G ON A.CPF = G.ATLETA
WHERE A.ATL_SIGLA_ESPORTE = '111' -- Código do futebol masculino
    AND NOT EXISTS (
        SELECT 1
        FROM DISPUTA D
        WHERE D.SIGLA_TIME = A.ATL_SIGLA_TIME
            AND D.SIGLA_ESPORTE = A.ATL_SIGLA_ESPORTE
            AND NOT EXISTS (
                SELECT 1
                FROM VIDEO V
                WHERE V.ATLETA = A.CPF
                    AND V.PARTIDA_DATA = D.EST_DATA
                    AND V.PARTIDA_LOCAL = D.EST_LOCAL
            )
    );

SELECT *
FROM VIDEO;

SELECT *
FROM ATLETA;

SELECT *
FROM DISPUTA D
    JOIN PARTIDA P ON D.EST_DATA = P.DATA
    AND D.EST_LOCAL = P.LOCAL;

SELECT P.NOME AS PARTIDA, A.NOME AS ATLETA, TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) AS IDADE, A.CPF, A.DATA AS DATA_NASCIMENTO, A.RUA, A.NUMERO, A.BAIRRO, A.CEP, A.UF
FROM PARTIDA P
    JOIN DISPUTA D ON P.DATA = D.EST_DATA
    AND P.LOCAL = D.EST_LOCAL
    JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
    JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
WHERE (P.DATA, P.LOCAL, TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) ) IN (
        SELECT P.DATA, P.LOCAL, MAX (TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) ) AS IDADE_MAX
        FROM PARTIDA P
            JOIN DISPUTA D ON P.DATA = D.EST_DATA
            AND P.LOCAL = D.EST_LOCAL
            JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
            JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
        GROUP BY P.DATA, P.LOCAL
    ) MINUS
    SELECT P.DATA, P.LOCAL, TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) AS IDADE
    FROM PARTIDA P
        JOIN DISPUTA D ON P.DATA = D.EST_DATA
        AND P.LOCAL = D.EST_LOCAL
        JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
        JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
    WHERE TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) < (
            SELECT MAX (TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) )
            FROM PARTIDA P
                JOIN DISPUTA D ON P.DATA = D.EST_DATA
                AND P.LOCAL = D.EST_LOCAL
                JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
                JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
            WHERE P.DATA = P.DATA
                AND P.LOCAL = P.LOCAL
        );

-- GROUP BY A.CPF,V.PARTIDA_DATA,V.PARTIDA_LOCAL;
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
    de 30 anos tendo ao menos 2 dos jogadores com essa faixa etaria? */

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


SELECT P.NOME, A.NOME, A.DATA, TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12)
FROM PARTIDA P
    JOIN DISPUTA D ON P.DATA = D.EST_DATA
    AND P.LOCAL = D.EST_LOCAL
    JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
    JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
GROUP BY P.NOME, A.NOME, A.DATA
HAVING TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) > 30;

SELECT T.ESTADO, T.NOME, T.SALDO_GOLS
FROM TIME T
WHERE (T.ESTADO, T.SALDO_GOLS) IN (
        SELECT P.DATA, P.LOCAL
        FROM PARTIDA P
            JOIN DISPUTA D ON P.DATA = D.EST_DATA
            AND P.LOCAL = D.EST_LOCAL
            JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
            JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
        WHERE TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) > 30
    );

SELECT P.NOME, A.NOME, MAX (TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) ) AS IDADE
FROM PARTIDA P
    JOIN DISPUTA D ON P.DATA = D.EST_DATA
    AND P.LOCAL = D.EST_LOCAL
    JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
    JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
WHERE TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) > 26
GROUP BY P.NOME, A.NOME;

SELECT T.ESTADO, T.NOME, T.SALDO_GOLS
FROM TIME T
WHERE (T.ESTADO, T.SALDO_GOLS) IN (
        SELECT T1.ESTADO, MIN (T1.SALDO_GOLS)
        FROM TIME T1
        GROUP BY T1.ESTADO
    );

SELECT A.NOME, G.GENOMA, V.DADO_VIDEO
FROM ATLETA A
    JOIN ESPORTE E ON A.ATL_SIGLA_ESPORTE = E.SIGLA_ESPORTE
    JOIN VIDEO V ON A.CPF = V.ATLETA
    LEFT JOIN GENOMA G ON A.CPF = G.ATLETA
WHERE E.NOME = :ESPORTE_NOME
    AND V.DADO_VIDEO IS NOT NULL
    AND NOT EXISTS (
        SELECT D.EST_DATA, D.EST_LOCAL
        FROM DISPUTA D
            JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
            AND T.SIGLA_ESPORTE = D.SIGLA_ESPORTE
        WHERE T.SIGLA_TIME = A.ATL_SIGLA_TIME MINUS
            SELECT D.EST_DATA, D.EST_LOCAL
            FROM DISPUTA D
                JOIN VIDEO V2 ON D.EST_DATA = V2.PARTIDA_DATA
                AND D.EST_LOCAL = V2.PARTIDA_LOCAL
                JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
                AND T.SIGLA_ESPORTE = D.SIGLA_ESPORTE
            WHERE T.SIGLA_TIME = A.ATL_SIGLA_TIME
    );

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 8  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*
    Selecionar todos as partidas estatisticas_partida de de todas as partidas das quais tenham mais 3 de videos
    Selecionar todos os atletas cuja somatória de gols na partidas seja maior que 3 e este atleta tenha pelo menos 3 videos nesta partida.
*/

SELECT E.EST_DATA, E.EST_LOCAL
FROM PARTIDA P
    JOIN ESTAT_PARTIDA E ON E.EST_DATA = P.DATA
    AND E.EST_LOCAL = P.LOCAL
GROUP BY E.EST_DATA, E.EST_LOCAL
HAVING COUNT ( * ) = (
        SELECT COUNT ( * )
        FROM PARTIDA P
            JOIN VIDEO V ON V.PARTIDA_DATA = P.DATA
            AND V.PARTIDA_LOCAL = P.LOCAL
    );

SELECT COUNT ( * )
FROM PARTIDA P
    JOIN VIDEO V ON V.PARTIDA_DATA = P.DATA
    AND V.PARTIDA_LOCAL = P.LOCAL;

SELECT E.EST_DATA, E.EST_LOCAL, E.CRITERIO, E.VALOR
FROM ESTAT_PARTIDA E;

SELECT V.MAC_ADDRESS, V.PARTIDA_DATA, V.PARTIDA_LOCAL
FROM VIDEO V;

SELECT E.EST_DATA, E.EST_LOCAL, E.CRITERIO, E.VALOR
FROM ESTAT_PARTIDA E
WHERE (E.EST_DATA, E.EST_LOCAL) IN (
        SELECT V.PARTIDA_DATA, V.PARTIDA_LOCAL
        FROM VIDEO V
        GROUP BY V.PARTIDA_DATA, V.PARTIDA_LOCAL
        HAVING COUNT ( * ) > 2
    )
GROUP BY E.EST_DATA, E.EST_LOCAL, E.CRITERIO, E.VALOR
 -- HAVING COUNT ( * ) = (
    --         SELECT COUNT ( * )
    --         FROM VIDEO V
    --         WHERE V.PARTIDA_DATA = E.EST_DATA
    --             AND V.PARTIDA_LOCAL = E.EST_LOCAL
    --     )
;

SELECT COUNT ( * )
FROM VIDEO V
WHERE V.PARTIDA_DATA = E.EST_DATA
    AND V.PARTIDA_LOCAL = E.EST_LOCAL;

SELECT A.NOME
FROM ATLETA A
    JOIN ESTAT_ATLETA_PARTIDA E ON A.CPF = E.ATLETA
WHERE (E.EST_DATA, E.EST_LOCAL) IN (
        SELECT V.PARTIDA_DATA, V.PARTIDA_LOCAL
        FROM VIDEO V
        GROUP BY V.PARTIDA_DATA, V.PARTIDA_LOCAL
        HAVING COUNT ( * ) > 2
    )
    and 
    
GROUP BY A.NOME
HAVING SUM (E.VALOR) > 5
;

select * from ESTAT_ATLETA_PARTIDA;
select * from atleta;
select * from video;

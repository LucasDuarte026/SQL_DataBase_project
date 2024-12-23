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
    2. Consulta 2: Filtra os atletas cuja o saldo de gols tenha sido maior que 3 em partidas que tenha no mínimo 3 vídeos.
    3. Consulta 3: Exibe exames com níveis de oxigênio acima de 79 e temperaturas entre 36 e 37 graus, com links para exames cardiológicos.
    4. Consulta 4: Exibe o time da base de dados com mais jogadores menores de 30 anos.
    5. Consulta 5: Exibe times com pelo menos 2 partidas com menos de 2 gols por jogo.
    6. Consulta 6: Exibe partidas com o maior saldo de gols em esportes que ocorreram na Praça da Liberdade ou Coronel Cervantes.
*/

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 1  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --


/*  Apresente todos os nomes das partidas com seu mês de ocorrêcia e dos respectivos nomes dos
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
WHERE P.SIGLA_ESPORTE = '111'
    AND (P.LOCAL = 'PRAÇA DA LIBERDADE')
    AND (EXTRACT (MONTH FROM P.DATA) BETWEEN 6
    AND 11);

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 2  -- -- -- -- --       CONSULTA COM DIVISÃO
-- -- -- -- ---- -- -- -- ---- -- -- -- --


/*  Selecionar todos os atletas cuja somatória de gols na partidas seja maior
    que 3 e este atleta tenha pelo menos 3 videos nesta partida.
    Apresente o seu nome, CPF, o time em que joga, sua idade e seu endereço    */

SELECT A.NOME AS ATLETA, A.CPF, T.NOME AS TIME, TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) AS IDADE, A.RUA, A.BAIRRO, A.NUMERO, A.CEP, A.UF
FROM ATLETA A
    JOIN TIME T ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
    JOIN ESTAT_ATLETA_PARTIDA E ON A.CPF = E.ATLETA
WHERE (E.EST_DATA, E.EST_LOCAL) IN (
        SELECT V.PARTIDA_DATA, V.PARTIDA_LOCAL
        FROM VIDEO V
        GROUP BY V.PARTIDA_DATA, V.PARTIDA_LOCAL
        HAVING COUNT ( * ) > 2
    )
GROUP BY A.NOME, A.CPF, T.NOME, TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) , A.RUA, A.BAIRRO, A.NUMERO, A.CEP, A.UF
HAVING SUM (E.VALOR) > 3
ORDER BY A.NOME;

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 3  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Apresente os exames que tenham nivel de oxigenio maior que 79 e temperatura entre 36 e 37 graus do banco de dados. 
    Caso seja um exame especializado em cardiologia, apresentar o link para a ultrassom. Apresente todos os dados do exame, assim 
    como o nome do médico que operou o exame, o nome do atleta o qual está nessas condições, a data de execução do teste e o link caso seja cardiológico*/
SELECT E.PROTOCOLO, E.DATA_HORA, M.NOME AS MÉDICO, A.NOME AS ATLETA, E.NIVEL_OXIGENIO, E.PRESSAO_ATLETA, E.TEMPERATURA_ATLETA, C.ULTRASSOM
FROM EXAME E
    JOIN MEDICO M ON E.MEDICO = M.CPF
    JOIN ATLETA A ON E.ATLETA = A.CPF
    LEFT JOIN CARDIOLOGICO C ON C.EXAME = E.PROTOCOLO
WHERE E.NIVEL_OXIGENIO > 79
    AND TO_NUMBER (E.TEMPERATURA_ATLETA) BETWEEN 36 AND 37
ORDER BY A.NOME;

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 4  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Qual time da Base de Dados que contém a maior quantidade de jogadores menores 
    de 30 anos contendo ao menos 2 jogadores com essa faixa etaria? */

SELECT T.NOME AS MODALIDADE, T.SIGLA_TIME, COUNT ( * ) AS QUANT_PESSOAS_MAIORDE30
FROM TIME T
    JOIN ATLETA A ON A.ATL_SIGLA_TIME = T.SIGLA_TIME
    AND A.ATL_SIGLA_ESPORTE = T.SIGLA_ESPORTE
WHERE TRUNC (MONTHS_BETWEEN (SYSDATE, A.DATA) / 12) > 30
GROUP BY T.NOME, T.SIGLA_TIME
HAVING COUNT ( * ) > 1;

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 5  -- -- -- -- --
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Selecione a sigla e o nome dos times de futebol que jogaram ao máximo 2 partidas que houveram 
    mais do que 2 gols por partida. A seleção deve tanto mostrar a sigla e o nome 
    do time em questão como apresentar a quantidade de partidas em que houve essa ocasião */

SELECT T.SIGLA_TIME, T.NOME, COUNT ( * ) AS PARTIDAS
FROM ESTAT_PARTIDA E
    JOIN PARTIDA P ON P.DATA = E.EST_DATA
    AND P.LOCAL = E.EST_LOCAL
    JOIN DISPUTA D ON P.DATA = D.EST_DATA
    AND P.LOCAL = D.EST_LOCAL
    JOIN TIME T ON T.SIGLA_TIME = D.SIGLA_TIME
    AND T.SIGLA_ESPORTE = D.SIGLA_ESPORTE
WHERE P.SIGLA_ESPORTE = '111'
    AND E.CRITERIO = 'GOLS'
    AND E.VALOR >= 2
GROUP BY T.SIGLA_TIME, T.NOME
HAVING COUNT (E.VALOR) <= 2;

-- -- -- -- ---- -- -- -- ---- -- -- -- --
-- -- -- -- --  CONSULTA 6  -- -- -- -- -- 
-- -- -- -- ---- -- -- -- ---- -- -- -- --

/*  Selecione as partidas com maior saldo de gols por esporte em que tenha acontecido 
    ou na Praça da Liberdade ou na Coronel Cervantes. OBS: saldos de menos de 3 gols não devem ser selecionados 
    Apresentar a sigla do esporte e seu nome, nome da partida, data e hora, local e saldo de gols*/

SELECT ES.NOME, MAX (E.VALOR) AS MAXIMO_SALDO_GOL
FROM PARTIDA P
    JOIN ESTAT_PARTIDA E ON P.DATA = E.EST_DATA
    AND P.LOCAL = E.EST_LOCAL
    JOIN ESPORTE ES ON ES.SIGLA_ESPORTE = P.SIGLA_ESPORTE
WHERE E.CRITERIO = 'GOLS'
    AND (P.LOCAL = 'PRAÇA DA LIBERDADE'
    OR P.LOCAL = 'CORONEL CERVANTES')
GROUP BY ES.NOME
HAVING MAX (E.VALOR) >= 3;
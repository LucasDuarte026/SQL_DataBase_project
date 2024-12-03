import oracledb

# Configuração da conexão
username = ""
password = ""
dsn = ""

try:
    # Inicializar o cliente Oracle
    oracledb.init_oracle_client(lib_dir="C:/oracle/instant_client")

    # Tentativa de conexão ao banco
    connection = oracledb.connect(user=username, password=password, dsn=dsn)

    # Criar cursor e executar uma consulta
    cursor = connection.cursor()
    query = "SELECT * FROM TIME"  # Altere para a tabela ou consulta que deseja testar
    cursor.execute(query)

    # Iterar pelos resultados e exibi-los
    print("Resultados da consulta:")
    for row in cursor:
        print(row)

    # Fechar o cursor e a conexão
    cursor.close()
    connection.close()

except oracledb.Error as e:
    print("Erro ao conectar no Oracle Database:", e)
except Exception as e:
    print("Erro inesperado:", e)

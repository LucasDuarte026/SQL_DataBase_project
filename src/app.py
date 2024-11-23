import oracledb



# Conectando ao banco
try:
    # Modo thin (sem Oracle Client obrigatório)
    oracledb.init_oracle_client() 
    connection = oracledb.connect(user=username, password=password, dsn=dsn)

    # Cursor para executar comandos SQL
    cursor = connection.cursor()

    # Exemplo de execução de consulta
    query = "SELECT * FROM JOGADOR"
    cursor.execute(query)

    # Iterando nos resultados
    for row in cursor:
        print(row)

    # Fechar o cursor e conexão
    cursor.close()
    connection.close()

except oracledb.Error as e:
    print("Erro ao conectar no Oracle Database:", e)
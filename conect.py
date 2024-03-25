import psycopg2

# Parâmetros de conexão ao banco de dados
conexao = psycopg2.connect(
    dbname="INSS",
    user="seu_usuario",
    password="sua_senha",
    host="localhost",
    port="5432"
)

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Consulta SQL para selecionar todos os registros da tabela Beneficios
consulta = "SELECT * FROM Beneficios;"

# Executa a consulta SQL
cursor.execute(consulta)

# Obtém todos os resultados da consulta
registros = cursor.fetchall()

# Exibe os resultados
for registro in registros:
    print(registro)

# Fecha o cursor e a conexão
cursor.close()
conexao.close()

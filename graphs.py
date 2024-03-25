import psycopg2
import matplotlib.pyplot as plt

# Gráfico de Pizza (Observador)
class GraficoPizza(Observador):
    def __init__(self, conexao):
        self.conexao = conexao

    def atualizar(self):
        print("Atualizando gráfico de pizza...")
        cursor = self.conexao.cursor()
        consulta = "SELECT MunicipioResidencia, COUNT(*) AS total FROM Beneficios GROUP BY MunicipioResidencia;"
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()

        # Extrair os dados para criar o gráfico
        dados = {registro[0]: registro[1] for registro in registros}
        labels = list(dados.keys())
        valores = list(dados.values())

        # Criar o gráfico de pizza
        plt.figure(figsize=(8, 6))
        plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Distribuição de Benefícios por Município')
        plt.axis('equal')  # Mantém a forma do círculo
        plt.show()

# Gráfico de Coluna (Observador)
class GraficoColuna(Observador):
    def __init__(self, conexao):
        self.conexao = conexao

    def atualizar(self):
        print("Atualizando gráfico de coluna...")
        cursor = self.conexao.cursor()
        consulta = "SELECT MunicipioResidencia, COUNT(*) AS total FROM Beneficios GROUP BY MunicipioResidencia;"
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()

        # Extrair os dados para criar o gráfico
        municipios = [registro[0] for registro in registros]
        quantidades = [registro[1] for registro in registros]

        # Criar o gráfico de colunas
        plt.figure(figsize=(10, 6))
        plt.bar(municipios, quantidades)
        plt.xlabel('Município')
        plt.ylabel('Quantidade de Benefícios')
        plt.title('Quantidade de Benefícios por Município')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

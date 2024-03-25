# Extrai os dados para criar o gráfico
municipios = [registro[0] for registro in registros]
quantidades = [registro[1] for registro in registros]

# Cria o gráfico de barras interativo
fig = go.Figure(data=[go.Bar(x=municipios, y=quantidades)])

# Atualiza o layout para adicionar título e rótulos dos eixos
fig.update_layout(title="Número de Benefícios por Município de Residência",
                  xaxis_title="Município",
                  yaxis_title="Quantidade de Benefícios")

# Exibe o gráfico interativo
fig.show()

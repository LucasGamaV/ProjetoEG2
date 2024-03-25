if __name__ == "__main__":
    # Criando o sujeito (subject)
    sujeito = Sujeito()

    # Criando os observadores (gráficos)
    grafico_pizza = GraficoPizza()
    grafico_barra = GraficoBarra()
    grafico_coluna = GraficoColuna()

    # Registrando os observadores no sujeito
    sujeito.registrar_observador(grafico_pizza)
    sujeito.registrar_observador(grafico_barra)
    sujeito.registrar_observador(grafico_coluna)

    # Criando dados de benefícios
    dados_beneficios = DadosBeneficios()

    # Simulando uma atualização nos dados de benefícios
    novos_dados = {"Município A": 100, "Município B": 200, "Município C": 150}
    dados_beneficios.atualizar_dados(novos_dados)

    # Notificando os observadores sobre a atualização nos dados
    sujeito.notificar_observadores(dados_beneficios.dados)

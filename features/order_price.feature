Feature: Ordenação por preço
    Scenario: Ordenar produtos por preço crescente
        Given que o usuário está na página de inventário
        When ele seleciona a ordenação por preço crescente
        Then os produtos devem aparecer em ordem crescente de preço

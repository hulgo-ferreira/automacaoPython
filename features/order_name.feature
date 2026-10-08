Feature: Ordenação por nome
    Scenario: Ordenar produtos por nome (A-Z)
        Given que o usuário está na página de inventário
        When ele seleciona a ordenação por nome (A-Z)
        Then os produtos devem aparecer em ordem alfabética

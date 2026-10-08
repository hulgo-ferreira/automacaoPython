Feature: Checkout sem preencher dados
    Scenario: Tentar continuar checkout sem preencher dados
        Given que o usuário adicionou um item ao carrinho
        When ele inicia o checkout sem preencher os dados
        Then uma mensagem de erro deve ser exibida informando campos obrigatórios

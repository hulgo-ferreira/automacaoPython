Feature: Login inválido
    Scenario: Login com credenciais inválidas
        Given que o usuário acessa a página de login
        When ele tenta logar com credenciais inválidas
        Then uma mensagem de erro deve ser exibida

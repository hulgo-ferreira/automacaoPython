Feature: Usuário bloqueado
    Scenario: Login com usuário bloqueado
        Given que o usuário acessa a página de login
        When ele tenta logar com usuário bloqueado
        Then uma mensagem de usuário bloqueado deve ser exibida

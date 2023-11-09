# language: pt

Funcionalidade: Testes no Nubank

Esquema do Cenário: Peça sua conta e cartão de crédito do Nubank

    Dado que esteja na tela inicial
    Quando preencho campo de cpf com um valor inválido: "<cpf>"
    Então verificar se é disparada a mensagem "Precisamos de um CPF válido."

    Exemplos:
        | cpf         |
        | 81038695032 |
        | 81038695031 |


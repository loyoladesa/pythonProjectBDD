Feature: Operações de Calculadora
    Como um usuário
    Eu quero poder usar uma calculadora
    Para realizar operações matemáticas

    Scenario: Adição de dois números
      Given que eu tenho dois números 5 e 3
      When eu adiciono esses números
      Then o resultado deve ser 8
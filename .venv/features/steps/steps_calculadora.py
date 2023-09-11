from behave import given,when,then

@given(u'que eu tenho dois números {num1:d} e {num2:d}')
def step_dados_dois_numeros(context,num1,num2):
    context.calc.armazenarNumeros(num1,num2)


@when(u'eu adiciono esses números')
def step_adicionar_numeros(context):
    context.calc.somar()


@then(u'o resultado deve ser {resultado:d}')
def step_verificar_resultado(context,resultado):
    assert context.calc.obterValor() == resultado

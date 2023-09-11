# features/steps/steps_addition.py

from behave import given,when,then


@given(u"I have '{num1:d}' and '{num2:d}'")
def given_i_have(context,num1,num2):
    context.math.doStoreNum1Num2(num1,num2)


@when(u'I add them')
def when_i_add(context):
    context.math.doAdd()

@then(u"The result must be '{value:d}'")
def then_the_result_must_be(context,value):
    actual_value = context.math.getValue()
    assert value == actual_value,"Expected %d got %d"%(value,actual_value)









# Empty for time being
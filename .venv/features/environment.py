# environment.py

import libmath
import calculadora


def before_scenario(context,scenario):
    context.math = libmath.libMath()
    context.calc = calculadora.Calculadora()


# Empty for time being
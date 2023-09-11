# environment.py

import libmath


def before_scenario(context,scenario):
    context.math = libmath.libMath()


# Empty for time being
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def plus(self):
        return self.op1 + self.op2

    def minus(self):
        return self.op1 - self.op2


def operate(arg):

    if arg == "suma":
        result = calculator.plus()
    elif arg == "resta":
        result = calculator.minus()
    else:
        exit('Error: Only accept "suma" or "resta"')
    return (result)


if __name__ == "__main__":
    try:
        operating1 = int(sys.argv[1])
        arg = sys.argv[2]
        operating2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculator = Calculadora(operating1, operating2)
    result = operate(arg)
    print(result)

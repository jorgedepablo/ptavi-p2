#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def plus(self, op1, op2):
        return op1 + op2

    def minus(self, op1, op2):
        return op1 - op2


calculator = Calculadora()

if __name__ == "__main__":
    try:
        operating1 = int(sys.argv[1])
        operating2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculator.plus(operating1, operating2)
    elif sys.argv[2] == "resta":
        result = calculator.minus(operating1, operating2)
    else:
        sys.exit('Operación solo puede ser sumar o restar.')

print(result)

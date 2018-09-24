#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def plus(self, op1, op2):
        return op1 + op2

    def minus(self, op1, op2):
        return op1 - op2


class CalculadoraHija(Calculadora):

    def times(self, op1, op2):
        return op1 * op2

    def over(self, op1, op2):
        return op1 / op2


calculator = CalculadoraHija()

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
    elif sys.argv[2] == "multiplica":
        result = calculator.times(operating1, operating2)
    elif sys.argv[2] == "divide":
        if operating2 == 0:
            sys.exit("Division by zero is not allowed")
        else:
            result = calculator.over(operating1, operating2)

    else:
        sys.exit('Operación solo puede ser sumar,restar,multiplicar,dividir.')

    print(result)

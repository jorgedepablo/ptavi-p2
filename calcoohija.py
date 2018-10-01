#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora

class CalculadoraHija(Calculadora):

    def times(self):
        return self.op1 * self.op2

    def over(self):
        try:
            return self.op1 / self.op2
        except ZeroDivisionError:
            exit("Division by zero is not allowed")

    def operate(self, arg):
        if arg == "suma":
            result = self.plus()
        elif arg == "resta":
            result = self.minus()
        elif arg == "multiplica":
            result = self.times()
        elif arg == "divide":
            result = self.over()
        else:
            exit('Error: Only accept "suma","resta","multiplica" or "divide"')
        return (result)

if __name__ == "__main__":
    try:
        operating1 = int(sys.argv[1])
        arg = sys.argv[2]
        operating2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculator = CalculadoraHija(operating1, operating2)
    result = calculator.operate(arg)
    print (result)

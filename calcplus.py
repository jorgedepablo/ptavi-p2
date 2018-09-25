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
        file = open(sys.argv[1])
    except
        sys.exit("Error: The argument is not valid")

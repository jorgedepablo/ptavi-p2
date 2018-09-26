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
        with open(sys.argv[1], "r") as file: #r de read solo quiero leer el fichero, no modificarlo
            for linea in file.readlines():
                operaciones = linea.split(",")
                operador = operaciones[0]
                print(operador)

    except ValueError:
        sys.exit("Error: The argument is not valid")

    file.close()

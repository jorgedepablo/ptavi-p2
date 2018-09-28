#!/usr/bin/python3
# -*- coding: utf-8 -*-

# version funcional pero hay que arreglar lo de las clases heredadas
#la movida con lo de dividir por 0 meterlo en el objeto
#control de errores de ficheros
#pasar PEP8

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
        file = open(sys.argv[1], "r") #r de read solo quiero leer el fichero, no modificarlo
        for linea in file.readlines():
            linea = linea.rstrip('\n')
            operaciones = linea.split(',')
            operador = operaciones[0]
            if operador == "suma":
                result = int(operaciones[1])
                for operandos in operaciones[2:]:
                    result = calculator.plus(result, int(operandos))
            elif operador == "resta":
                result = int(operaciones[1])
                for operandos in operaciones[2:]:
                    result = calculator.minus(result, int(operandos))
            elif operador == "multiplica":
                result = int(operaciones[1])
                for operandos in operaciones[2:]:
                    result = calculator.times(result, int(operandos))
            elif operador == "divide":
                result = int(operaciones[1])
                for operandos in operaciones[2:]:
                    try:
                        result = calculator.over(result, int(operandos))
                    except ZeroDivisionError:
                        print("no dividas por 0 capullo")
            else:
                exit('Operación solo puede ser sumar,restar,multiplicar,dividir.')
            print(result)
    except ValueError:
        sys.exit("Error: The argument is not valid")

    file.close()

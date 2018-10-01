#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":
    try:
        file = open(sys.argv[1], "r")
        for line in file.readlines():
            line = line.rstrip('\n')
            operations = line.split(',')
            arg = operations[0]
            result = int(operations[1])
            for operands in operations[2:]:
                calculator = calcoohija.CalculadoraHija(result, int(operands))
                result = calculator.operate(arg)
            print (result)
    except ValueError:
        sys.exit("Error: The argument is not valid")

    file.close()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as file:
            line = csv.reader(file)
            for operations in line:
                arg = operations[0]
                result = int(operations[1])
                for operands in operations[2:]:
                    calculator = calcoohija.CalculadoraHija(result,
                                                            int(operands))
                    result = calculator.operate(arg)
                print(result)
            file.close()
    except ValueError:
        sys.exit("Error: The argument is not valid")

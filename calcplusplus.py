#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import calcoohija
import csv

if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as file:
            operaciones = csv.reader(file)
            print(operaciones)
            #operando = operaciones[1]

    except ValueError:
        sys.exit("Error: The argument is not valid")

    file.close()

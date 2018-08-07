#!/usr/bin/python
# -*- coding: utf-8 -*-

# Abre el archivo
file = open( "./files/results.csv", "r" )

# Itera cada uno de las líneas del archivo
for line in file:
    print line

# Cierra el archivo
file .close()

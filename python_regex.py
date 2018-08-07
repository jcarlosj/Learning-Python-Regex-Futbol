#!/usr/bin/python
# -*- coding: utf-8 -*-
import re                                       # Importa Líbrería Regex

# Usamos el comando r (match) para validar nuestra expresión que en Python se encierra entre ' comillas sencillas
pattern = re .compile( r'^([\d]{4,4})\-.*$' )

# Abre el archivo
file = open( "./files/results.csv", "r" )

# Itera cada uno de las líneas del archivo
for line in file:
    res = re .match( pattern, line )            # Valida el patrón (previamente compilado que hace la ejecución más rápida)
    if res:                                     # Valida si la expresión ha hecho match
        print "%s \n" % res .group( 1 )

# Cierra el archivo
file .close()

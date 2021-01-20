import re

patron = re.compile('^[A-Za-z]+(?:[ _-][A-Za-z]+)*$')
patron_numerico = re.compile('^[0-9]+$')

def validacion (evaluar):
    if patron.match(evaluar) != None:
        return True
    else:
        return False


def validacion_numerica (evaluar):
    if patron_numerico.match(evaluar) != None:
        return True
    else:
        return False
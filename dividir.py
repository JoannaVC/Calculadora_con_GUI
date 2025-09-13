def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero no permitida."
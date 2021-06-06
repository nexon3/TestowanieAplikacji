def add(x, y):
    """Dodawanie"""
    return x + y


def subtract(x, y):
    """Odejmowanie"""
    return x - y


def multiply(x, y):
    """Mnożenie"""
    return x * y


def divide(x, y):
    """Dzielenie"""
    if y == 0:
        raise ValueError('Nie mozna dzielic przez zero!')
    return x / y
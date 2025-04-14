import pytest
from app.calculator import Calculator  # Assurez-vous que le module calculator.py est dans le répertoire approprié

def test_add_failure():
    """
    Teste la méthode d'addition de la classe Calculator avec un échec prévu.
    """
    calc = Calculator()
    assert calc.add(2, 3) != 6  # Ici on échoue

def test_add_success():
    """
    Teste la méthode d'addition de la classe Calculator.
    """
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_add_success_negative():
    """
    Teste la méthode d'addition de la classe Calculator avec des nombres négatifs.
    """
    calc = Calculator()
    assert calc.add(-2, -3) == -5

def test_add_success_float():
    """
    Teste la méthode d'addition de la classe Calculator avec des nombres à virgule flottante.
    """
    calc = Calculator()
    assert calc.add(2.5, 3.5) == 6.0

def test_add_success_large_numbers():
    """
    Teste la méthode d'addition de la classe Calculator avec de grands nombres.
    """
    calc = Calculator()
    assert calc.add(1000000, 2000000) == 3000000

def test_add_success_zero():
    """
    Teste la méthode d'addition de la classe Calculator avec zéro.
    """
    calc = Calculator()
    assert calc.add(0, 0) == 0

def test_subtract_failure():
    """
    Teste la méthode de soustraction de la classe Calculator avec un échec prévu.
    """
    calc = Calculator()
    assert calc.subtract(5, 3) != 3  # Ici c'est l'echec scolaire

def test_subtract_success():
    """
    Teste la méthode de soustraction de la classe Calculator.
    """
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_subtract_success_negative():
    """
    Teste la méthode de soustraction de la classe Calculator avec des nombres négatifs.
    """
    calc = Calculator()
    assert calc.subtract(-5, -3) == -2

def test_subtract_success_float():
    """
    Teste la méthode de soustraction de la classe Calculator avec des nombres à virgule flottante.
    """
    calc = Calculator()
    assert calc.subtract(5.5, 3.5) == 2.0

def test_subtract_success_large_numbers():
    """
    Teste la méthode de soustraction de la classe Calculator avec de grands nombres.
    """
    calc = Calculator()
    assert calc.subtract(2000000, 1000000) == 1000000

def test_multiply_failure():
    """
    Teste la méthode de multiplication de la classe Calculator avec un échec prévu.
    """
    calc = Calculator()
    assert calc.multiply(2, 3) != 5  # Comment chui nul

def test_multiply_success():
    """
    Teste la méthode de multiplication de la classe Calculator.
    """
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_multiply_success_negative():
    """
    Teste la méthode de multiplication de la classe Calculator avec des nombres négatifs.
    """
    calc = Calculator()
    assert calc.multiply(-2, -3) == 6

def test_multiply_success_float():
    """
    Teste la méthode de multiplication de la classe Calculator avec des nombres à virgule flottante.
    """
    calc = Calculator()
    assert calc.multiply(2.5, 3.5) == 8.75

def test_divide_failure():
    """
    Teste la méthode de division de la classe Calculator avec un échec prévu.
    """
    calc = Calculator()
    assert calc.divide(6, 3) != 3  # https://tenor.com/bpF46.gif


def test_divide_success():
    """
    Teste la méthode de division de la classe Calculator.
    """
    calc = Calculator()
    assert calc.divide(6, 3) == 2

def test_divide_by_zero():
    """
    Teste la division par zéro dans la méthode de division de la classe Calculator.
    """
    calc = Calculator()
    try:
        calc.divide(6, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False
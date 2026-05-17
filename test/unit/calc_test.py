import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

#Agrego pruebas para la suma - Casos de error
    def test_add_method_falla_con_datos_errados(self):
        self.assertRaises(TypeError, self.calc.add, "a", 3)
        self.assertRaises(TypeError, self.calc.add, 3, "b")
        self.assertRaises(TypeError, self.calc.add, None, "6")
        self.assertRaises(TypeError, self.calc.add, "b", None)
        self.assertRaises(TypeError, self.calc.add, object(), "r")
        self.assertRaises(TypeError, self.calc.add, "23", object())

#Agrego pruebas para la resta - Casos de éxito
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(16, self.calc.substract(10, -6))
        self.assertEqual(-3, self.calc.substract(-2, 1))
        self.assertEqual(1, self.calc.substract(1, 0))

#Agrego pruebas para la resta - Casos de error
    def test_substract_method_falla_con_datos_errados(self):
        self.assertRaises(TypeError, self.calc.substract, "1", 4)
        self.assertRaises(TypeError, self.calc.substract, 3, "9")
        self.assertRaises(TypeError, self.calc.substract, "a", 3)
        self.assertRaises(TypeError, self.calc.substract, 3, "b")
        self.assertRaises(TypeError, self.calc.substract, None, "6")
        self.assertRaises(TypeError, self.calc.substract, "b", None)
        self.assertRaises(TypeError, self.calc.substract, object(), "r")
        self.assertRaises(TypeError, self.calc.substract, "23", object())

#Agrego pruebas para la multiplicación - Casos de éxito
    def test_multiply_method_returns_resultado_exitoso(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(0, self.calc.multiply(0, 0))
        self.assertEqual(0, self.calc.multiply(0, 2))

#Agrego pruebas para la multiplicación - Casos de error
    def test_multiply_method_falla_con_datos_errados(self):
        self.assertRaises(TypeError, self.calc.multiply, "1", 4)
        self.assertRaises(TypeError, self.calc.multiply, 3, "9")
        self.assertRaises(TypeError, self.calc.multiply, "a", 3)
        self.assertRaises(TypeError, self.calc.multiply, 3, "b")
        self.assertRaises(TypeError, self.calc.multiply, None, "6")
        self.assertRaises(TypeError, self.calc.multiply, "b", None)
        self.assertRaises(TypeError, self.calc.multiply, object(), "r")
        self.assertRaises(TypeError, self.calc.multiply, "23", object())

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "90", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "64")
        self.assertRaises(TypeError, self.calc.divide, "2", "32")
        self.assertRaises(TypeError, self.calc.divide, None, "56")
        self.assertRaises(TypeError, self.calc.divide, "b", None)
        self.assertRaises(TypeError, self.calc.divide, object(), "r")
        self.assertRaises(TypeError, self.calc.divide, "23", object())

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

#Agregro pruebas para la potenciación - Casos de éxito
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(3, 0))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(0, self.calc.power(0, 2))
        self.assertEqual(1, self.calc.power(0, 0)) # Por convención, cualquier número elevado a la potencia de 0 es igual a 1

#Agrego pruebas para la potenciación - Casos de error
    def test_power_method_falla_con_datos_errados(self):
        self.assertRaises(TypeError, self.calc.power, "1", 4)
        self.assertRaises(TypeError, self.calc.power, 3, "9")
        self.assertRaises(TypeError, self.calc.power, "a", 3)
        self.assertRaises(TypeError, self.calc.power, 3, "b")
        self.assertRaises(TypeError, self.calc.power, None, "6")
        self.assertRaises(TypeError, self.calc.power, "b", None)
        self.assertRaises(TypeError, self.calc.power, object(), "r")
        self.assertRaises(TypeError, self.calc.power, "23", object())

#Agregro pruebas para la raíz cuadrada - Casos de éxito
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(0, self.calc.sqrt(0))
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertEqual(1.4142135623730951, self.calc.sqrt(2))

#Agrego pruebas para la raíz cuadrada - Casos de error
    def test_sqrt_method_falla_con_datos_errados(self):
        self.assertRaises(TypeError, self.calc.sqrt, "4")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())
        self.assertRaises(TypeError, self.calc.sqrt, -1)
        self.assertRaises(TypeError, self.calc.sqrt, -0.0001)

#agrego pruebas para el logaritmo en base 10 - Casos de éxito
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(0.30102999566398114, self.calc.log10(2))

#agrego pruebas para el logaritmo en base 10 - Casos de error
    def test_log10_method_falla_con_datos_errados(self):
        self.assertRaises(TypeError, self.calc.log10, "10")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())
        self.assertRaises(ValueError, self.calc.log10, 0)
        self.assertRaises(ValueError, self.calc.log10, -1)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

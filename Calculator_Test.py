import unittest
from Calculator import *

class GeneralTests(unittest.TestCase):
    # Test sprawdzajacy tworzenie obiektu kalkulatora
    def test_check_instance(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)
    
    # Test sprawdzajacy domyslne wartosci
    def test_check_result(self):
        calc = Calculator()
        self.assertEqual(calc.get_result(), '')

    # Test sprawdzajacy domyslny system liczowy
    def test_check_numeric_system(self):
        calc = Calculator()
        self.assertEqual(calc.numeric_system, NumericSystem.DEC)

# Testy do sprawdzenia przyjmowania znakow dla roznych systemow
class InputTests(unittest.TestCase):
    def test_check_dec_input_positive(self):
        calc = Calculator()
        for character in "0123456789":
            self.assertEqual(calc.add_input(character), True)

    def test_check_dec_input_negative(self):
        calc = Calculator()
        for character in "ABCDEF":
            self.assertEqual(calc.add_input(character), False)

    def test_check_oct_input_positive(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.OCT
        for character in "01234567":
            self.assertEqual(calc.add_input(character), True)

    def test_check_oct_input_negative(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.OCT
        for character in "89ABCDEF":
            self.assertEqual(calc.add_input(character), False)

    def test_check_bin_input_positive(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.BIN
        for character in "01":
            self.assertEqual(calc.add_input(character), True)

    def test_check_bin_input_negative(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.BIN
        for character in "23456789ABCDEF":
            self.assertEqual(calc.add_input(character), False)

    def test_check_hex_input_positive(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.HEX
        for character in "0123456789ABCDEF":
            self.assertEqual(calc.add_input(character), True)

    def test_check_hex_input_negative(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.HEX
        for character in "GHJKILXQ":
            self.assertEqual(calc.add_input(character), False)

class NumericSystemTests(unittest.TestCase):
    def test_dec_to_bin(self):
        input_values = ['1', '12', '255', '1377']
        expected_values = ['0b1', '0b1100', '0b11111111', '0b10101100001']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.BIN)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.BIN)
    
    def test_dec_to_hex(self):
        input_values = ['1', '12', '255', '1377']
        expected_values = ['0x1', '0xC', '0xFF', '0x561']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.HEX)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.HEX)

    def test_dec_to_oct(self):
        input_values = ['1', '12', '255', '1377']
        expected_values = ['0o1', '0o14', '0o377', '0o2541']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.OCT)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.OCT)
    



if __name__ == '__main__':
    unittest.main()
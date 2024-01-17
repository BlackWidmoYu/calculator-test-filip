import unittest
from Calculator import *

# Generalne testy
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

    # Test sprawdzajacy domyslny data type
    def test_check_datatype(self):
        calc = Calculator()
        self.assertEqual(calc.data_type, DataType.qword)

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

# Operacje dla roznych systemow liczbowych
    def test_signs_input(self):
        calc = Calculator()
        for num_sys in {NumericSystem.BIN , NumericSystem.DEC , NumericSystem.OCT , NumericSystem.HEX}:
            calc.numericSystem = num_sys
            for i in "+-*/":
                calc.value = '0'
                calc.operation = ""

                calc.add_input(i)
                self.assertEqual(calc.last_number, '0')
                self.assertEqual(calc.operation, i)

    def test_input_between_specific_values_range(self):
        calc = Calculator()
        calc.data_type = DataType.byte
        calc.add_input('0')
        self.assertEqual(calc.last_number, '0')

    def test2_input_between_specific_values_range(self):
        calc = Calculator()
        calc.data_type = DataType.byte
        calc.add_input('00')
        self.assertEqual(calc.last_number, '0')

    def test3_input_between_specific_values_range(self):
        calc = Calculator()
        calc.data_type = DataType.byte
        calc.add_input('127')
        self.assertEqual(calc.last_number, '127')

    # def test4_input_between_specific_values_range_negative(self):
    #     calc = Calculator()
    #     calc.data_type = DataType.byte
    #     calc.numeric_system=NumericSystem.DEC
    #     self.assertEqual(calc.add_input('300'), False)     


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
    
    def test_oct_to_dec(self):
        input_values = ['0o1', '0o14', '0o377', '0o2541']
        expected_values = ['1', '12', '255', '1377']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.numeric_system = NumericSystem.OCT
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.DEC)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.DEC)

    def test_oct_to_hex(self):
        input_values = ['0o1', '0o14', '0o377', '0o2541']
        expected_values = ['0x1', '0xC', '0xFF', '0x561']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.numeric_system = NumericSystem.OCT
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.HEX)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.HEX)

    def test_oct_to_bin(self):
        input_values = ['0o1', '0o14', '0o377', '0o2541']
        expected_values = ['0b1', '0b1100', '0b11111111', '0b10101100001']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.numeric_system = NumericSystem.OCT
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.BIN)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.BIN)

    def test_bin_to_dec(self):
        input_values = ['0b1', '0b1100', '0b11111111', '0b10101100001']
        expected_values = ['1', '12', '255', '1377']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.numeric_system = NumericSystem.BIN
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.DEC)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.DEC)

    def test_bin_to_hex(self):
        input_values = ['0b1', '0b1100', '0b11111111', '0b10101100001']
        expected_values = ['0x1', '0xC', '0xFF', '0x561']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.numeric_system = NumericSystem.BIN
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.HEX)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.HEX)

    def test_bin_to_oct(self):
        input_values = ['0b1', '0b1100', '0b11111111', '0b10101100001']
        expected_values = ['0o1', '0o14', '0o377', '0o2541']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.numeric_system = NumericSystem.BIN
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.OCT)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.OCT)

    def test_hex_to_dec(self):
        input_values = ['0x1', '0xC', '0xFF', '0x561']
        expected_values = ['1', '12', '255', '1377']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.numeric_system = NumericSystem.HEX
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.DEC)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.DEC)

    def test_hex_to_oct(self):
        input_values = ['0x1', '0xC', '0xFF', '0x561']
        expected_values = ['0o1', '0o14', '0o377', '0o2541']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.numeric_system = NumericSystem.HEX
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.OCT)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.OCT)

    def test_hex_to_bin(self):
        input_values = ['0x1', '0xC', '0xFF', '0x561']
        expected_values = ['0b1', '0b1100', '0b11111111', '0b10101100001']

        for i in range(len(input_values)):
            calc = Calculator()
            calc.numeric_system = NumericSystem.HEX
            calc.last_number = input_values[i]
            calc.change_numeric_system(NumericSystem.BIN)

            self.assertEqual(calc.last_number, expected_values[i])
            self.assertEqual(calc.numeric_system, NumericSystem.BIN)

# Operacje podstawowe
class ArithmeticOperationsTests(unittest.TestCase):
    def test_addition(self):
        calc = Calculator()
        calc.add_input('1')
        calc.add_input('+')
        calc.add_input('2')
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '3')

    def test_subtraction(self):
        calc = Calculator()
        calc.add_input('5')
        calc.add_input('-')
        calc.add_input('3')
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '2')

    def test_multiplication(self):
        calc = Calculator()
        calc.add_input('3')
        calc.add_input('*')
        calc.add_input('4')
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '12')

    def test_division(self):
        calc = Calculator()
        calc.add_input('10')
        calc.add_input('/')
        calc.add_input('2')
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '5')

    def test_negative_result(self):
        calc = Calculator()
        calc.add_input('5')
        calc.add_input('-')
        calc.add_input('10')
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '-5')

    # Testy dla systemu binarnego
    def test_addition_binary(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.BIN
        calc.add_input('1101')  # 13 in binary
        calc.add_input('+')
        calc.add_input('101')   # 5 in binary
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0b10010')  # 18 in binary

    def test_subtraction_binary(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.BIN
        calc.add_input('1010')  # 10 in binary
        calc.add_input('-')
        calc.add_input('11')    # 3 in binary
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0b111')  # 7 in binary

    def test_multiplication_binary(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.BIN
        calc.add_input('110')   # 6 in binary
        calc.add_input('*')
        calc.add_input('10')    # 2 in binary
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0b1100')  # 12 in binary

    def test_division_binary(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.BIN
        calc.add_input('1100')  # 12 in binary
        calc.add_input('/')
        calc.add_input('10')    # 2 in binary
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0b110')  # 6 in binary

    def test_addition_hexadecimal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.HEX
        calc.add_input('A')     # 10 in hexadecimal
        calc.add_input('+')
        calc.add_input('5')     # 5 in hexadecimal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0xF')  # 15 in hexadecimal

    def test_subtraction_hexadecimal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.HEX
        calc.add_input('B')     # 11 in hexadecimal
        calc.add_input('-')
        calc.add_input('2')     # 2 in hexadecimal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0x9')  # 9 in hexadecimal

    def test_multiplication_hexadecimal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.HEX
        calc.add_input('A')     # 10 in hexadecimal
        calc.add_input('*')
        calc.add_input('4')     # 4 in hexadecimal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0x28')  # 40 in hexadecimal

    def test_division_hexadecimal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.HEX
        calc.add_input('1E')    # 30 in hexadecimal
        calc.add_input('/')
        calc.add_input('5')     # 5 in hexadecimal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0x6')  # 6 in hexadecimal

    def test_addition_octal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.OCT
        calc.add_input('15')    # 13 in octal
        calc.add_input('+')
        calc.add_input('5')     # 5 in octal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0o22')  # 16 in octal

    def test_subtraction_octal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.OCT
        calc.add_input('17')    # 15 in octal
        calc.add_input('-')
        calc.add_input('2')     # 2 in octal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0o15')  # 13 in octal

    def test_multiplication_octal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.OCT
        calc.add_input('12')    # 10 in octal
        calc.add_input('*')
        calc.add_input('4')     # 4 in octal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0o50')  # 40 in octal

    def test_division_octal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.OCT
        calc.add_input('50')    # 40 in octal
        calc.add_input('/')
        calc.add_input('5')     # 5 in octal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0o10')  # 8 in octal

# Operacje binarne
class BinaryOperationsTests(unittest.TestCase):
    def test_bitwise_and_binary(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.BIN
        calc.add_input('1101')  # 13 in binary
        calc.add_input('&')
        calc.add_input('1011')  # 11 in binary
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0b1001')  # 9 in binary

    def test_bitwise_and_decimal(self):
        calc = Calculator()
        calc.add_input('13')
        calc.add_input('&')
        calc.add_input('11')
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '9')

    def test_bitwise_and_octal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.OCT
        calc.add_input('15')  # 13 in octal
        calc.add_input('&')
        calc.add_input('13')  # 11 in octal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0o11')  # 9 in octal

    def test_bitwise_and_hexadecimal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.HEX
        calc.add_input('D')  # 13 in hexadecimal
        calc.add_input('&')
        calc.add_input('B')  # 11 in hexadecimal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0x9')  # 9 in hexadecimal

    def test_bitwise_or_binary(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.BIN
        calc.add_input('1101')  # 13 in binary
        calc.add_input('|')
        calc.add_input('1011')  # 11 in binary
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0b1111')  # 15 in binary

    def test_bitwise_or_decimal(self):
        calc = Calculator()
        calc.add_input('13')
        calc.add_input('|')
        calc.add_input('11')
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '15')

    def test_bitwise_or_octal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.OCT
        calc.add_input('15')  # 13 in octal
        calc.add_input('|')
        calc.add_input('13')  # 11 in octal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0o17')  # 15 in octal

    def test_bitwise_or_hexadecimal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.HEX
        calc.add_input('D')  # 13 in hexadecimal
        calc.add_input('|')
        calc.add_input('B')  # 11 in hexadecimal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0xF')  # 15 in hexadecimal

    def test_bitwise_xor_binary(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.BIN
        calc.add_input('1101')  # 13 in binary
        calc.add_input('^')
        calc.add_input('1011')  # 11 in binary
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0b110')  # 6 in binary

    def test_bitwise_xor_decimal(self):
        calc = Calculator()
        calc.add_input('13')
        calc.add_input('^')
        calc.add_input('11')
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '6')

    def test_bitwise_xor_octal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.OCT
        calc.add_input('15')  # 13 in octal
        calc.add_input('^')
        calc.add_input('13')  # 11 in octal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0o6')  # 6 in octal

    def test_bitwise_xor_hexadecimal(self):
        calc = Calculator()
        calc.numeric_system = NumericSystem.HEX
        calc.add_input('D')  # 13 in hexadecimal
        calc.add_input('^')
        calc.add_input('B')  # 11 in hexadecimal
        calc.perform_operation()
        self.assertEqual(str(calc.get_result()), '0x6')  # 6 in hexadecimal




if __name__ == '__main__':
    unittest.main()
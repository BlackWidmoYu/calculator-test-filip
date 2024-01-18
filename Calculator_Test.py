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
                calc.last_number = '0'
                calc.operation = ""

                calc.add_input(i)
                self.assertEqual(calc.last_number, '0')
                self.assertEqual(calc.operation, i)

class ByteDataTypeTests(unittest.TestCase):
    def test_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        self.assertEqual(calc.add_input('0'), True)
        self.assertEqual(calc.last_number, '0')

    def test2_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        self.assertEqual(calc.add_input('00'), True)
        self.assertEqual(calc.last_number, '0')

    def test3_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        self.assertEqual(calc.add_input('127'), True)
        self.assertEqual(calc.last_number, '127')

    def test4_input_between_specific_values_range_negative(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        self.assertEqual(calc.add_input('128'), False)
    
    def test5_input_between_specific_values_range_minus_valid(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        self.assertEqual(calc.add_input('-128'), True)
        self.assertEqual(calc.last_number, '-128')

    def test6_input_between_specific_values_range_minus_invalid(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        self.assertEqual(calc.add_input('-129'), False)

    def test7_acceptable_input(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        calc.add_input('2')
        calc.add_input('2')
        calc.add_input('2')
        self.assertEqual(calc.last_number, '22')

    def test8_acceptable_negative_input(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        calc.add_input('-1')
        calc.add_input('2')
        calc.add_input('9')
        self.assertEqual(calc.last_number, '-12')

class WordDataTypeTests(unittest.TestCase):
    def test_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        self.assertEqual(calc.add_input('0'), True)
        self.assertEqual(calc.last_number, '0')

    def test2_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        self.assertEqual(calc.add_input('00'), True)
        self.assertEqual(calc.last_number, '0')

    def test3_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        self.assertEqual(calc.add_input('32767'), True)
        self.assertEqual(calc.last_number, '32767')

    def test4_input_between_specific_values_range_negative(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        self.assertEqual(calc.add_input('32768'), False)
    
    def test5_input_between_specific_values_range_minus_valid(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        self.assertEqual(calc.add_input('-32768'), True)
        self.assertEqual(calc.last_number, '-32768')

    def test6_input_between_specific_values_range_minus_invalid(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        self.assertEqual(calc.add_input('-32769'), False)

    def test7_acceptable_input(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('3')
        calc.add_input('2')
        calc.add_input('7')
        calc.add_input('9')
        calc.add_input('9')
        self.assertEqual(calc.last_number, '3279')

    def test8_acceptable_negative_input(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('-3')
        calc.add_input('2')
        calc.add_input('7')
        calc.add_input('9')
        calc.add_input('9')
        self.assertEqual(calc.last_number, '-3279')

class DwordDataTypeTests(unittest.TestCase):
    def test_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        self.assertEqual(calc.add_input('0'), True)
        self.assertEqual(calc.last_number, '0')

    def test2_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        self.assertEqual(calc.add_input('00'), True)
        self.assertEqual(calc.last_number, '0')

    def test3_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        self.assertEqual(calc.add_input('2147483647'), True)
        self.assertEqual(calc.last_number, '2147483647')

    def test4_input_between_specific_values_range_negative(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        self.assertEqual(calc.add_input('2147483648'), False)
    
    def test5_input_between_specific_values_range_minus_valid(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        self.assertEqual(calc.add_input('-2147483648'), True)
        self.assertEqual(calc.last_number, '-2147483648')

    def test6_input_between_specific_values_range_minus_invalid(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        self.assertEqual(calc.add_input('-2147483649'), False)

    def test7_acceptable_input(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('2')
        calc.add_input('1')
        calc.add_input('4')
        calc.add_input('7')
        calc.add_input('4')
        calc.add_input('8')
        calc.add_input('3')
        calc.add_input('6')
        calc.add_input('4')
        calc.add_input('9')
        self.assertEqual(calc.last_number, '214748364')

    def test8_acceptable_negative_input(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('-2')
        calc.add_input('1')
        calc.add_input('4')
        calc.add_input('7')
        calc.add_input('4')
        calc.add_input('8')
        calc.add_input('3')
        calc.add_input('6')
        calc.add_input('4')
        calc.add_input('9')
        self.assertEqual(calc.last_number, '-214748364')

class QwordDataTypeTests(unittest.TestCase):
    def test_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        self.assertEqual(calc.add_input('0'), True)
        self.assertEqual(calc.last_number, '0')

    def test2_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        self.assertEqual(calc.add_input('00'), True)
        self.assertEqual(calc.last_number, '0')

    def test3_input_between_specific_values_range(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        self.assertEqual(calc.add_input('9223372036854775807'), True)
        self.assertEqual(calc.last_number, '9223372036854775807')

    def test4_input_between_specific_values_range_negative(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        self.assertEqual(calc.add_input('9223372036854775808'), False)
    
    def test5_input_between_specific_values_range_minus_valid(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        self.assertEqual(calc.add_input('-9223372036854775808'), True)
        self.assertEqual(calc.last_number, '-9223372036854775808')

    def test6_input_between_specific_values_range_minus_invalid(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        self.assertEqual(calc.add_input('-9223372036854775809'), False)

    def test7_acceptable_input(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('9')
        calc.add_input('2')
        calc.add_input('2')
        calc.add_input('3')
        calc.add_input('3')
        calc.add_input('7')
        calc.add_input('2')
        calc.add_input('0')
        calc.add_input('3')
        calc.add_input('6')
        calc.add_input('8')
        calc.add_input('5')
        calc.add_input('4')
        calc.add_input('7')
        calc.add_input('7')
        calc.add_input('5')
        calc.add_input('8')
        calc.add_input('0')
        calc.add_input('8')
        self.assertEqual(calc.last_number, '922337203685477580')

    def test8_acceptable_negative_input(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('-9')
        calc.add_input('2')
        calc.add_input('2')
        calc.add_input('3')
        calc.add_input('3')
        calc.add_input('7')
        calc.add_input('2')
        calc.add_input('0')
        calc.add_input('3')
        calc.add_input('6')
        calc.add_input('8')
        calc.add_input('5')
        calc.add_input('4')
        calc.add_input('7')
        calc.add_input('7')
        calc.add_input('5')
        calc.add_input('8')
        calc.add_input('0')
        calc.add_input('9')
        self.assertEqual(calc.last_number, '-922337203685477580')

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

class GetCurrentMinMaxTests(unittest.TestCase):
    def test_byte_max_value(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        self.assertEqual(calc.get_current_max_value(), 2**7 - 1)

    def test_byte_min_value(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        self.assertEqual(calc.get_current_min_value(), -2**7)

    def test_word_max_value(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        self.assertEqual(calc.get_current_max_value(), 2**15 - 1)

    def test_word_min_value(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        self.assertEqual(calc.get_current_min_value(), -2**15)

    def test_dword_max_value(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        self.assertEqual(calc.get_current_max_value(), 2**31 - 1)

    def test_dword_min_value(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        self.assertEqual(calc.get_current_min_value(), -2**31)

    def test_qword_max_value(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        self.assertEqual(calc.get_current_max_value(), 2**63 - 1)

    def test_qword_min_value(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        self.assertEqual(calc.get_current_min_value(), -2**63)

    def test_invalid_data_type(self):
        calc = Calculator()
        calc.data_type = None
        self.assertEqual(calc.get_current_min_value(), 0)
        self.assertEqual(calc.get_current_min_value(), 0)

class DataTypeCastingTests(unittest.TestCase):
    # Casting from byte to other data types
    def test_byte_to_word1(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        calc.add_input('127')
        self.assertEqual(calc.binary_representation, '01111111')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '127')
        self.assertEqual(calc.binary_representation, '0000000001111111')
    
    def test_byte_to_word2(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        calc.add_input('-128')
        self.assertEqual(calc.binary_representation, '10000000')
        
        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '-128')
        self.assertEqual(calc.binary_representation, '1111111110000000')

    def test_byte_to_dword1(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        calc.add_input('127')
        self.assertEqual(calc.binary_representation, '01111111')

        self.assertEqual(calc.change_data_type(DataType.dword), True)
        self.assertEqual(calc.last_number, '127')
        self.assertEqual(calc.binary_representation, 
                         '00000000000000000000000001111111')
    
    def test_byte_to_dword2(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        calc.add_input('-128')
        self.assertEqual(calc.binary_representation, '10000000')
        
        self.assertEqual(calc.change_data_type(DataType.dword), True)
        self.assertEqual(calc.last_number, '-128')
        self.assertEqual(calc.binary_representation, 
                         '11111111111111111111111110000000')
        
    def test_byte_to_qword1(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        calc.add_input('127')
        self.assertEqual(calc.binary_representation, '01111111')

        self.assertEqual(calc.change_data_type(DataType.qword), True)
        self.assertEqual(calc.last_number, '127')
        self.assertEqual(calc.binary_representation, 
            '0000000000000000000000000000000000000000000000000000000001111111')
    
    def test_byte_to_qword2(self):
        calc = Calculator()
        calc.change_data_type(DataType.byte)
        calc.add_input('-128')
        self.assertEqual(calc.binary_representation, '10000000')
        
        self.assertEqual(calc.change_data_type(DataType.qword), True)
        self.assertEqual(calc.last_number, '-128')
        self.assertEqual(calc.binary_representation, 
            '1111111111111111111111111111111111111111111111111111111110000000')
    
    # Casting from word to other data types
    def test_word_to_byte1(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('128')
        self.assertEqual(calc.binary_representation, '0000000010000000')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-128')
        self.assertEqual(calc.binary_representation, '10000000')

    def test_word_to_byte2(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('129')
        self.assertEqual(calc.binary_representation, '0000000010000001')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-127')
        self.assertEqual(calc.binary_representation, '10000001')

    def test_word_to_byte3(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('255')
        self.assertEqual(calc.binary_representation, '0000000011111111')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-1')
        self.assertEqual(calc.binary_representation, '11111111')

    def test_word_to_byte4(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('500')
        self.assertEqual(calc.binary_representation, '0000000111110100')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-12')
        self.assertEqual(calc.binary_representation, '11110100')

    def test_word_to_byte5(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('280')
        self.assertEqual(calc.binary_representation, '0000000100011000')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '24')
        self.assertEqual(calc.binary_representation, '00011000')

    def test_word_to_dword1(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('1123')
        self.assertEqual(calc.binary_representation, '0000010001100011')

        self.assertEqual(calc.change_data_type(DataType.dword), True)
        self.assertEqual(calc.last_number, '1123')
        self.assertEqual(calc.binary_representation, 
                         '00000000000000000000010001100011')
    def test_word_to_dword2(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('-23456')
        self.assertEqual(calc.binary_representation, '1010010001100000')

        self.assertEqual(calc.change_data_type(DataType.dword), True)
        self.assertEqual(calc.last_number, '-23456')
        self.assertEqual(calc.binary_representation, 
                         '11111111111111111010010001100000')
        
    def test_word_to_qword1(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('1123')
        self.assertEqual(calc.binary_representation, '0000010001100011')

        self.assertEqual(calc.change_data_type(DataType.qword), True)
        self.assertEqual(calc.last_number, '1123')
        self.assertEqual(calc.binary_representation, 
            '0000000000000000000000000000000000000000000000000000010001100011')
    def test_word_to_qword2(self):
        calc = Calculator()
        calc.change_data_type(DataType.word)
        calc.add_input('-23456')
        self.assertEqual(calc.binary_representation, '1010010001100000')

        self.assertEqual(calc.change_data_type(DataType.qword), True)
        self.assertEqual(calc.last_number, '-23456')
        self.assertEqual(calc.binary_representation, 
            '1111111111111111111111111111111111111111111111111010010001100000')
    
    # Dword casting tests
    def test_dword_to_byte1(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('128')
        self.assertEqual(calc.binary_representation, '00000000000000000000000010000000')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-128')
        self.assertEqual(calc.binary_representation, '10000000')

    def test_dword_to_byte2(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('129')
        self.assertEqual(calc.binary_representation, '00000000000000000000000010000001')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-127')
        self.assertEqual(calc.binary_representation, '10000001')

    def test_dword_to_byte3(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('255')
        self.assertEqual(calc.binary_representation, '00000000000000000000000011111111')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-1')
        self.assertEqual(calc.binary_representation, '11111111')

    def test_dword_to_byte4(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('500')
        self.assertEqual(calc.binary_representation, '00000000000000000000000111110100')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-12')
        self.assertEqual(calc.binary_representation, '11110100')

    def test_dword_to_byte5(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('280')
        self.assertEqual(calc.binary_representation, '00000000000000000000000100011000')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '24')
        self.assertEqual(calc.binary_representation, '00011000')

    def test_dword_to_word1(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('1123')
        self.assertEqual(calc.binary_representation, '00000000000000000000010001100011')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '1123')
        self.assertEqual(calc.binary_representation, '0000010001100011')

    def test_dword_to_word2(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('-23456')
        self.assertEqual(calc.binary_representation, '11111111111111111010010001100000')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '-23456')
        self.assertEqual(calc.binary_representation, '1010010001100000')

    def test_dword_to_word3(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('32768')
        self.assertEqual(calc.binary_representation, '00000000000000001000000000000000')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '-32768')
        self.assertEqual(calc.binary_representation, '1000000000000000')

    def test_dword_to_word4(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('32769')
        self.assertEqual(calc.binary_representation, '00000000000000001000000000000001')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '-32767')
        self.assertEqual(calc.binary_representation, '1000000000000001')

    def test_dword_to_word5(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('65535')
        self.assertEqual(calc.binary_representation, '00000000000000001111111111111111')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '-1')
        self.assertEqual(calc.binary_representation, '1111111111111111')

    def test_dword_to_qword1(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('1123')
        self.assertEqual(calc.binary_representation, '00000000000000000000010001100011')

        self.assertEqual(calc.change_data_type(DataType.qword), True)
        self.assertEqual(calc.last_number, '1123')
        self.assertEqual(calc.binary_representation,
            '0000000000000000000000000000000000000000000000000000010001100011')

    def test_dword_to_qword2(self):
        calc = Calculator()
        calc.change_data_type(DataType.dword)
        calc.add_input('-23456')
        self.assertEqual(calc.binary_representation, '11111111111111111010010001100000')

        self.assertEqual(calc.change_data_type(DataType.qword), True)
        self.assertEqual(calc.last_number, '-23456')
        self.assertEqual(calc.binary_representation,
            '1111111111111111111111111111111111111111111111111010010001100000')
        
    def test_qword_to_byte1(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('128')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000000000000010000000')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-128')
        self.assertEqual(calc.binary_representation, '10000000')

    def test_qword_to_byte2(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('129')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000000000000010000001')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-127')
        self.assertEqual(calc.binary_representation, '10000001')

    def test_qword_to_byte3(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('255')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000000000000011111111')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-1')
        self.assertEqual(calc.binary_representation, '11111111')

    def test_qword_to_byte4(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('500')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000000000000111110100')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '-12')
        self.assertEqual(calc.binary_representation, '11110100')

    def test_qword_to_byte5(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('280')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000000000000100011000')

        self.assertEqual(calc.change_data_type(DataType.byte), True)
        self.assertEqual(calc.last_number, '24')
        self.assertEqual(calc.binary_representation, '00011000')

    def test_qword_to_word1(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('1123')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000000000010001100011')
        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '1123')
        self.assertEqual(calc.binary_representation, '0000010001100011')\
        
    def test_qword_to_word2(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('-23456')
        self.assertEqual(calc.binary_representation, '1111111111111111111111111111111111111111111111111010010001100000')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '-23456')
        self.assertEqual(calc.binary_representation, '1010010001100000')

    def test_qword_to_word3(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('32768')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000001000000000000000')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '-32768')
        self.assertEqual(calc.binary_representation, '1000000000000000')

    def test_qword_to_word4(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('32769')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000001000000000000001')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '-32767')
        self.assertEqual(calc.binary_representation, '1000000000000001')

    def test_qword_to_word5(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('65535')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000001111111111111111')

        self.assertEqual(calc.change_data_type(DataType.word), True)
        self.assertEqual(calc.last_number, '-1')
        self.assertEqual(calc.binary_representation, '1111111111111111')

    def test_qword_to_dword1(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('1123')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000000000000000000000000010001100011')

        self.assertEqual(calc.change_data_type(DataType.dword), True)
        self.assertEqual(calc.last_number, '1123')
        self.assertEqual(calc.binary_representation,
            '00000000000000000000010001100011')
        
    def test_qword_to_dword2(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('-23456')
        self.assertEqual(calc.binary_representation, '1111111111111111111111111111111111111111111111111010010001100000')

        self.assertEqual(calc.change_data_type(DataType.dword), True)
        self.assertEqual(calc.last_number, '-23456')
        self.assertEqual(calc.binary_representation,
            '11111111111111111010010001100000')

    def test_qword_to_dword3(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('2147483648')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000010000000000000000000000000000000')

        self.assertEqual(calc.change_data_type(DataType.dword), True)
        self.assertEqual(calc.last_number, '-2147483648')
        self.assertEqual(calc.binary_representation,
            '10000000000000000000000000000000')

    def test_qword_to_dword4(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('2147483649')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000010000000000000000000000000000001')

        self.assertEqual(calc.change_data_type(DataType.dword), True)
        self.assertEqual(calc.last_number, '-2147483647')
        self.assertEqual(calc.binary_representation,
            '10000000000000000000000000000001')

    def test_qword_to_dword5(self):
        calc = Calculator()
        calc.change_data_type(DataType.qword)
        calc.add_input('4294967295')
        self.assertEqual(calc.binary_representation, '0000000000000000000000000000000011111111111111111111111111111111')

        self.assertEqual(calc.change_data_type(DataType.dword), True)
        self.assertEqual(calc.last_number, '-1')
        self.assertEqual(calc.binary_representation, '11111111111111111111111111111111')


if __name__ == '__main__':
    unittest.main()
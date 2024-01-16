import tkinter as tk
from enum import Enum, auto
import sys

class NumericSystem(Enum):
    BIN = ("01", 2)
    DEC = ("0123456789", 10)
    HEX = ("0123456789ABCDEF", 16)
    OCT = ("01234567", 8)

class DataType(Enum):
    byte  = '1'
    word  = '2'
    dword = '4'
    qword = '8'

class Sign(Enum):
    POSITIVE = auto()
    NEGATIVE = auto()

class Operation(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    AND = '&'
    OR = '|'
    XOR = '^'
    NONE = 'NONE'

def twos(val_str, bytes):
    val = int(val_str, 2)
    b = val.to_bytes(bytes, byteorder=sys.byteorder, signed=False)                                                          
    return int.from_bytes(b, byteorder=sys.byteorder, signed=True)

class Calculator:
    def __init__(self):
        self.last_number = "0"
        self.change_number = False
        self.expression = "0"
        self.result = ""
        self.operation = Operation.NONE.value[0]
        self.numeric_system = NumericSystem.DEC
        self.sign = Sign.POSITIVE
        self.data_type = DataType.qword

        # Data types
        self.max_value = self.get_current_max_value()
        self.binary_representation = '0' * 64
        self.update_binary_representation()

    def get_current_max_value(self):
        if self.data_type == DataType.byte:
            return 2**7 - 1
        elif self.data_type == DataType.word:
            return 2**15 - 1
        elif self.data_type == DataType.dword:
            return 2**31 - 1
        elif self.data_type == DataType.qword:
            return 2**63 - 1
        
    def get_current_min_value(self):
        if self.data_type == DataType.byte:
            return -2**7
        elif self.data_type == DataType.word:
            return -2**15
        elif self.data_type == DataType.dword:
            return -2**31
        elif self.data_type == DataType.qword:
            return -2**63
        
    def update_binary_representation(self):
        old_binary_representation = self.binary_representation
        numeric_value = int(self.last_number, self.numeric_system.value[1])
        
        data_type_length = int(self.data_type.value) * 8
        
        if self.sign == Sign.NEGATIVE:
            max_value = 2 ** data_type_length
            numeric_value = (numeric_value + max_value) % max_value

        binary_representation = bin(numeric_value)[2:].zfill(data_type_length)

        if not self.is_binary_representation_within_bounds():
            print(f"Input exceeds the maximum value or minimum value for {int(self.data_type.value) * 8} data type.")
            self.expression = str(self.get_system_input_representation(old_binary_representation, 2))
            self.last_number = str(self.get_system_input_representation(old_binary_representation, 2))
            self.binary_representation = old_binary_representation
            return False

        self.binary_representation = binary_representation
        print(self.binary_representation)
        
    def is_binary_representation_within_bounds(self):
        print("Abs: ", abs(int(self.last_number, self.numeric_system.value[1])))
        print("Max value: ", self.max_value)
        return int(self.last_number, self.numeric_system.value[1]) <= self.max_value and int(self.last_number, self.numeric_system.value[1]) >= self.get_current_min_value()

    def update_max_value(self):
        self.max_value = self.get_current_max_value()
    
    def is_input_valid(self, input):
        for char in input:
            if char not in self.numeric_system.value[0]:
                return False
        return True
    
    def get_system_input_representation(self, input, old_numeric_system_value=10):
        if self.numeric_system == NumericSystem.BIN:
            return bin(int(input, old_numeric_system_value))
        elif self.numeric_system == NumericSystem.OCT:
            return oct(int(input, old_numeric_system_value))
        elif self.numeric_system == NumericSystem.DEC:
            return int(input, old_numeric_system_value)
        elif self.numeric_system == NumericSystem.HEX:
            return hex(int(input, old_numeric_system_value)).upper().replace('X', 'x')

    def add_input(self, input):
        zeroes = ("0", "0b0", "0x0", "0o0")

        if (self.is_input_valid(input)):
            number = self.get_system_input_representation(input, self.numeric_system.value[1])
            if self.expression in zeroes:
                self.expression = str(number)
                self.last_number = str(number)
                self.update_binary_representation()
                return True
            else:
                if self.change_number:
                    self.last_number = str(number)
                    self.expression += str(number)
                    self.change_number = False
                else:
                    self.last_number += str(number).replace("0o", "").replace("0x", "").replace("0b", "")
                    self.expression += str(number).replace("0o", "").replace("0x", "").replace("0b", "")
                self.update_binary_representation()
                return True
        elif input != Operation.NONE.value[0] and any(input in member.value[0] for member in Operation):
            self.expression += input
            self.operation = input
            self.change_number = True
            self.update_binary_representation()
            return True
        else:
            print("Wrong input:", input)
            return False
    
    def perform_operation(self):
        print("INPUT:", self.expression)
        try:
            self.result = self.get_system_input_representation(str(eval(self.expression.replace("/", "//"))))
            self.expression = str(self.result)
            self.last_number = str(self.result)
            print("Result:", self.result)
        except:
            print("Wrong expression:", self.expression)
            self.result = 0
            self.expression = "0"
            self.last_number = "0"

        if str(self.result).startswith('-'):
            self.sign = Sign.NEGATIVE
        else:
            self.sign = Sign.POSITIVE
        
        self.update_binary_representation()
        self.operation = Operation.NONE.value[0]

    def get_result(self):
        return self.result
    
    def change_data_type(self, new_data_type):
        if isinstance(new_data_type, DataType):
            old_data_type = self.data_type
            old_sign_bit = self.binary_representation[0]
            self.data_type = new_data_type
            self.update_max_value()
            if int(self.data_type.value) < int(old_data_type.value):
                self.last_number = str(self.get_system_input_representation(str(twos(self.binary_representation, int(self.data_type.value)))))
                self.expression = str(self.get_system_input_representation(str(twos(self.binary_representation, int(self.data_type.value)))))
            print("Changed to ", self.last_number)

            if old_sign_bit == '1' or int(self.last_number, self.numeric_system.value[1]) < 0:
                self.sign = Sign.NEGATIVE
            else:
                self.sign = Sign.POSITIVE
            self.update_binary_representation()

            print("Changed Data Type to:", new_data_type)
        else:
            print("Wrong data type:", new_data_type)
    
    def change_numeric_system(self, new_numeric_system):
        if isinstance(new_numeric_system, NumericSystem):
            old_numeric_system_value = self.numeric_system.value[1]
            self.numeric_system = new_numeric_system
            self.expression = str(self.get_system_input_representation(self.last_number, old_numeric_system_value))
            self.last_number = self.expression
        else:
            print("Wrong numeric system:", new_numeric_system)

class CalculatorGUI(tk.Tk):
    def __init__(self, calculator):
        super().__init__()

        self.calculator = calculator
        self.geometry("700x450")

        self.title("Calculator")
        self.resizable(False, False)

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.binary_label_var = tk.StringVar()
        self.binary_label_var.set("0000000000000000000000000000000000000000000000000000000000000000")

        self.create_widgets()

    def activate_buttons(self):
        active_numbers = self.calculator.numeric_system.value[0]
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text") in NumericSystem.HEX.value[0]:
                button_text = widget.cget("text")
                widget["state"] = tk.NORMAL if button_text in active_numbers else tk.DISABLED

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 14), bd=10, insertwidth=4, width=14,
                        justify='right', state='readonly')
        entry.grid(row=0, column=0, columnspan=10, padx=0, pady=0)

        binary_label_frame = tk.Frame(self)
        binary_label_frame.grid(row=1, column=0, columnspan=10, padx=0, pady=0)

        binary_label = tk.Label(binary_label_frame, textvariable=self.binary_label_var, font=('Arial', 12), bd=10, anchor='w', width=80)
        binary_label.grid(row=1, column=0, sticky='w', columnspan=10)

        numeric_buttons = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        for i, num in enumerate(numeric_buttons):
            row_index = i // 3 + 2
            col_index = i % 3 + 1
            tk.Button(self, text=num, command=lambda n=num: self.on_button_click(n), width=10, height=2).grid(row=row_index, column=col_index, padx=2, pady=2)

        hex_buttons = ['A', 'B', 'C', 'D', 'E', 'F']
        for i, hex_num in enumerate(hex_buttons):
            tk.Button(self, text=hex_num, command=lambda h=hex_num: self.on_button_click(h), width=10, height=2).grid(row=2+i, column=0, padx=2, pady=2)

        operation_buttons = ['+', '-', '*', '/', '&', '|', '^', '=']
        for i, op in enumerate(operation_buttons):
            tk.Button(self, text=op, command=lambda o=op: self.on_button_click(o), width=4, height=2).grid(row=i+2 if i < 4 else i-2, column=4 if i < 4 else 5, padx=2, pady=2)

        system_buttons = ['Dec', 'Bin', 'Oct', 'Hex']
        for i, sys in enumerate(system_buttons):
            tk.Button(self, text=sys, command=lambda s=sys: self.change_numeric_system(s), width=10, height=2).grid(row=7, column=i+1, padx=2, pady=2)

        data_type_label = tk.Label(self, text="Data Type:")
        data_type_label.grid(row=8, column=1, sticky='e', padx=5, pady=5)

        data_types = [dt.name.capitalize() for dt in DataType]
        data_type_var = tk.StringVar()
        data_type_var.set(self.calculator.data_type.name.capitalize())
        data_type_dropdown = tk.OptionMenu(self, data_type_var, *data_types, command=self.change_data_type_gui)
        data_type_dropdown.grid(row=8, column=2, sticky='w', padx=5, pady=5)

        self.activate_buttons()


    def on_button_click(self, value):
        if value == '=':
            self.calculator.perform_operation()
        else:
            self.calculator.add_input(value)
        self.result_var.set(str(self.calculator.last_number).replace("0b", "").replace("0o", "").replace("0x", ""))
        self.binary_label_var.set(f"{self.calculator.binary_representation}")
        print("Current Expression:", self.calculator.expression)

    def change_numeric_system(self, system):
        new_system = None
        if system == 'Dec':
            new_system = NumericSystem.DEC
        elif system == 'Bin':
            new_system = NumericSystem.BIN
        elif system == 'Oct':
            new_system = NumericSystem.OCT
        elif system == 'Hex':
            new_system = NumericSystem.HEX

        if new_system:
            self.calculator.change_numeric_system(new_system)
            self.result_var.set(str(self.calculator.last_number).replace("0b", "").replace("0o", "").replace("0x", ""))
            print("Changed Numeric System to:", new_system)
            self.activate_buttons()

    def change_data_type_gui(self, data_type):
        data_type_enum = next(dt for dt in DataType if dt.name.capitalize() == data_type.capitalize())
        self.calculator.change_data_type(data_type_enum)
        self.binary_label_var.set(f"{self.calculator.binary_representation}")
        print("Changed Data Type to:", data_type_enum)

if __name__ == "__main__":
    calculator = Calculator()
    calculator_gui = CalculatorGUI(calculator)
    calculator_gui.mainloop()

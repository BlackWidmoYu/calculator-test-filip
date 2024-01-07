import tkinter as tk
from enum import Enum, auto

class NumericSystem(Enum):
    BIN = ("01", 2)
    DEC = ("0123456789", 10)
    HEX = ("0123456789ABCDEF", 16)
    OCT = ("01234567", 8)

class DataType(Enum):
    byte  = '8'
    word  = '16'
    dword = '32'
    qword = '64'

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
            else:
                if self.change_number:
                    self.last_number = str(number)
                    self.expression += str(number)
                    self.change_number = False
                else:
                    self.last_number += str(number).replace("0o", "").replace("0x", "").replace("0b", "")
                    self.expression += str(number).replace("0o", "").replace("0x", "").replace("0b", "")
        elif input != Operation.NONE.value[0] and any(input in member.value[0] for member in Operation):
            self.expression += input
            self.operation = input
            self.change_number = True
        else:
            print("Wrong input:", input)
    
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
        self.operation = Operation.NONE.value[0]
    def get_result(self):
        return self.result
    
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

        self.title("Calculator")
        self.resizable(False, False)

        self.result_var = tk.StringVar()
        self.result_var.set("0")

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
        entry.grid(row=0, column=1, columnspan=5)


        hex_buttons = ['A', 'B', 'C', 'D', 'E', 'F']
        for i, hex_num in enumerate(hex_buttons):
            tk.Button(self, text=hex_num, command=lambda h=hex_num: self.on_button_click(h), width=2).grid(row=i+1, column=0)

        numeric_buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0'
        ]

        for i, num in enumerate(numeric_buttons):
            row_index = i // 3 + 1
            col_index = i % 3 + 2
            tk.Button(self, text=num, command=lambda n=num: self.on_button_click(n), width=2).grid(row=row_index+2, column=col_index)

        operation_buttons = ['+', '-', '*', '/', '&', '|', '^', '=']
        for i, op in enumerate(operation_buttons):
            tk.Button(self, text=op, command=lambda o=op: self.on_button_click(o), width=2).grid(row=i+2 if i < 4 else i-2, column=5 if i < 4 else 6)

        system_buttons = ['Dec', 'Bin', 'Oct', 'Hex']
        for i, sys in enumerate(system_buttons):
            tk.Button(self, text=sys, command=lambda s=sys: self.change_numeric_system(s), width=2).grid(row=7, column=i+2)

        self.activate_buttons()

    def on_button_click(self, value):
        if value == '=':
            self.calculator.perform_operation()
        else:
            self.calculator.add_input(value)
        self.result_var.set(str(self.calculator.last_number).replace("0b", "").replace("0o", "").replace("0x", ""))
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


if __name__ == "__main__":
    calculator = Calculator()
    calculator_gui = CalculatorGUI(calculator)
    calculator_gui.mainloop()

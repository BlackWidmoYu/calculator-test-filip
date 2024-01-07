import tkinter as tk
from enum import Enum, auto

class NumericSystem(Enum):
    BIN = "01"
    DEC = "0123456789"
    HEX = "0123456789ABCDEF"
    OCT = "01234567"

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
        self.expression = ""
        self.result = ""
        self.operation = Operation.NONE.value
        self.numeric_system = NumericSystem.DEC
        self.sign = Sign.POSITIVE
        self.data_type = DataType.qword
    
    def is_input_valid(self, input):
        for char in input:
            if char not in self.numeric_system.value:
                return False
        return True
    
    def get_system_input_representation(self, input):
        if self.numeric_system == NumericSystem.BIN:
            return bin(int(input))
        elif self.numeric_system == NumericSystem.OCT:
            return oct(int(input))
        elif self.numeric_system == NumericSystem.DEC:
            return int(input)
        elif self.numeric_system == NumericSystem.HEX:
            print(input)
            return hex(int(input))

    def add_input(self, input):
        if (self.is_input_valid(input)):
            number = self.get_system_input_representation(input)
            print("Added num:", number)
            if self.expression == "0":
                self.expression = str(number)
            else:
                self.expression += str(number)
            if self.operation != Operation.NONE.value:
                self.perform_operation()
        elif input != Operation.NONE.value and any(input in member.value for member in Operation):
            self.expression += input
            self.operation = input
        else:
            print("Wrong input:", input)
    
    def perform_operation(self):
        print("INPUT:", self.expression)
        try:
            self.result = self.get_system_input_representation(str(eval(self.expression.replace("/", "//"))))
            self.expression = str(self.result)
            print("Result:", self.result)
        except:
            print("Wrong expression:", self.expression)
            self.result = 0
            self.expression = "0"
        self.operation = Operation.NONE.value
    def get_result(self):
        return self.result
    
    def change_numeric_system(self, new_numeric_system):
        if isinstance(new_numeric_system, NumericSystem):
            self.numeric_system = new_numeric_system
            self.expression = self.get_system_input_representation(self.expression)
        else:
            print("Wrong numeric system:", new_numeric_system)

class CalculatorGUI(tk.Tk):
    def __init__(self, calculator):
        super().__init__()

        self.calculator = calculator

        self.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 14), bd=10, insertwidth=4, width=14,
                         justify='right', state='readonly')
        entry.grid(row=0, column=0, columnspan=4)

        for i in range(9, -1, -1):
            tk.Button(self, text=str(i), command=lambda num=i: self.on_button_click(str(num))).grid(
                row=(9 - i) // 3 + 1, column=(8 - i) % 3)
        operations = ['+', '-', '*', '/', '&', '|', '^', '=']
        for i, op in enumerate(operations):
            tk.Button(self, text=op, command=lambda o=op: self.on_button_click(o)).grid(row=i // 2 + 1, column=3 + i % 2)

        tk.Button(self, text="Change System", command=self.change_numeric_system).grid(row=5, column=3)

    def on_button_click(self, value):
        self.calculator.add_input(value)
        self.result_var.set(str(self.calculator.expression))
        print("Current Expression:", self.calculator.expression)

    def change_numeric_system(self):
        new_system = NumericSystem.HEX if self.calculator.numeric_system == NumericSystem.DEC else NumericSystem.DEC
        self.calculator.change_numeric_system(new_system)
        self.result_var.set(str(self.calculator.expression))
        print("Changed Numeric System to:", new_system)


if __name__ == "__main__":
    calculator = Calculator()
    print(eval("77/7"))
    calculator_gui = CalculatorGUI(calculator)
    calculator_gui.mainloop()

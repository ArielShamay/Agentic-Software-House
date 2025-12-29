import tkinter as tk
from operations import Operations

class GUI:
    def __init__(self, master):
        self.master = master
        self.operations = Operations()
        self.entry_field = tk.Entry(master, width=20)
        self.entry_field.grid(row=0, column=0, columnspan=4)
        self.create_buttons()
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.master, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        tk.Button(self.master, text='0', width=5, command=lambda: self.click_button('0')).grid(row=row_val, column=0)
        tk.Button(self.master, text='C', width=5, command=self.clear_entry).grid(row=row_val, column=1)
        tk.Button(self.master, text='=', width=5, command=self.calculate_result).grid(row=row_val, column=2)
        tk.Button(self.master, text='+', width=5, command=lambda: self.click_button('+')).grid(row=row_val, column=3)
    def click_button(self, button):
        current = self.entry_field.get()
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(0, str(current) + str(button))
    def clear_entry(self):
        self.entry_field.delete(0, tk.END)
    def calculate_result(self):
        try:
            result = eval(self.entry_field.get())
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(0, str(result))
        except Exception as e:
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(0, 'Error')
import tkinter as tk
from tkinter import messagebox
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Dasar")

        # Variabel untuk menyimpan input dan hasil
        self.input_var = tk.StringVar()
        self.result_var = tk.StringVar()
        #Entry untuk input
        self.entry = tk.Entry(root, textvariable=self.input_var, font=("Arial", 20), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 20), justify='right', state='readonly')
        self.result_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('C', 6, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, ipadx=20, ipady=20)

    def on_button_click(self, char):
        if char == 'C':
            self.input_var.set('')
            self.result_var.set('')
        elif char == '=':
            try:
                result = eval(self.input_var.get())
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        else:
            current = self.input_var.get() 
            self.input_var.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    kalkulator = CalculatorApp(root)
    root.mainloop()
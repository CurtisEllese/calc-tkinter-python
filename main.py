import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=25, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+"
        ]

        row_num = 1
        col_num = 0
        for label in button_list:
            tk.Button(master, text=label, width=5, height=2, command=lambda label=label:self.button_click(label)).grid(row=row_num, column=col_num, padx=5, pady=5)
            col_num += 1
            if col_num > 3:
                col_num = 0
                row_num += 1

        tk.Button(master, text="=", width=22, height=2, command=self.calculate).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    def button_click(self, label):
        current = self.display.get()
        if label == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, current + label)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

root = tk.Tk()
my_calc = Calculator(root)
root.mainloop()

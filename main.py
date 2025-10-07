import tkinter as tk
from math import sin, cos, pow, sqrt, tan

def main():
    main_root = tk.Tk()
    main_root.title("Calculator")
    CALCULATOR_IMAGE = tk.PhotoImage(file="calculator_photo.png")
    main_root.iconphoto(True, CALCULATOR_IMAGE)

    just_space = tk.StringVar(value="")

    def button_click(symbol):
        if symbol == "=":
            try:
                result = eval(text_box.get())
                text_box.delete(0, tk.END)
                text_box.insert(tk.END, result)
            except Exception:
                text_box.delete(0, tk.END)
                text_box.insert(tk.END, "Error")
        elif symbol == "C":
            text_box.delete(0, tk.END)
        else:
            text_box.insert(tk.END, symbol)

    buttons = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('sin', 5, 0), ('cos', 5, 1), ('sqrt', 5, 2), ('pow', 5, 3),
        ('tan', 6, 0), ('(', 6, 1), (')', 6, 2), ('C', 6, 3)
    ]

    text_box = tk.Entry(main_root, font=("Arial", 16), bd=5, textvariable=just_space)
    text_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

    for (text, row, col) in buttons:
        tk.Button(
            main_root,
            text=text,
            width=7,
            height=3,
            command=lambda t=text: button_click(t)
        ).grid(row=row, column=col)

    main_root.geometry("370x450")
    main_root.resizable(False, False)
    main_root.mainloop()

    return 0

main()
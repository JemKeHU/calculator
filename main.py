import tkinter as tk


def main():
    main_root = tk.Tk()
    main_root.title("Calculator")
    CALCULATOR_IMAGE = tk.PhotoImage(file="calculator_photo.png")
    main_root.iconphoto(True, CALCULATOR_IMAGE)

    def button_click(symbol):
        if symbol == "=":
            try:
                result = eval(text_box.get())
                text_box.delete(0, tk.END)
                text_box.insert(tk.END, result)
            except Exception:
                text_box.delete(0, tk.END)
                text_box.insert(tk.END, "Error")
        else:
            text_box.insert(tk.END, symbol)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    text_box = tk.Entry(main_root, font=("Arial", 16), bd=5)
    text_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

    for (text, row, col) in buttons:
        tk.Button(
            main_root,
            text=text,
            width=7,
            height=3,
            command=lambda t=text: button_click(t)
        ).grid(row=row, column=col)

    main_root.geometry("370x320")
    main_root.resizable(False, False)
    main_root.mainloop()

    return 0

main()
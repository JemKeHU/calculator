import tkinter as tk

def main():
    main_root = tk.Tk()
    main_root.title("Test1")
    CALCULATOR_IMAGE = tk.PhotoImage(file="calculator_photo.png")
    main_root.iconphoto(True, CALCULATOR_IMAGE)

    def button_clicked(i=1):
        if i <= 10:
            label2.config(text=f"Number {i} is displayed!")
            main_root.after(1000, button_clicked, i + 1)

    label1 = tk.Label(main_root, text="Test message!")
    label1.pack()

    button1 = tk.Button(main_root, text="Stop", width=25, command=main_root.destroy)
    button1.pack()

    button2 = tk.Button(main_root, text="Click me!", width=25, command=button_clicked)
    button2.pack()
    label2 = tk.Label(main_root, text="Number \"kal\" is displayed!")
    label2.pack()

    main_root.geometry("340x240")
    main_root.mainloop()

    return 0

main()
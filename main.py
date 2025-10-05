import tkinter as tk

def main():
    main_root = tk.Tk()
    main_root.title("Test1")
    CALCULATOR_IMAGE = tk.PhotoImage(file="calculator_photo.png")
    main_root.iconphoto(True, CALCULATOR_IMAGE)

    label1 = tk.Label(main_root, text="Test message!")
    label1.pack()

    button1 = tk.Button(main_root, text="Stop", width=25, command=main_root.destroy)
    button1.pack()

    main_root.geometry("240x240")
    main_root.mainloop()

    return 0

main()
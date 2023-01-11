import tkinter as tk
from tkinter import ttk


class Example(ttk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root, padding=10)
        root.title('Hello')
        self.grid()

        ttk.Label(self, text='Hello World!', padding=10).grid(column=0, row=0)
        ttk.Button(self, text='Quit', command=root.destroy).grid(column=0, row=1)


def main():
    root = tk.Tk()
    app = Example(root)
    app.mainloop()


if __name__ == "__main__":
    main()

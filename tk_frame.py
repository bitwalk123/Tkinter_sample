import tkinter as tk
from tkinter import ttk


class Example(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root.title('Frame')
        self.pack()

        self.frame2 = ttk.Frame(
            self,
            width=200, height=100,
            borderwidth=5, relief='sunken'
        )
        self.frame2.pack()

def main():
    root = tk.Tk()
    app = Example(root)
    app.mainloop()


if __name__ == "__main__":
    main()

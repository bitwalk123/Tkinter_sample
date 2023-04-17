import tkinter as tk


class Hello:
    def __init__(self, master):
        self.master = master
        master.title("Hello World!")

        self.button = tk.Button(master, text="Hello World!", command=self.say_hello)
        self.button.pack()

    def say_hello(self):
        print("Hello World!")


def main():
    root = tk.Tk()
    app = Hello(root)
    root.mainloop()


if __name__ == '__main__':
    main()

import tkinter as tk


class Panel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Panel')
        self.menu_options()

    def menu_options(self):
        menu_bar = tk.Menu(self)

        file_menu = tk.Menu(menu_bar, tearoff=0)

        file_menu.add_command(label='New Project')
        file_menu.add_command(label='Open')

        menu_bar.add_cascade(label='File', menu=file_menu)

        self.config(menu=menu_bar)

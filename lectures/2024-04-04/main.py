import tkinter as tk


class Login(tk.Tk):
    def __init__(self, size, title):
        super().__init__()
        self.geometry(size)
        self.title(title)
        self.widgets()

    def widgets(self):
        label_username = tk.Label(self, text='Full name')
        label_username.grid(row=0, column=0)

        entry_username = tk.Entry(self)
        entry_username.grid(row=0, column=1)

        label_password = tk.Label(self, text='Address')
        label_password.grid(row=1, column=0)

        entry_password = tk.Entry(self)
        entry_password.grid(row=1, column=1)

        button_add_record = tk.Button(self, text='Add record')
        button_add_record.grid(row=2, column=1)


if __name__ == '__main__':
    login = Login('300x300', 'Log in')
    login.mainloop()

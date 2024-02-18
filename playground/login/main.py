import tkinter as tk

from center_window import center_window
from connection import Connection

# Define constants
USERNAME = 'root'
PASSWORD = '1234567890'
DATABASE = 'IT_Department'
HOST = 'localhost'

connection = Connection(username=USERNAME, password=PASSWORD, database=DATABASE, host=HOST)
connection.establish_connection()

login_window = tk.Tk()
login_window.title('Log in')

center_window(width=400, height=400, window=login_window)

frame = tk.Frame(login_window)
frame.place(relx=0.5, rely=0.5, anchor='center')


def login():
    username = entry_username.get()
    password = entry_password.get()

    if len(entry_username.get()) != 0 and len(entry_password.get()) != 0:
        connection.log_in(username, password)
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)


label_username = tk.Label(master=frame, text='Username')
label_username.grid(row=0, column=0)

entry_username = tk.Entry(master=frame)
entry_username.grid(row=0, column=1)

label_password = tk.Label(master=frame, text='Password')
label_password.grid(row=1, column=0)

entry_password = tk.Entry(master=frame, show='*')
entry_password.grid(row=1, column=1)

button_login = tk.Button(master=frame, text='Log in', command=login)
button_login.grid(row=2, column=1)

login_window.mainloop()

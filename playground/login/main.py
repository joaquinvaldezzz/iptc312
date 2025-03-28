# Import tkinter
import tkinter as tk
from tkinter import ttk

# Import custom modules
from center_window import center_window
from connection import Connection

# Define constants
USERNAME = 'root'
# Change this to `root` or whatever password you set during installation
PASSWORD = '1234567890'
DATABASE = 'IT_Department'
HOST = 'localhost'

# Create an instance of the Connection class
connection = Connection(
    username=USERNAME, password=PASSWORD, database=DATABASE, host=HOST)

# Establish a connection to the database
connection.establish_connection()

# Create a window
login_window = tk.Tk()

# Set the title of the window
login_window.title('Log in')

# Center the window using the `center_window` function
center_window(width=512, height=512, window=login_window)

# Create a frame
frame = tk.Frame(login_window)

# Place the frame in the center of the window
frame.place(relx=0.5, rely=0.5, anchor='center')


# Define a function to log in
def login():
    # Get the username and password from the entry widgets
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are not empty
    if len(entry_username.get()) != 0 and len(entry_password.get()) != 0:
        # Change the `log_in` to `sign_up` for signing up
        connection.sign_up(username, password)

        # Delete the content of the username and password entry
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

        connection.display(database_view)
    else:
        # If the username and password are empty, display a message
        print('Please enter a username and password.')


def edit():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are not empty
    if len(entry_username.get()) != 0 and len(entry_password.get()) != 0:
        # Change the `log_in` to `sign_up` for signing up
        connection.sign_up(username, password)

        # Delete the content of the username and password entry
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

        connection.display(database_view)
    else:
        # If the username and password are empty, display a message
        print('Please enter a username and password.')


# Create a label for the username
label_username = tk.Label(master=frame, text='Username')

# Create an entry widget for the username
entry_username = tk.Entry(master=frame)

# Create a label for the password
label_password = tk.Label(master=frame, text='Password')

# Create an entry widget for the password
entry_password = tk.Entry(master=frame, show='*')

# Create a button to log in
button_login = tk.Button(master=frame, text='Log in', command=login)

button_edit = tk.Button(master=frame, text='Edit', command=connection.edit())

database_view = ttk.Treeview(master=frame, columns=(
    'id', 'username', 'password'), show='headings')
database_view.heading('id', text='ID')
database_view.heading('username', text='Username')
database_view.heading('password', text='Password')
connection.display(database_view)

# Place all widgets in the frame using the grid layout manager
label_username.grid(row=0, column=0)
entry_username.grid(row=0, column=1)
label_password.grid(row=1, column=0)
entry_password.grid(row=1, column=1)
button_login.grid(row=2, column=1)
database_view.grid(row=3, column=0, columnspan=2)


# Run the main loop
login_window.mainloop()

idk = tk.Label(cursor=frame, text='ID',)

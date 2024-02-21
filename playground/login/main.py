# Import tkinter
import tkinter as tk

# Import custom modules
from center_window import center_window
from connection import Connection

# Define constants
USERNAME = 'root'
PASSWORD = '1234567890'
DATABASE = 'IT_Department'
HOST = 'localhost'

# Create an instance of the Connection class
connection = Connection(username=USERNAME, password=PASSWORD, database=DATABASE, host=HOST)

# Establish a connection to the database
connection.establish_connection()

# Create a window
login_window = tk.Tk()

# Set the title of the window
login_window.title('Log in')

# Center the window using the center_window function
center_window(width=400, height=400, window=login_window)

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
        connection.log_in(username, password)
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    # If the username and password are empty, display a message
    else:
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

# Place all widgets in the frame using the grid layout manager
label_username.grid(row=0, column=0)
entry_username.grid(row=0, column=1)
label_password.grid(row=1, column=0)
entry_password.grid(row=1, column=1)
button_login.grid(row=2, column=1)

# Run the main loop
login_window.mainloop()

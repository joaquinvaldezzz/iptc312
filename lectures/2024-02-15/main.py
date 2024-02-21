# Import tkinter
import tkinter as tk

# Create a window
window = tk.Tk()

# Set the size of the window
window.geometry('400x400')

# Set the title of the window
window.title('Main Window')

# Create a label
label_text = tk.Label(master=window,
                      text='Type a message then click the button to extract the text')


# Define a function to extract text
def extract_text():
    # Get the message from the entry widget
    message = entry_message.get()

    # Check if the message is not empty
    if len(message) != 0:
        label_text.config(text=message)
    # If the message is empty, display a message
    else:
        label_text.config(text='Please enter something')


# Create an entry and a button widget
entry_message = tk.Entry(master=window, justify='center')
button_extract_text = tk.Button(master=window, text='Extract text', command=extract_text)

# Place the widgets in the window
label_text.pack()
entry_message.pack()
button_extract_text.pack()

# Run the main loop
window.mainloop()

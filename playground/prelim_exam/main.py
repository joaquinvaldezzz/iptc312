# Importing the tkinter module
import tkinter as tk

# Creating a new tkinter window
window = tk.Tk()

# Setting the geometry of the window
window.geometry('256x128')

# Setting the title of the window
window.title('Preliminary Examination')

# Creating a new Label widget
# master: the parent widget, in this case, the window
# text: the text displayed on the label
label_welcome = tk.Label(master=window, text='Hello Second Semester!')

# Adding the Label widget to the window
label_welcome.pack()

# Starting the main event loop
window.mainloop()

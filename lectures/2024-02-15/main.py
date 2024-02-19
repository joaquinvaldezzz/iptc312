import tkinter as tk

from playground.login.center_window import center_window

window = tk.Tk()
window.title('Main Window')

center_window(width=400, height=400, window=window)

label_text = tk.Label(master=window,
                      text='Type a message then click the button to extract the text')
label_text.pack()


def extract_text():
    message = entry_message.get()

    if len(message) != 0:
        label_text.config(text=message)
    else:
        label_text.config(text='Please enter something')


entry_message = tk.Entry(master=window, justify='center')
entry_message.pack()

button_extract = tk.Button(
    master=window, text='Extract text', command=extract_text)
button_extract.pack()

window.mainloop()

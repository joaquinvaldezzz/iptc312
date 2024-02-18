import tkinter as tk

window = tk.Tk()
window.geometry('400x400')
window.title('Main Window')

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

button_extract = tk.Button(master=window, text='Extract text', command=extract_text)
button_extract.pack()

window.mainloop()

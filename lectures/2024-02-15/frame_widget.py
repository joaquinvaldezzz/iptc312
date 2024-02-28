import tkinter as tk

window = tk.Tk()

# window.geometry('500x500')
#
# frame = tk.Frame(master=window, bg='red', colormap='new', height=100, width=100)
# frame.pack(side=tk.LEFT)
#
# frame = tk.Frame(master=window, bg='green', colormap='new', height=100, width=100)
# frame.pack(side=tk.BOTTOM)
#
# frame = tk.Frame(master=window, bg='blue', colormap='new', height=100, width=100)
# frame.pack(side=tk.RIGHT)
#
# frame = tk.Frame(master=window, bg='yellow', colormap='new', height=100, width=100)
# frame.pack(side=tk.TOP)

window.geometry('300x300')
window.title('Border Effects')

border_effects = {
    'flat': tk.FLAT,
    'sunken': tk.SUNKEN,
    'raised': tk.RAISED,
    'groove': tk.GROOVE,
    'ridge': tk.RIDGE,
}

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, borderwidth=4, relief=relief)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()

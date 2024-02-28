import tkinter as tk

window = tk.Tk()
window.title('Grid Layout')

for row in range(3):
    for column in range(3):
        frame = tk.Frame(master=window, borderwidth=1, relief=tk.RAISED)
        frame.grid(row=row, column=column)
        label = tk.Label(master=frame, text=f'Row {row}\nColumn {column}')
        label.pack()

window.mainloop()

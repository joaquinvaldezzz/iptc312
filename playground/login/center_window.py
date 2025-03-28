def center_window(width, height, window):
    x = (window.winfo_screenwidth() / 2) - (width / 2)
    y = (window.winfo_screenheight() / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

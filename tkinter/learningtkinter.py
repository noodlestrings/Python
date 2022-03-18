import this
import tkinter as tk

window = tk.Tk()
window.title("Hello World")

# title with no args returns the title
titleOfWindow = window.title()

window_width = 550
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = (screen_width // 2) - (window_width // 2)
center_y = (screen_height // 2) - (window_height // 2)

# geometry method takes 'widthxheight+-X+-Y'
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# stops the window being able to be resized  resizable(width, height)
window.resizable(False, True)

# .minsize or .maxsize takes the width and height that can be resized to
window.minsize(500, 100)
window.maxsize(500, 800)


# 0 fully transparent, 1 fully opaque
# THIS ONLY FOR LINUX
window.wait_visibility(window)
# ONLY THIS WORKS ON WINDOWS
window.attributes('-alpha', 0.5)

# shows window above all others
window.attributes("-topmost", 1)


# label creates a widget and takes two arguments, the container and options (e.g. text)
message = tk.Label(window, text="Hello World")
message.pack()


# keeps the window displaying, should be after all other code
window.mainloop()


import tkinter as tk

root = tk.Tk()
root.title("Image Example")
root.geometry("400x400")

# Load the image (must be PNG or GIF)
img = tk.PhotoImage(file="black.png")

# Put it in a label
label = tk.Label(root, image=img)
label.pack()

root.mainloop()

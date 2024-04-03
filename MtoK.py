import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# convert function
def convert():
    miles = float(entry.get())
    km = miles * 1.60934
    output_label.config(text=f"Kilometers: {km}")

#window
window = ttk.Window(themename="darkly")
window.title("M to K convertor!")
window.geometry('550x200')

# title
title_label = ttk.Label(master=window, text="Miles to Kilometers!", font=("Arial 24 bold"))
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text="Convert", command= convert)
entry.pack(side=tk.LEFT, padx=10)
button.pack(side=tk.LEFT)
input_frame.pack(pady=10)

# output
output_label = ttk.Label(master=window, text="Kilometers: 0", font=("Arial 16"))
output_label.pack(pady=10)

# run
window.mainloop()
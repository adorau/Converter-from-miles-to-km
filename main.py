from tkinter import *


def counting_write():
    miles_write = float(input_miles.get())
    km = round(miles_write*1.61,2)
    result_label.config(text=km)


def counting_scale(mil_scale):
    km = round(int(mil_scale) * 1.61, 2)
    result_label.config(text=km)


window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=200, height=200)
window.configure(background='#dff5fb')
window.config(padx=50, pady=50)

miles_label = Label(text="miles", background='#dff5fb')
miles_label.grid(row=0, column=2)

miles_label2 = Label(text="miles", background='#dff5fb')
miles_label2.grid(row=3, column=2)

km_label = Label(text="km", background='#dff5fb')
km_label.grid(row=1, column=2)

is_equal_label = Label(text="is equal to", background='#dff5fb')
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0", width=13, background="#6ed5ee", font=("Arial",12))
result_label.grid(row=1, column=1)
result_label.rowconfigure(40, weight=10)

calculate_bottom = Button(text="calculate", font=("Arial", 10), command=counting_write, width=25, background="#B0E0E6")
calculate_bottom.grid(row=2, column=1)

input_miles = Entry()
input_miles.grid(row=0, column=1)


mil_scale = Scale(from_=0, to=100, orient=HORIZONTAL, sliderlength=20, width=60, command=counting_scale,
                  background='#dff5fb')
mil_scale.grid(row=3, column=1)

window.mainloop()

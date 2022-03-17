from tkinter import *

def converter():
    miles = float(input_entry.get())
    km = miles*1.609
    kilometer_label.config(text=f'{km}')


window = Tk()
window.minsize(width=500, height=200)
window.title("Miles to Kilometer Converter")
window.config(padx=100, pady=100)


input_entry = Entry(width=20)
input_entry.grid(column=1, row=0)


miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

is_equal_label = Label(text = "is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(text="0")
kilometer_label.grid(column=1, row=1)

kmeter_label = Label(text="KM")
kmeter_label.grid(column=2, row =1)

calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(column=1, row=2)


window.mainloop()

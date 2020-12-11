"""
Program Name:   Celsius to Fahrenheit GUI
Filename        main.py
Author:         Ryan Fong
Date:           2 December 2020
Assignment:     Assignment 14
Description:    Celsius to Fahrenheit conversion through tkinter gui library
Sources:        javatpoint.com/python-tkinter
"""


import tkinter


CONVERSION_FACTOR = 9/5


def calculate_button__click():
    """
    Module Name:   calculate_button__click()
    Parameters:    None
    Description:   Performs the conversion of celsius to fahrenheit and posts it to result label
    """
    global celsius_entry
    global fahrenheit_result
    celsius_temp = float(celsius_entry.get())
    fahrenheit_temp = CONVERSION_FACTOR * celsius_temp + 32
    fahrenheit_result.configure(text=f'The degrees Fahrenheit is: {fahrenheit_temp}', relief=tkinter.RIDGE, bg='#cad2f7')


def exit_button__click():
    """
    Module Name:   exit_button__click()
    Parameters:    None
    Description:   Destroys main window
    """
    root.destroy()


root = tkinter.Tk()  #Creating window object as root
root.geometry('400x150')  #Setting window geometry as 400px by 150px
root.configure(bg='#8b9dee')  #Setting background color for main window


input_frame = tkinter.Frame(root, bg='#8b9dee', pady=15)  #Frame object for first Label and Entry
input_frame.pack()
entry_label = tkinter.Label(input_frame, bg='#8b9dee', padx=5, text='Enter the temperature in Celsius:    ')
entry_label.pack(side='left')
celsius_entry = tkinter.Entry(input_frame, borderwidth=4, relief=tkinter.RIDGE, width=15)
celsius_entry.pack(side='right')

result_frame = tkinter.Frame(root, bg='#8b9dee')
result_frame.pack(fill=tkinter.X)
fahrenheit_result = tkinter.Label(result_frame, borderwidth=4, bg='#8b9dee')  #Creating empty Label, text is set later in calculate_button__click()
fahrenheit_result.pack()

button_frame = tkinter.Frame(root, bg='#8b9dee')
button_frame.pack(fill=tkinter.X)
entry_submit = tkinter.Button(button_frame, borderwidth=3, text='Calculate', bg='#4c63cd', command=calculate_button__click)
entry_submit.pack(side='left')
exit_button = tkinter.Button(button_frame, borderwidth=3, text='Exit', bg='#4c63cd', command=exit_button__click)
exit_button.pack(side='right')

root.mainloop()

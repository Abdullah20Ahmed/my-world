from tkinter import *
import webbrowser

def open_link():
    if age_var.get() == 0:   
        status_label.config(text="You must confirm you are over 16.", fg="red")
        return

    link = link_entry.get().strip()
    if link != "":
        status_label.config(text="You will now proceed to the link...", fg="green")
        root.after(1000, lambda: webbrowser.open("https://www."+link+".com"))  
    else:
        status_label.config(text="Please enter a link.", fg="red")

def exit_app():
    root.destroy()

root = Tk()
root.title("My Browser App")
root.geometry("500x480")


title_label = Label(root, text="Simple Web Browser", font="Helvetica 14 bold")
title_label.pack(pady=20)


link_entry = Entry(root, width=40, font="Helvetica 12")
link_entry.pack(padx=20, pady=10, ipady=5, fill=X)

age_var = IntVar()
age_check = Checkbutton(
    root,
    text="I confirm that I am over 16 years old",
    variable=age_var,
    font="Helvetica 11"
)
age_check.pack(pady=10)

button_frame = Frame(root)
button_frame.pack(pady=20, fill=X)

open_button = Button(
    button_frame,
    text="Open Link",
    fg="white",
    bg="green",
    padx=20,
    pady=10,
    font="Helvetica 12 bold",
    command=open_link
)
open_button.pack(side=LEFT, padx=20)

exit_button = Button(
    button_frame,
    text="Exit",
    fg="white",
    bg="red",
    padx=30,
    pady=10,
    font="Helvetica 12 bold",
    command=exit_app
)
exit_button.pack(side=RIGHT, padx=20)

status_label = Label(root, text="", font="Helvetica 10")
status_label.pack(pady=10)

root.mainloop()

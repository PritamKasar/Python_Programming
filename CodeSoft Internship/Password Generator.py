from tkinter import *
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    else:
        result_label.config(text="Invalid complexity level")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated Password: " + password)

gui = Tk()
gui.geometry("400x300")
gui.configure(background="cornsilk1")
gui.title(" Password Generator")
length_label = Label(gui, text="Password Length:",font="Lucid 10 bold", background='cornsilk1')
length_label.pack()
length_entry = Entry(font="Lucid 20 bold", border=4, background='cornsilk1')
length_entry.pack()

complexity_label = Label(gui, text="Password Complexity:",font="Lucid 10 bold", background='cornsilk1')
complexity_label.pack()

complexity_var = StringVar()
complexity_var.set("Low")

complexity_low = Radiobutton(gui, text="Low",font="Lucid 10 ", variable=complexity_var, background='cornsilk1', value="Low")
complexity_low.pack()

complexity_medium = Radiobutton(gui, text="Medium",font="Lucid 10 ", variable=complexity_var, background='cornsilk1', value="Medium")
complexity_medium.pack()

complexity_high = Radiobutton(gui, text="High",font="Lucid 10 ", variable=complexity_var, background='cornsilk1', value="High")
complexity_high.pack()

generate_button = Button(gui, text="Generate Password",font="Lucid 10 bold", background='chartreuse1', command=generate_password)
generate_button.pack()


result_label = Label(gui, text="")
result_label.pack()


gui.mainloop()

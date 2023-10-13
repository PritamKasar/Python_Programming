from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1


def inputError():

    if enterTaskField.get() == "":
        messagebox.showerror("Input Error","Please Insert a Task")
        return 0
    return 1

def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

def clear_taskField():
    enterTaskField.delete(0, END)

def insertTask():
    global counter
    value = inputError()
    if value == 0:
        return
    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
    counter += 1
    clear_taskField()

def delete():
    global counter
    if len(tasks_list) == 0:
        messagebox.showerror("No task","Please Insert Task Number For Delete")
        return
    number = taskNumberField.get(1.0, END)
    if number == "\n":
        messagebox.showerror("input error")
        return
    else:
        task_no = int(number)
    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="cornsilk1")
    gui.title("To-Do-List ")
    gui.geometry("260x320")
    enterTask = Label(gui, text="Enter Your Task",font="Lucid 10 bold", background="cornsilk1")
    enterTask.grid(row=0, column=2)
    enterTaskField = Entry(gui, border=4, background='cornsilk1')
    enterTaskField.grid(row=1, column=2, ipadx=50)
    Submit = Button(gui, text="Submit", fg="Black",bg="chartreuse1", font="Lucid 10 bold", command=insertTask)
    Submit.grid(row=3, column=2, padx=4, pady=4)
    TextArea = Text(gui, height=5, width=25,font="lucida 13", border=4, background='cornsilk1')
    TextArea.grid(row=5, column=2, padx=10, sticky=W)
    taskNumber = Label(gui, text="Delete Task Number",font="Lucid 10 bold", bg="cornsilk1")
    taskNumber.grid(row=6, column=2, pady=5)
    taskNumberField = Text(gui, height=1, width=2,font="lucida 13", border=4, background="cornsilk1")
    taskNumberField.grid(row=7, column=2)
    delete = Button(gui, text="Delete", fg="Black",bg="crimson", font="Lucid 10 bold", command=delete)
    delete.grid(row=8, column=2, pady=5)
    Exit = Button(gui, text="Exit", font="Lucid 10 bold",fg="Black", bg="darkgoldenrod1", command=exit)
    Exit.grid(row=9, column=2)
    
    
    gui.mainloop()

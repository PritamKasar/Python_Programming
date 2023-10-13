from tkinter import *

input = ""

def enter(number):
    global input
    input = input + str(number)
    equation.set(input)

def clear_input():
    global input
    input = ""
    equation.set("")
    
def equalto():
    try:
        global input
        ans = str(eval(input))
        equation.set(ans)
        input = ""
    except:
         equation.set("No Input Available! ")
         input = ""

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="cornsilk1")
    gui.title("Basic Calculator")
    gui.geometry("350x300")
    equation = StringVar()
    input_field = Entry(gui, textvariable=equation,font="Lucid 20 bold", border=4, background='cornsilk1',justify='right')
    input_field.grid(columnspan=4, ipadx=15, padx=5, pady=5)
    
    button1 = Button(gui, text=' 1 ', fg='Green Yellow', bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(1), height=2, width=7)
    button1.grid(row=2, column=0, padx=4, pady=4)

    button2 = Button(gui, text=' 2 ', fg='Green Yellow',bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(2), height=2, width=7)
    button2.grid(row=2, column=1, padx=4, pady=4)

    button3 = Button(gui, text=' 3 ', fg='Green Yellow',bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(3), height=2, width=7)
    button3.grid(row=2, column=2, padx=4, pady=4)

    button4 = Button(gui, text=' 4 ', fg='Green Yellow',bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(4), height=2, width=7)
    button4.grid(row=3, column=0, padx=4, pady=4)

    button5 = Button(gui, text=' 5 ', fg='Green Yellow',bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(5), height=2, width=7)
    button5.grid(row=3, column=1, padx=4, pady=4)

    button6 = Button(gui, text=' 6 ', fg='Green Yellow',bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(6), height=2, width=7)
    button6.grid(row=3, column=2, padx=4, pady=4)

    button7 = Button(gui, text=' 7 ', fg='Green Yellow',bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(7), height=2, width=7)
    button7.grid(row=4, column=0, padx=4, pady=4)

    button8 = Button(gui, text=' 8 ', fg='Green Yellow',bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(8), height=2, width=7)
    button8.grid(row=4, column=1, padx=4, pady=4)

    button9 = Button(gui, text=' 9 ', fg='Green Yellow',bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(9), height=2, width=7)
    button9.grid(row=4, column=2, padx=4, pady=4)

    button0 = Button(gui, text=' 0 ', fg='Green Yellow',bg='SlateBlue1',activebackground='blueviolet', command=lambda: enter(0), height=2, width=7)
    button0.grid(row=5, column=0, padx=4, pady=4)    

    decimal = Button(gui, text='.', fg='Green Yellow', bg='SlateBlue1',activebackground='blueviolet',command=lambda: enter('.'), height=2, width=7)
    decimal.grid(row=5, column=1, padx=4, pady=4)

    addition = Button(gui, text=' + ', fg='Green Yellow',bg='mediumpurple2',activebackground='SlateBlue1', command=lambda: enter("+"), height=2, width=7)
    addition.grid(row=2, column=3, padx=4, pady=4)

    subtraction = Button(gui, text=' - ', fg='Green Yellow',bg='mediumpurple2',activebackground='SlateBlue1', command=lambda: enter("-"), height=2, width=7)
    subtraction.grid(row=3, column=3, padx=4, pady=4)

    multiplication = Button(gui, text=' x ', fg='Green Yellow',bg='mediumpurple2',activebackground='SlateBlue1', command=lambda: enter("*"), height=2, width=7)
    multiplication.grid(row=4, column=3, padx=4, pady=4)

    divide = Button(gui, text=' / ', fg='Green Yellow', bg='mediumpurple2',activebackground='SlateBlue1',command=lambda: enter("/"), height=2, width=7)
    divide.grid(row=5, column=3, padx=4, pady=4)

    equal = Button(gui, text=' = ', fg='Green Yellow',bg='mediumpurple2',activebackground='SlateBlue1', command=equalto, height=2, width=7)
    equal.grid(row=5, column=2, padx=4, pady=4)

    clear_input = Button(gui, text='AC ', fg='lightyellow1',bg='blueviolet',activebackground='SlateBlue1', command=clear_input, height=2, width=7)
    clear_input.grid(row=6, ipadx=131, columnspan=4)

    gui.mainloop()

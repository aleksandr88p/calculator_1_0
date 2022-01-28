from tkinter import *

root = Tk()
root.title('калькулятор')  # делаем заголовок

buttons = (('7', '8', '9', '/',),
           ('4', '5', '6', '*',),
           ('1', '2', '3', '-',),
           ('0', '.', '=', '+',))

start = True  # для понимания, вводится ли первое число
lastcommand = '='
result = 0


def click(text):  # принимает текст с кнопки на которую нажали
    global start
    global lastcommand
    global result
    if text.isdigit() or text == '.':
        if start:
            display.configure(text='')  # убираем 0 если пользователь нажал на цифру
            start = False
        # если текст не точка, либо точка, но ее еще не было
        if text != '.' or display.cget('text').find('.') == -1:
            # дальше добавляем цифры в конец display, если пользователь ввел не точку
            display.configure(text=(display.cget('text') + text))
    else:
        if start:
            lastcommand = text
        else:
            calculate(float(display.cget('text')))
            lastcommand = text
            start = True


def calculate(x):
    global lastcommand
    global result
    global display
    if lastcommand == '+':
        result += x
    elif lastcommand == '-':
        result -= x
    elif lastcommand == '*':
        result *= x
    elif lastcommand == '/':
        try:
            result /= x
        except ZeroDivisionError:
            pass
    elif lastcommand == '=':
        result = x

    display.configure(text=result)


# делаем табло
display = Label(root, text='0', font='Tahoma 20', bd=10)
# размещаем в самом верху,
display.grid(row=0, column=0, columnspan=4)

# выводим кнопки, перебираем в цикле
for row in range(4):
    for column in range(4):
        # создаем кнопку
        button = Button(root, text=buttons[row][column], font='Tahoma 20',
                        command=lambda text=buttons[row][column]: click(text))
        button.grid(row=row + 1, column=column, padx=5, pady=5, ipadx=20, ipady=20, sticky='nsew')
        # ^^^ размещаем кнопки(ряд+1, так как первый ряд занят таблом, padx/pady = растягивает кнопку
        # ipadx/ipady = отступы от других кнопок)

# чтобы расположить название по центру, нужнро узнать размер окна
w = root.winfo_reqwidth()  # ширина
h = root.winfo_reqheight()  # высота
# далее узнаем разрешение экрану у пользователя
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws / 2 - w / 2)
y = int(hs / 2 - h / 2)
root.geometry("+{0}+{1}".format(x, y))
root.mainloop()

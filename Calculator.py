"""
@file name: Simplest Calculator
@description:
This program is trying to make a simple calculator where users can perform easy operations such as addition,
 subtraction, multiplication and division.by using provided buttons.
@authors:
Bingshu Li
"""


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# To create a calculator object


class Calculator:
    # The constructor method of calculator object
    def __init__(self, root):
        # the number selected before the operator
        global number_bf
        number_bf = 0
        # the number selected after the operator
        global number_aft
        number_aft = 0
        # True if the next selected number is before the operator
        global first_number
        first_number = True
        # The selected operator
        global operator
        operator = ''
        # True if select a decimal number
        global dec
        dec = False
        # number of decimal places
        global dec_number
        dec_number = 1
        # the decimal string
        global string
        string = ''

        # display the selected number and the calculation result
        def display(number):
            global number_bf
            global dec_number
            global number_aft
            global string

            if not dec:
                if first_number:
                    number_bf = 10 * number_bf + number
                    string = str(number_bf)
                    self.number_label.config(text='{}'.format(number_bf))
                else:
                    number_aft = 10 * number_aft + number
                    string = str(number_aft)
                    self.number_label.config(text='{}'.format(number_aft))
            else:
                if first_number:
                    number_bf = number_bf + 0.1 ** dec_number * number
                    self.number_label.config(text='{}'.format(number_bf))
                    dec_number += 1
                else:
                    number_aft = number_aft + 0.1 ** dec_number * number
                    self.number_label.config(text='{}'.format(number_aft))
                    dec_number += 1

        def plus():
            global operator
            global first_number
            global dec
            global dec_number
            equal()
            dec_number = 0
            dec = False
            first_number = False
            operator = 'p'

        def minus():
            global operator
            global first_number
            global dec
            global dec_number
            equal()
            dec_number = 0
            dec = False
            first_number = False
            operator = 'mi'

        def multiply():
            global operator
            global first_number
            global dec
            global dec_number
            equal()
            dec_number = 0
            dec = False
            first_number = False
            operator = 'mu'

        def divide():
            global operator
            global first_number
            global dec
            global dec_number
            equal()
            dec_number = 0
            dec = False
            first_number = False
            operator = 'd'

        def decimal():
            global dec
            global string
            dec = True
            self.number_label.config(text=string+'.')

        def clear():
            global number_bf
            global operator
            global first_number
            global dec
            global number_aft
            global dec_number
            global string
            string = ''
            dec_number = 1
            self.number_label.config(text='0')
            number_bf = 0
            operator = ''
            first_number = True
            dec = False
            number_aft = 0

        def equal():
            global operator
            global number_bf
            global dec
            global number_aft
            global dec_number
            dec_number = 1
            dec = False

            if operator == '':
                result = number_bf
            elif operator == 'p':
                result = number_bf + number_aft
            elif operator == 'mi':
                result = number_bf - number_aft
            elif operator == 'mu':
                result = number_bf * number_aft

            try:
                if operator == 'd':
                    result = number_bf / number_aft

                number_aft = 0
                number_bf = result
                self.number_label.config(text='{}'.format(result))
            except ZeroDivisionError:
                messagebox.showinfo(title='Dude you are quite stupid...',
                                    message='My boy, you cannot divide anything by zero.;)')
                clear()

        root.resizable(FALSE, FALSE)
        root.title('Simplest Calculator in the world by Mr. Li')
        self.label_frame = ttk.Frame(root)
        self.button_frame = ttk.Frame(root)
        self.label_frame.pack()
        self.button_frame.pack()

        self.number_label = ttk.Label(self.label_frame, width=20, text='0', relief=SUNKEN, anchor='e',
                                      font=('Italy', 25, 'bold'))
        self.number_label.pack(padx=5, pady=5)
        root.configure(background='#e1d8b9')

        ttk.Button(self.button_frame, text='1', command=lambda: display(1)).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(self.button_frame, text='2', command=lambda: display(2)).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.button_frame, text='3', command=lambda: display(3)).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(self.button_frame, text='4', command=lambda: display(4)).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(self.button_frame, text='5', command=lambda: display(5)).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.button_frame, text='6', command=lambda: display(6)).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(self.button_frame, text='7', command=lambda: display(7)).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(self.button_frame, text='8', command=lambda: display(8)).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(self.button_frame, text='9', command=lambda: display(9)).grid(row=2, column=2, padx=5, pady=5)
        ttk.Button(self.button_frame, text='0', command=lambda: display(0)).grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(self.button_frame, text='+', command=plus).grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(self.button_frame, text='-', command=minus).grid(row=1, column=3, padx=5, pady=5)
        ttk.Button(self.button_frame, text='*', command=multiply).grid(row=2, column=3, padx=5, pady=5)
        ttk.Button(self.button_frame, text='/', command=divide).grid(row=3, column=3, padx=5, pady=5)
        ttk.Button(self.button_frame, text='.', command=decimal).grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(self.button_frame, text='=', command=equal).grid(row=3, column=2, padx=5, pady=5)
        ttk.Button(self.button_frame, text='C', width=50, command=clear).grid(row=4, column=0, columnspan=4,
                                                                              padx=5, pady=5)
        self.style = ttk.Style()
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9')
        self.style.configure('TFrame', background='#e1d8b9')


def main():
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == '__main__':
    main()

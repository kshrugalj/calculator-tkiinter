
from tkinter import *

# Create the main window
tk = Tk()
tk.geometry('300x250')
tk.title("KJ Calculator")
expression = "" 
 
# Function to update expression in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
    # concatenation of string 
    expression = expression + str(num) 
    # update the expression by using set method 
    equations.set(expression) 
 
# Function to evaluate the final expression 
def equalsign(): 
    # Try and except statement is used for handling the errors like zero, division error etc. 
    # Put that code inside the try block which may generate the error 
    try: 
        global expression 
        # eval function evaluate the expression and str function convert the result into string 
        total = str(eval(expression)) 
        equations.set(total) 
        # initialize the expression variable by empty string 
        expression = "" 
    # if error is generate then handle by the except block 
    except: 
        equations.set(" error ") 
        expression = "" 
 
# Function to clear the contents of text entry box 
def clearbutton(): 
    global expression 
    expression = "" 
    equations.set("") 

equations = StringVar() 
# All numbers/digits/operands,...
# Making the number 1 button and placing it at (0, 100)
number1 = Button(tk, text="1", command=lambda:press(1),height=3, width=5, bg = 'green')
number1.place(x=0, y=100)
#Making the number 2 and placing it at (50,100)
number2 = Button(tk, text="2",command= lambda:press(2), height=3, width=5, bg = 'green')
number2.place(x=45, y=100)
#Making the number 3 and placing it at (100,100)
number3 = Button(tk, text="3",command= lambda:press(3), height=3, width=5, bg = 'green')
number3.place(x=90, y=100)
#Making the number 4 and placing it at (0,155)
number4 = Button(tk, text="4",command= lambda:press(4), height=3, width=5, bg = 'green')
number4.place(x=0,y=155)
#Making the number 5 and placing it at (45,155)
number5 = Button(tk, text="5",command= lambda:press(5), height=3, width=5, bg = 'green')
number5.place(x = 45, y=155 )
#Making the number 6 and placing it at (90,155)
number6 = Button(tk, text="6",command= lambda:press(6), height=3, width=5, bg = 'green')
number6.place(x=90, y=155)
#Making the number 7 and placing it at (0,210)
number7 = Button(tk, text="7",command= lambda:press(7), height=2, width=5, bg = 'green')
number7.place(x=0, y=210)
#Making the number 8 and placing it at (45,210)
number8 = Button(tk, text="8",command= lambda:press(8), height=2, width=5, bg = 'green')
number8.place(x=45, y=210)
#Making the number 9 and placing it at (90,210)
number9 = Button(tk, text="9",command= lambda:press(9), height=2, width=5, bg = 'green')
number9.place(x=90, y=210)
#Making the number 0 and placing it at (0,60)
number0 = Button(tk, text="0",command= lambda:press(0), height=2, width=5, bg = 'green')
number0.place(x=0, y=60)

# All basic symbols/operators,..
#Making the operator symbol '+' 
plusOperator = Button(tk, text = "+",command= lambda:press('+'), height = 3, width = 10, bg = 'orange')
plusOperator.place(x=135,y=100)
#making the operator symbol '-'
minusoperator = Button(tk, text="-",command= lambda:press('-'), height=3, width=10, bg='orange')
minusoperator.place(x=135, y=155)
#making the operator symbol '*'
multiplicationoperator = Button(tk, text = '*',command= lambda:press('*'), height = 2, width = 10, bg='orange')
multiplicationoperator.place(x=135, y=210)
#making the operator symbol '/'
divisionoperator = Button(tk, text ='/', command= lambda:press('/'), height = 3, width = 11, bg ='orange')
divisionoperator.place(x=215,y=100)

#making the equal sign funtion'='; will be calling equalsign()
equaloperation = Button(tk, text = '=',command= equalsign, height = 3, width = 11, bg = 'orange')
equaloperation.place(x=215,y=155)
#making the clear function 'clear'; will be calling clearbutton()
clearoperation = Button(tk, text = 'clear',command= clearbutton, height = 2, width = 11, bg = 'orange')
clearoperation.place(x=215, y=210)

#making the screen to show inputs 
calcentry = Entry(tk, textvariable=equations)
calcentry.place(x=10, y=10, width=280, height=50)
calcentry.configure(bg = 'lightblue') #making the screen lightblue 

# Start the Tkinter main loop
tk.mainloop()
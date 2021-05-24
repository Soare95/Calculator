from tkinter import *
import math
import parser


root = Tk()
root.geometry('185x305')
root.resizable(0,0)
root.title('Calculator')

display = Entry(root)
display.grid(row = 1, columnspan = 4,sticky=N+E+W+S)

Button(root, text = '=', width = 25, height = 2, cursor = 'hand2', command = lambda: calculate()).grid(row = 8, columnspan = 4)

Button(root, text = 'exp', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations('**')).grid(row = 7, column = 0, sticky=N+E+W+S)
Button(root, text = '0', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(0)).grid(row = 7, column = 1, sticky=N+E+W+S)
Button(root, text = '.', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable('.')).grid(row = 7, column = 2, sticky=N+E+W+S)
Button(root, text = '+', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations('+')).grid(row = 7, column = 3, sticky=N+E+W+S)

Button(root, text = '1', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(1)).grid(row = 6, column = 0, sticky=N+E+W+S)
Button(root, text = '2', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(2)).grid(row = 6, column = 1, sticky=N+E+W+S)
Button(root, text = '3', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(3)).grid(row = 6, column = 2, sticky=N+E+W+S)
Button(root, text = '-', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations('-')).grid(row = 6, column = 3, sticky=N+E+W+S)

Button(root, text = '4', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(4)).grid(row = 5, column = 0, sticky=N+E+W+S)
Button(root, text = '5', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(5)).grid(row = 5, column = 1, sticky=N+E+W+S)
Button(root, text = '6', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(6)).grid(row = 5, column = 2, sticky=N+E+W+S)
Button(root, text = '*', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations('*')).grid(row = 5, column = 3, sticky=N+E+W+S)

Button(root, text = '7', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(7)).grid(row = 4, column = 0, sticky=N+E+W+S)
Button(root, text = '8', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(8)).grid(row = 4, column = 1, sticky=N+E+W+S)
Button(root, text = '9', width = 5, height = 2, cursor = 'hand2', command = lambda: get_variable(9)).grid(row = 4, column = 2, sticky=N+E+W+S)
Button(root, text = '/', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations('/')).grid(row = 4, column = 3, sticky=N+E+W+S)

Button(root, text = '(', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations('(')).grid(row = 3, column = 0, sticky=N+E+W+S)
Button(root, text = ')', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations(')')).grid(row = 3, column = 1, sticky=N+E+W+S)
Button(root, text = '^2', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations('**2')).grid(row = 3, column = 2, sticky=N+E+W+S)
Button(root, text = 'x!', width = 5, height = 2, cursor = 'hand2', command = lambda: factor()).grid(row = 3, column = 3, sticky=N+E+W+S)

Button(root, text = 'PI', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations('*3.14159265')).grid(row = 2, column = 0, sticky=N+E+W+S)
Button(root, text = '%', width = 5, height = 2, cursor = 'hand2', command = lambda: get_operations('/100')).grid(row = 2, column = 1, sticky=N+E+W+S)
Button(root, text = 'AC', width = 5, height = 2, cursor = 'hand2', command = lambda: delete_all()).grid(row = 2, column = 2, sticky=N+E+W+S)
Button(root, text = '<-', width = 5, height = 2, cursor = 'hand2', command = lambda: delete()).grid(row = 2, column = 3, sticky=N+E+W+S)

i = 0
def get_variable(num):
	global i
	display.insert(i, num)
	i += 1

def get_operations(operator):
	global i
	length = len(operator)
	display.insert(i, operator)
	i += length

def delete_all():
	display.delete(0,END)

def calculate():
	entire_string = display.get()
	try:
		a = parser.expr(entire_string).compile()
		result = eval(a)
		delete_all()
		display.insert(0,result)
	except Exception:
		delete_all()
		display.insert(0,"Error")


def delete():
	entire_string = display.get()
	if len(entire_string):
		new_string = entire_string[:-1]
		delete_all()
		display.insert(0, new_string)
	else:
		delete_all()
		display.insert(0, "Error")

def factor():
	entire_string = display.get()
	try:
		result = factorial(int(entire_string))
		delete_all()
		display.insert(0, result)
	except Exception:
		delete_all()
		display.insert(0, "Error")

root.mainloop()
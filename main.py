import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile

from tkinter import messagebox
import subprocess
FILE_NAME = tkinter.NONE

def run():
    global res, res_2
    #save_as()
    #file = str(input("Введите имя файла:"))
    file_2 = str((os.path.basename(FILE_NAME)))
    command_1 = "cd C:\\Users\\Home\\PycharmProjects\\pythonProject1"
    command_2 = "python C:\\Users\Home\\PycharmProjects\\pythonProject1\\"

    new_f = command_2 + file_2

    res = subprocess.call(command_1, shell=True)
     
    res_2 = subprocess.call(new_f, shell=True)
    root.title(file_2+" - Notepad")
    print(new_f)

	
	
def new_file():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete('1.0', tkinter.END)

def save_file():
	data = text.get('1.0', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def save_as():
	out = asksaveasfile(mode='w', defaultextension='txt')
	data = text.get('1.0', tkinter.END)

	out.write(data.rstrip())

def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)
    a = str((os.path.basename(FILE_NAME)))
    
    root.title(a+" - Notepad")


root = tkinter.Tk()
root.title("Notepad")

root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
 
 
text = tkinter.Text(root, width=400, height=400, wrap="word", bg="#263246",font="Courier 12")
text.configure(foreground='lime', selectbackground="#DCDC8C",)
text.pack(fill=BOTH, expand=1)
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Exit", command=root.quit)
menuBar.add_cascade(label="Run", command=run)
root.config(menu=menuBar)
root.mainloop()

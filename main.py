import os.path
import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
import subprocess
import json
from tkinter.messagebox import showerror
from pygments.lexers import PythonLexer
from pygments.token import Token

FILE_NAME = tkinter.NONE

with open("lan.json", "r") as json_file:
    h = json.load(json_file)
langug = (h.get("Lan"))
#lexer = PythonLexer()

def enggg():
    global langug
    a = {"Lan": 'English'}
    with open("lan.json", "w") as json_file:
        json.dump(a, json_file, indent=2)
    langug = 'English'
    print('Restart')

    root.quit()
    d = 'cd C:\\Users\Home\\PycharmProjects\\pythonProject1'
    dd = 'python C:\\Users\Home\\PycharmProjects\\pythonProject1\\VisualNotepad+++.py'
    subprocess.call(d, shell=True)
    subprocess.call(dd, shell=True)
    root.quit()
def russs():
    global langug
    a = {"Lan": 'Russian'}
    with open("lan.json", "w") as json_file:
        json.dump(a, json_file, indent=2)
    langug = 'Russian'
    print('Перезапустите')

    root.quit()
    d = 'cd C:\\Users\Home\\PycharmProjects\\pythonProject1'
    dd = 'python C:\\Users\Home\\PycharmProjects\\pythonProject1\\VisualNotepad+++.py'
    subprocess.call(d, shell=True)
    subprocess.call(dd, shell=True)
    root.quit()
def eng():
    fileMenu.add_command(label="New", command=new_file)
    fileMenu.add_command(label="Open", command=open_file)
    fileMenu.add_command(label="Save", command=save_file)
    fileMenu.add_command(label="Save as", command=save_as)

    menuBar.add_cascade(label="File", menu=fileMenu)
    menuBar.add_cascade(label="Exit", command=root.quit)
    menuBar.add_cascade(label="Run", command=run)
    menuBar.add_cascade(label="Language", menu=fileMenu_2)
    root.config(menu=menuBar)
    root.mainloop()
def rus():
    fileMenu.add_command(label="Новый файл", command=new_file)
    fileMenu.add_command(label="Открыть", command=open_file)
    fileMenu.add_command(label="Сохранить", command=save_file)
    fileMenu.add_command(label="Сохранить как", command=save_as)

    menuBar.add_cascade(label="Файл", menu=fileMenu)
    menuBar.add_cascade(label="Выход", command=root.quit)
    menuBar.add_cascade(label="Выполнить", command=run)
    menuBar.add_cascade(label="Язык", menu=fileMenu_2)

    root.config(menu=menuBar)
    root.mainloop()
def direct():
    global a
    with open("path.json", "r") as json_file:
        a = json.load(json_file)
    return a["File"]
def run():
    global res, res_2
    direct()
    # save_as()
    # file = str(input("Введите имя файла:"))
    file_2 = str((os.path.basename(FILE_NAME)))

    # command_1 = "cd C:\\Users\\Home\\PycharmProjects\\pythonProject1"
    command_1 = "cd " + a["File"]
    # command_2 = "python C:\\Users\Home\\PycharmProjects\\pythonProject1\\"
    command_2 = "python " + a["File"] + "\\"

    new_f = command_2 + file_2

    res = subprocess.call(command_1, shell=True)
    res_2 = subprocess.call(new_f, shell=True)

    root.title(file_2 + " - Notepad")
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
    global d
    out = asksaveasfile(mode='w', defaultextension='txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
        d = os.path.abspath(FILE_NAME)
    except Exception:
        showerror(title="Error", message="Saving file error")
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

    root.title(a + " - Notepad")


root = tkinter.Tk()
root.title("Notepad")
root.iconbitmap("office_folder_icon_219512.ico")
root.minsize(width=500, height=500)
root.maxsize(width=1000, height=500)

text = tkinter.Text(root, width=400, height=400, wrap="word", bg="#1e1e1e", font="Courier 12")
text.configure(foreground='white', selectbackground="#DCDC8C", )
text.pack(fill=BOTH, expand=1)

text.tag_config("keyword", foreground='#98dcfe')
text.tag_config("string_literal", foreground='#ce9178')
text.tag_config("comment", foreground='#529953')


token_type_to_tag = {
    Token.Keyword: "keyword",
    Token.Operator.Word: "keyword",
    Token.Name.Builtin: "keyword",

    Token.Literal.String.Single: "string_literal",
    Token.Literal.String.Double: "string_literal",
    Token.Comment.Single: "comment",
}

def get_text_coord(s: str, i: int):



    for row_number, line in enumerate(s.splitlines(keepends=True), 1):
        if i < len(line):
            return f'{row_number}.{i}'

        i -= len(line)


def on_edit(event):
    # Удалить все имеющиеся теги из текста
    for tag in text.tag_names():
        text.tag_remove(tag, 1.0, END)

    # Разобрать текст на токены
    s = text.get(1.0, END)
    tokens = lexer.get_tokens_unprocessed(s)

    for i, token_type, token in tokens:
        #print(i, token_type, repr(token))  # Отладочный вывод - тут видно какие типы токенов выдаются
        j = i + len(token)
        if token_type in token_type_to_tag:
            text.tag_add(token_type_to_tag[token_type], get_text_coord(s, i), get_text_coord(s, j))

    # Сбросить флаг редактирования текста
    text.edit_modified(0)


text.bind('<<Modified>>', on_edit)
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)
text.pack()

menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu_2 = tkinter.Menu(menuBar)

fileMenu_2.add_command(label="English", command=enggg)
fileMenu_2.add_command(label="Russian", command=russs)

if langug == "English":
    eng()
elif langug == "Russian":
    rus()


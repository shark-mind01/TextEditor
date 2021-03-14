#!C:\Users\ns5_max\AppData\Local\Programs\Python\Python39\python.exe

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    meh.title("Untitled - TextEditor")
    file = None
    TextArea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])
    if file == "":
        file = None
    else:
        meh.title(os.path.basename(file) + " - TextEditor")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

        meh.title(os.path.basename(file) + " - TextEditor")
        print("file Saved")

def quit():
    meh.destroy()
def cut():
    TextArea.event_generate(("<<cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("TextEditor", "Creared BY Amit kumar")

if __name__ == '__main__':
    #Basic Setup
    meh = Tk()
    meh.title("Untitle - TextEditor")
    # meh.wm_iconbitmap("text.ico")
    meh.geometry("650x650")


    # Text Area setup
    TextArea = Text(meh, font="Arial 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)


    # menubar creation
    MenuBar = Menu(meh)
    FileMenu = Menu(MenuBar, tearoff=0)
    # to Open new file
    FileMenu.add_command(label="New", command=newFile)
    #to Open exiting File
    FileMenu.add_command(label="Open", command=openFile)
    #Open Current File
    FileMenu.add_command(label="Save", command = savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quit)
    MenuBar.add_cascade(label = "File", menu=FileMenu)

    meh.config(menu=MenuBar)

    #Edit Menu start
    EditMenu = Menu(MenuBar, tearoff=0)
    #apply feature
    EditMenu.add_command(label = "cut", command=cut)
    EditMenu.add_command(label = "copy", command=copy)
    EditMenu.add_command(label = "paste", command=paste)
    MenuBar.add_cascade(label = "Edit", menu = EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "Info About TextEditor", command=about)
    MenuBar.add_cascade(label = "Help", menu = HelpMenu)

    #scroll Bar Adding
    s = Scrollbar(TextArea)
    s.pack(side=RIGHT, fill=Y)
    s.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=s.set)
    meh.mainloop()

    
 











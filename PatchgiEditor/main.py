# coding: utf-8

# Python2.X encoding wrapper (Windows dedicated processing)
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from tkFileDialog import *
from ScrolledText import *
import sys, os.path
from Tkinter import*

root =Tk()
root.title("PATCHGI EDITOR")
menubar =Menu(root)
root.configure(menu = menubar)

if sys.platform == "win32":

    root.wm_iconbitmap("boarder.ico")



text =ScrolledText(root)
text.pack()

def load_file():
    path_name= ""
    filename = askopenfilename(filetypes=[('Text Files', ('.txt', '.py'))],
                               initialdir=path_name)
    if filename != "":
        path_name = os.path.dirname(filename)
        fi = open(filename)
        text.delete('1.0', 'end')
        for x in fi:
            text.insert('end', x.decode('shift_jis'))
        fi.close()
        text.focus_set()
def save_file():
    data = text.get('0.0', END)
    path_name= ""
    filename = asksaveasfilename(filetypes=[('Text Files', ('.txt', '.py'))],
                               initialdir=path_name)
    if filename != "":
        path_name = os.path.dirname(filename)
        fi = open(filename,"w")
        fi.write(data.encode('utf-8'))
        fi.close()  

File=Menu(menubar,tearoff=False)
Edit=Menu(menubar,tearoff=False)


menubar.add_cascade(label="File",underline=0,menu=File)
menubar.add_cascade(label="Edit",underline=0,menu=Edit)

File.add_command(label="New File",under=0)
File.add_command(label="Open File",under=0,command=load_file)
File.add_command(label="Save File",under=0,command=save_file)



root.mainloop()
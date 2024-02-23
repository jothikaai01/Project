import tkinter as tk
#from tkinter import *
app=tk.Tk()
app.geometry("500x500")
app.title("My New Application")
app.config(bg="black")

def exitcommand():
    app.destroy()

menubar=tk.Menu(app)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
filemenu.add_command(label="New",underline=0,accelerator="Ctrl+N")
filemenu.add_command(label="Open",underline=0,accelerator="Ctrl+O")
filemenu.add_command(label="Save",underline=0,accelerator="Ctrl+S")
filemenu.add_command(label="Save As",underline=5)
filemenu.add_separator()
filemenu.add_command(label="Page Setup",underline=0)
filemenu.add_command(label="Print",underline=0,accelerator="Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",underline=1,command=exitcommand)

editmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu,underline=0)
editmenu.add_command(label="Undo",underline=0,accelerator="Ctrl+N")
editmenu.add_command(label="Copy",underline=0,accelerator="Ctrl+N")
editmenu.add_command(label="Paste",underline=0,accelerator="Ctrl+N")
editmenu.add_command(label="Delete",underline=0,accelerator="Ctrl+N")
editmenu.add_separator()
editmenu.add_command(label="Find",underline=0,accelerator="Ctrl+N")
editmenu.add_command(label="Find Next",underline=0,accelerator="Ctrl+N")
editmenu.add_command(label="Replace",underline=0,accelerator="Ctrl+N")
editmenu.add_command(label="Go To",underline=0,accelerator="Ctrl+N")
editmenu.add_separator()
editmenu.add_command(label="Select All",underline=0,accelerator="Ctrl+N")
editmenu.add_command(label="Time/Date",underline=0,accelerator="Ctrl+N")

formatmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu)
formatmenu.add_command(label="Word Wrap",underline=0)
formatmenu.add_command(label="Font")

viewmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu)
viewmenu.add_command(label="Status Bar",underline=0)

helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="View Help",underline=0)
helpmenu.add_command(label="About Notepad")

app.config(menu=menubar)

app.mainloop()
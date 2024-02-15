from tkinter import *
app=Tk()
app.title("my first python gui app")
app.geometry("500x400+100+100")
app.config(bg="orange")
#app.state("zoomed")

def clickresult():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a+b
    Labeloutput.config(text=c)

def clickresult2():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a-b
    Labeloutput.config(text=c)

def clickresult3():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a*b
    Labeloutput.config(text=c)
    
def clickresult4():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a/b
    Labeloutput.config(text=c)
    

Labeltitle=Label(app,text="A")
Labeltitle.grid(row=0,column=2,padx=40,pady=30)

inputbox1=Entry(app,width=10)
inputbox1.grid(row=0,column=3)

Labeltitle=Label(app,text="B")
Labeltitle.grid(row=3,column=2,padx=40,pady=30)

inputbox2=Entry(app,width=10)
inputbox2.grid(row=3,column=3)

clickme=Button(app,text="Addition",command=clickresult)
clickme.grid(row=4,column=2,padx=40,pady=30)

clickme=Button(app,text="Substraction",command=clickresult2)
clickme.grid(row=4,column=3,padx=40,pady=30)

clickme=Button(app,text="Multiplication",command=clickresult3)
clickme.grid(row=4,column=4,padx=40,pady=30)

clickme=Button(app,text="Division",command=clickresult4)
clickme.grid(row=4,column=5,padx=40,pady=30)

Labeloutput=Label(app,text="result")
Labeloutput.grid(row=5,column=2,padx=40,pady=30)
Labeloutput=Label(app,text="",width=10)
Labeloutput.grid(row=5,column=3,padx=40,pady=30)
app.mainloop()


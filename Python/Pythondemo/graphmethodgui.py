from tkinter import *
app=Tk()
app.title("my first python gui app")
app.geometry("500x400+100+100")
app.config(bg="black")
#app.state("zoomed")

def Addition():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a+b
    Labeloutput.config(text=c)

def Substraction():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a-b
    Labeloutput.config(text=c)

def Multiplication():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a*b
    Labeloutput.config(text=c)
    
def Division():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a/b
    Labeloutput.config(text=c)

def Modulas():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a%b
    Labeloutput.config(text=c)

def BetwiseXOR():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a**b
    Labeloutput.config(text=c)
    
def Floordivision():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a//b
    Labeloutput.config(text=c)

def addassign():
    a=int(inputbox1.get())
    #b=int(inputbox2.get())
    a+=a
    Labeloutput.config(text=a)

def subassign():
    a=int(inputbox1.get())
    #b=int(inputbox2.get())
    a-=3
    Labeloutput.config(text=a)

def multiassign():
    a=int(inputbox1.get())
    #b=int(inputbox2.get())
    a*=a
    Labeloutput.config(text=a)


Labeltitle=Label(app,text="A")
Labeltitle.grid(row=0,column=2,padx=40,pady=30)

inputbox1=Entry(app,width=10)
inputbox1.grid(row=0,column=3)

Labeltitle=Label(app,text="B")
Labeltitle.grid(row=3,column=2,padx=40,pady=30)

inputbox2=Entry(app,width=10)
inputbox2.grid(row=3,column=3)

clickme=Button(app,text="+",command=Addition,bg="blue")
clickme.grid(row=4,column=2,padx=10,pady=10)

clickme=Button(app,text="-",command=Substraction,bg="red")
clickme.grid(row=4,column=3,padx=10,pady=10)

clickme=Button(app,text="*",command=Multiplication,bg="green")
clickme.grid(row=4,column=4,padx=10,pady=10)

clickme=Button(app,text="/",command=Division,bg="yellow")
clickme.grid(row=4,column=5,padx=10,pady=10)

clickme=Button(app,text="%",command=Modulas,bg="pink")
clickme.grid(row=4,column=6,padx=10,pady=10)

clickme=Button(app,text="**",command=BetwiseXOR,bg="gray")
clickme.grid(row=4,column=7,padx=10,pady=10)

clickme=Button(app,text="//",command=Floordivision,bg="purple")
clickme.grid(row=4,column=8,padx=10,pady=10)

clickme=Button(app,text="+=",command=addassign,bg="maroon")
clickme.grid(row=4,column=8,padx=10,pady=10)

clickme=Button(app,text="-=",command=subassign,bg="lightgreen")
clickme.grid(row=4,column=9,padx=10,pady=10)

clickme=Button(app,text="*=",command=multiassign,bg="violet")
clickme.grid(row=4,column=10,padx=10,pady=10)

Labeloutput=Label(app,text="result")
Labeloutput.grid(row=5,column=2,padx=40,pady=30)
Labeloutput=Label(app,text="",width=10)
Labeloutput.grid(row=5,column=3,padx=40,pady=30)
app.mainloop()


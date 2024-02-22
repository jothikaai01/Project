from tkinter import *
import mysql.connector
from tkinter import messagebox
app=Tk()
app.title("Student MarkList")
app.geometry("500x500+100+100")
app.config(bg="gray")

def mysqlfunction():
    con=mysql.connector.connect(

    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="j_jothika"
    )
    return con

def insertrow():
    Tamil=int(inputbox1.get())
    English=int(inputbox2.get())
    Maths=int(inputbox3.get())
    Science=int(inputbox4.get())
    Social=int(inputbox5.get())

    con=mysqlfunction()
    result=con.cursor()
    statem="INSERT INTO studentmarklist (Tamil,English,Maths,Science,Social) values(%s,%s,%s,%s,%s)" 
    values=(Tamil,English,Maths,Science,Social)
    result.execute(statem,values)
    con.commit()
    print(result.rowcount,"row insert")
    print(messagebox.showinfo("information","data entered this program"))

def updaterow():
    Tamil=int(inputbox1.get())
    #English=int(inputbox2.get())
    #Maths=int(inputbox3.get())
    #Science=int(inputbox4.get())
    #Social=int(inputbox5.get())
    Sno=int(inputbox6.get())

    con=mysqlfunction()
    result=con.cursor()
    statem="UPDATE studentmarklist set Tamil=(%s) where sno=(%s)" 
    values=(Tamil,Sno)
    result.execute(statem,values)
    con.commit()
    print(result.rowcount,"row update")

def deleterow():
    
    Sno=int(inputbox6.get())

    con=mysqlfunction()
    result=con.cursor()
    statem="delete from studentmarklist where sno=(%s);" 
    values=(Sno,)
    result.execute(statem,values)
    con.commit()
    print(result.rowcount,"row delete")


Labeltitle=Label(app,text="Studentmarklist",bg="orange",fg="blue",font=("Comic Sans MS",13))
Labeltitle.grid(row=0,column=3,padx=30,pady=30)


Labeltitle=Label(app,text="Tamil",font=("Sitka Text",13))
Labeltitle.grid(row=1,column=2,padx=20,pady=20)

inputbox1=Entry(app,width=10)
inputbox1.grid(row=1,column=3)

Labeltitle=Label(app,text="English",font=("Sitka Text",13))
Labeltitle.grid(row=2,column=2,padx=20,pady=20)

inputbox2=Entry(app,width=10)
inputbox2.grid(row=2,column=3)

Labeltitle=Label(app,text="Maths",font=("Sitka Text",13))
Labeltitle.grid(row=3,column=2,padx=20,pady=20)

inputbox3=Entry(app,width=10)
inputbox3.grid(row=3,column=3)

Labeltitle=Label(app,text="Science",font=("Sitka Text",13))
Labeltitle.grid(row=4,column=2,padx=20,pady=20)

inputbox4=Entry(app,width=10)
inputbox4.grid(row=4,column=3)

Labeltitle=Label(app,text="Social",font=("Sitka Text",13))
Labeltitle.grid(row=5,column=2,padx=20,pady=20)

inputbox5=Entry(app,width=10)
inputbox5.grid(row=5,column=3)

Labeltitle=Label(app,text="Sno",font=("Sitka Text",13))
Labeltitle.grid(row=6,column=2,padx=20,pady=20)

inputbox6=Entry(app,width=10)
inputbox6.grid(row=6,column=3)


clickme=Button(app,text="insert",bg="blue",command=insertrow)
clickme.grid(row=7,column=1,padx=20,pady=20)
clickme=Button(app,text="update",bg="pink",command=updaterow)
clickme.grid(row=7,column=2,padx=20,pady=20)
clickme=Button(app,text="delete",bg="maroon",command=deleterow)
clickme.grid(row=7,column=3,padx=20,pady=20)
clickme=Button(app,text="reset",bg="red")
clickme.grid(row=7,column=4,padx=20,pady=20)


app.mainloop()
from tkinter import *
import mysql.connector

win=Tk()

win.title("Insert into MySQL DB Demo")
win.geometry("500x500")

class framefunction():
    def __init__(self):
        frametop=Frame(win,bg="black",width=800,height=300,padx=10,pady=10)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT",command=self.frameleft ).pack(padx=10, pady=10)
        btnupdate=Button(frametop,text="UPDATE" ).pack(padx=10, pady=10)
        btndelete=Button(frametop,text="DELETE").pack(padx=10, pady=10)
    
    
        
    def frameleft(self):

        newwin=Tk()
        newwin.title("Insert Window")
        newwin.geometry("500x500")
        
        frameleft=Frame(newwin,bg="black",width=500,height=500,padx=30,pady=30)
        frameleft.pack(padx = 100, pady = 100)

        #frameright=Frame(win,bg="red",width=500,height=500)
        #frameright.pack(side=RIGHT)

        lbl_Title_of_Operation=Label(frameleft,text="Insert into MySQL DB Demo")
        lbl_Title_of_Operation.grid(row=0,columnspan=5)

        lblName=Label(frameleft,text="Name")
        lblName.grid(row=2,column=1,padx=30,pady=10)

        lblJothika=Label(frameleft,text="Jothika")
        lblJothika.grid(row=3,column=1,padx=30,pady=10)

        newwin.mainloop()

run=framefunction()



win.mainloop()
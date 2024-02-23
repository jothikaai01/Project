from tkinter import *
import mysql.connector

win=Tk()

win.title("Delete into MySQL DB Demo")
win.geometry("500x500")

class framefunction():
    def __init__(self):
        frametop=Frame(win,bg="black",width=800,height=300,padx=10,pady=10)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT" ).pack(padx=10, pady=10)
        btnupdate=Button(frametop,text="UPDATE" ).pack(padx=10, pady=10)
        btndelete=Button(frametop,text="DELETE",command=self.framedelete ).pack(padx=10, pady=10)
    
    
        
    def framedelete(self):

        newwin=Tk()
        newwin.title("Delete Window")
        newwin.geometry("500x500")
        
        #frameleft=Frame(newwin,bg="black",width=500,height=500,padx=30,pady=30)
        #frameleft.pack(side=LEFT)

        #frameright=Frame(newwin,bg="red",width=500,height=500)
        #frameright.pack(side=RIGHT)

        framedelete=Frame(newwin,bg="blue",width=500)
        framedelete.pack(padx = 100, pady = 100)

        lbl_Title_of_Operation=Label(framedelete,text="Delete into MySQL DB Demo")
        lbl_Title_of_Operation.grid(row=0,columnspan=5)

        lblName=Label(framedelete,text="Name")
        lblName.grid(row=2,column=1,padx=30,pady=10)

        lblJothika=Label(framedelete,text="Jothika")
        lblJothika.grid(row=3,column=1,padx=30,pady=10)

        newwin.mainloop()

run=framefunction()



win.mainloop()
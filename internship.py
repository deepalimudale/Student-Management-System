from tkinter import*
from tkinter import ttk

import tkinter.messagebox
import dbinternship
from PIL import ImageTk,Image
import re
import datetime


root=Tk()
root.title("STUDENT DATABASE MANAGEMENT SYSTEM")
root.geometry("500x500")
canvas = Canvas(width=5000,height=5000)
canvas.place(x=0,y=0)
image=Image.open("internship\studentt.png")
photo = ImageTk.PhotoImage(image)
canvas.create_image(0,0,anchor=NW,image=photo)

StdID=StringVar()
Name=StringVar()
Address=StringVar()
Contact=StringVar()
Age=StringVar()
Gender=StringVar()
DOB=StringVar()
Branch=StringVar()
Semester=StringVar()
max_length=10
def validate( *args):
    if not Contact.get().isdigit():
        
        corrected = ''.join(filter(str.isdigit, Contact.get()))
        Contact.set(corrected)
def valid( *args):
    if not Name.get().isalpha():
        
        corrected = ''.join(filter(str.isalpha, Name.get()))
        Name.set(corrected)
        
        
        
def contact(*args):

        s=Contact.get()
        if len(s)>max_length:
            Contact.set(s[:max_length])
    
    
    


header=Label (root, text="STUDENT DATABASE MANAGEMENT SYSTEM", font=("arial",30,"bold"), fg="black").pack()
L1 = Label (root, text = "StdID", font=("arial", 16),bg="light sky blue").place(x=10,y=120)
L2 = Label (root, text = "Name", font=("arial", 16),bg="light sky blue").place(x=10,y=170)
L3 = Label (root, text = "Address", font=("arial", 16),bg="light sky blue").place(x=10,y=220)
L4 = Label (root, text = "Contact", font=("arial", 16),bg="light sky blue").place(x=10,y=270)
L5 = Label (root, text = "Age", font=("arial", 16),bg="light sky blue").place(x=10,y=320)
L6 = Label (root, text = "Gender", font=("arial", 16),bg="light sky blue").place(x=10,y=370)
L7 = Label (root, text = "DOB dd/mm/yyyy:", font=("arial", 16),bg="light sky blue").place(x=10,y=420)
L8 = Label (root, text = "Branch", font=("arial", 16),bg="light sky blue").place(x=10,y=490)
L9 = Label (root, text = "Semster", font=("arial", 16),bg="light sky blue").place(x=10,y=560)






DataFrameRight=LabelFrame(root,bd=2,width=450,height=300)
DataFrameRight.place(x=700,y=150)

StdIDT = Entry(root, textvariable=StdID,bd=5)
StdIDT.place(x=220,y=120)
NameT = Entry(root, textvariable=Name,bd=5)
NameT.place(x=220,y=170)
Name.trace("w",valid)

AddressT = Entry(root, textvariable=Address,bd=5)
AddressT.place(x=220,y=220)

ContactT = Entry(root, textvariable=Contact,bd=5)
ContactT.place(x=220,y=270)
Contact.trace("w",validate)
Contact.trace("w",contact)


AgeT = Spinbox(root, textvariable=Age,from_=1,to=100,bd=5)
AgeT.place(x=220,y=320)

R1 = Radiobutton(root, text = "Male", variable = Gender, value = "Male")
R1.place( x=220,y=370 )

R2 = Radiobutton(root, text = "Female", variable = Gender, value = "Female")
R2.place( x=320,y=370 )

R3 = Radiobutton(root, text = "Other", variable = Gender, value = "Other")
R3.place(x=420,y=370)
        
DOBT = Entry (root,textvariable=DOB,bd=5)
DOBT.place(x=220,y=420)
course=["Computer","Civil","Electronics and communnication","Electrical","Mechanical","Information Technology","Chemical","Mechatronics"]
BranchT = ttk.Combobox(root, textvariable=Branch,width=15,values=course)
BranchT.place(x=220,y=490)
BranchT.current(0)
sem=["1","2","3","4","5","6","7","8"]
SemesterT = ttk.Combobox(root, textvariable=Semester,width=15,values=sem)
SemesterT.place(x=220,y=560)
SemesterT.current(0)



        
sb1 = Scrollbar(DataFrameRight)
sb1.pack(side=RIGHT,fill=Y)
list1=Listbox(DataFrameRight,height=20,width=60,font=('arial',12,'bold'),bg="misty rose",yscrollcommand=sb1.set)
list1.pack(side=LEFT,fill=BOTH)
list1.bind('<<ListboxSelect>>')
sb1.config(command=list1.yview)
   

class students:
    def __init__(self, root):
        self.root = root
        B=tkinter.Button(root, text = "Add New",font=("arial",16,"bold"),command=self.add,bd='5',bg="red")
        B.place(x =10,y = 640)
        B=tkinter.Button(root, text = "Update",font=("arial",16,"bold"),command=self.update,bd='5',bg="yellow")
        B.place(x =180,y = 640)
        B=tkinter.Button(root, text = "Search",font=("arial",16,"bold"),command=self.search,bd='5',bg="blue")
        B.place(x =350,y = 640)
        B=tkinter.Button(root, text = "Delete",font=("arial",16,"bold"),command=self.delete,bd='5',bg="green")
        B.place(x =520,y = 640)
        B=tkinter.Button(root, text = "show",font=("arial",16,"bold"),command=self.show,bd='5',bg="pink")
        B.place(x =690,y = 640)
        B=tkinter.Button(root, text = "Exit",font=("arial",16,"bold"),command=self.exit,bd='5',bg="orange")
        B.place(x =860,y = 640)


    def exit(self):
        exit=tkinter.messagebox.askyesno("Student Database Management System","confirm if you want to exit")
        if exit>0:
            root.destroy()
            return
    def destroyee(self):
        StdIDT.delete(first=0,last=22)
        NameT.delete(first=0,last=22)
        AddressT.delete(first=0,last=22)
        ContactT.delete(first=0,last=22)
        AgeT.delete(first=0,last=22)
        DOBT.delete(first=0,last=22)
        BranchT.delete(first=0,last=22)
        SemesterT.delete(first=0,last=22)
   

    def add(self):      
        dbinternship.insert(StdID.get(),Name.get(),Address.get(),Contact.get(),Age.get(),Gender.get(),DOB.get(),Branch.get(),Semester.get())
        list1.delete(0,END)
        list1.insert(END ,StdID.get(),Name.get(),Address.get(),Contact.get(),Age.get(),Gender.get(),DOB.get(),Branch.get(),Semester.get())
        self.show()
        self.destroyee()
        add=tkinter.messagebox.showinfo("Success", "Data Saved Successfully.")

        
   
          
    def search(self):
        list1.delete(0,END)
        
            
        for i in  dbinternship.search(StdID.get(),Name.get(), Address.get(),Contact.get(),Age.get(),Gender.get(),DOB.get(),Branch.get(),Semester.get()):
                list1.insert(END,i,str(""))
                self.destroyee()
        
    
    def show(self):
        dbinternship.show()
        list1.delete(0,END)
        for i in dbinternship.show():
            list1.insert(END,i)

        
    def update(self):
        global sd

        try:
            index= list1.curselection()[0]
            
            sd = list1.get(index)
            
            dbinternship.update(sd[0],StdID.get(),Name.get(),Address.get(),Contact.get(),Age.get(),Gender.get(),DOB.get(),Branch.get(),Semester.get())

        except IndexError:
            pass                
        self.show()
        self.destroyee()


        

    def delete(self):
        global sd
        try:
            
            index= list1.curselection()[0]
            sd = list1.get(index)
            dbinternship.delete(sd[0])
            StdIDT.delete(0, END)
            StdIDT.insert(END,sd[1])
            
            NameT.delete(0,END)
            NameT.insert(END,sd[2])
            AddressT.delete(0, END)
            AddressT.insert(END,sd[3])
            ContactT.delete(0, END)
            ContactT.insert(END,sd[4])
            AgeT.delete(0, END)
            AgeT.insert(END,sd[5])
            DOBT.delete(0, END)
            DOBT.insert(END,sd[7])
            BranchT.delete(0, END)
            BranchT.insert(END,sd[8])
            SemesterT.delete(0, END)
            SemesterT.insert(END,sd[9])

        except IndexError:
            pass
         


        self.show()
        self.destroyee()
        

         
        
application =students(root)
root.mainloop()
        

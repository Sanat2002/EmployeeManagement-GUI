# GUI USING MONODB DATABASE
from tkinter import 
import time
import os
import tkinter.messagebox as tmsg
import pymongo
    

if __name__ == '__main__':

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['try_pymongo']
    collection = db["my_sample_collection"]


    root = Tk()
    root.title("EMPLOYEE MANAGEMENT SYSTEM")
    root.geometry("800x780")
    root.minsize(700,780)

    # Heading - label
    l = Label(root,text="EMPLOYEE MANAGEMENT SYSTEM",font="Helvetica 20 bold",fg="blue",pady=5)
    l.pack()

    # canvas for line
    c = Canvas(root,width=800,height=10)
    c.pack()
    c.create_line(0,6,800,6)

    # Frame
    f = Frame(root,borderwidth=5,relief=GROOVE)
    f.pack(pady=10)
    
    # adding labels to frame
    l = Label(f,text="EMPLOYEE ID",font="Times 14",padx=40)
    l.grid(row=1,padx=24,pady=10)
    
    l = Label(f,text="EMPLOYEE NAME",font="Times 14")
    l.grid(row=2,pady=20)

    l = Label(f,text="MOBILE",font="Times 14")
    l.grid(row=3,pady=20)

    l = Label(f,text="EMAIL",font="Times 14")
    l.grid(row=4,pady=20)

    l = Label(f,text="DEPARTMENT",font="Times 14")
    l.grid(row=5,pady=20)

    l = Label(f,text="DESIGINATION",font="Times 14")
    l.grid(row=6,pady=20)

    l = Label(f,text="SALARY",font="Times 14")
    l.grid(row=7,pady=20)
 
    status = StringVar()
    status.set("WELCOME....")
    l1 = Label(root,textvariable=status,anchor="w",font="lucida 10")
    l1.pack(side=BOTTOM,fill=X)

    # initializing variables
    id = StringVar()
    name = StringVar()
    mobile = StringVar()
    email = StringVar()
    d = StringVar()
    ds = StringVar()
    salary = StringVar()
    d.set("Select your department")
    ds.set("Select your desigination")

    # adding Entry widget
    e = Entry(f,textvariable=id,font="lucida 13")
    e.grid(row=1,column=2,padx=40,pady=10)
    
    e = Entry(f,textvariable=name,font="lucida 13")
    e.grid(row=2,column=2)

    e = Entry(f,textvariable=mobile,font="lucida 13")
    e.grid(row=3,column=2)

    e = Entry(f,textvariable=email,font="lucida 13")
    e.grid(row=4,column=2)

    e = Entry(f,textvariable=salary,font="lucida 13")
    e.grid(row=7,column=2)

    
    # adding optionmenu
    list1 = ['MGR','CLK','VP','PRES']
    op_menu = OptionMenu(f,d,*list1)
    op_menu.config(width=19,font="lucida 11")
    op_menu.grid(row=5,column=2)

    list2 = ['HR','IT','SALES','FIN']
    op_menu = OptionMenu(f,ds,*list2)
    op_menu.config(width=19,font="lucida 11")
    op_menu.grid(row=6,column=2)
    
    # commands
    def add():
        if (id.get() =="" or name.get()=="" or mobile.get()=="" or email.get()=="" or d.get()=="" or ds.get()=="" or salary.get()==""):
            status.set("PLEASE FILL UP ALL DETAILS....")
            l1.update()
            tmsg.showinfo("MESSAGE","PLEASE FILL UP ALL DETAILS....")
            time.sleep(2)
            status.set("WELCOME....")
            l1.update()
        else:
            a = True
            all_doc = collection.find()
            for doc in all_doc:
                if doc['emp_id'] == id.get():
                    status.set("SORRY,EMPLOYEE ALREADY EXISTS....")
                    l1.update()
                    tmsg.showerror("ERROR","SORRY,EMPLOYEE ALREADY EXISTS....")
                    time.sleep(2)
                    status.set("WELCOME....")
                    l1.update()
                    a = False
                    break

            if a:
                dic = {"emp_id":id.get(),"emp_name":name.get(),"mobile":mobile.get(),"email":email.get(),"department":d.get(),"desigination":ds.get(),"salary":salary.get()}
                collection.insert_one(dic)
                status.set("ADDING DETAILS....")
                l1.update()
                time.sleep(1)
                status.set("DETAILS ADDED....")
                l1.update()
                tmsg.showinfo("MESSAGE","DETAILS ADDED....")
                time.sleep(1)
                status.set("WELCOME....")
                l1.update()
    
    def delete():
        if (id.get()==""):
            status.set("PLEASE ENTER THE ID....")
            l1.update()
            tmsg.showinfo("MESSAGE","PLEASE ENTER THE ID....")
            status.set("WECOME....")
            l1.update()
        else:
            c = False
            deel = collection.delete_one({"emp_id":id.get()})
            if (deel.deleted_count > 0):
                c = True

            if c:
                status.set("DELETING DETAILS OF THE EMPLOYEE....")
                l1.update()
                time.sleep(1)
                status.set("DELETED....")
                l1.update()
                tmsg.showinfo("MESSAGE","DELETED....")
                time.sleep(1)
                status.set("WELCOME....")
                l1.update()
            else:
                status.set("EMPLOYEE NOT FOUND....")
                l1.update()
                tmsg.showerror("ERROR","EMPLOYEE NOT FOUND....")
                time.sleep(1)
                status.set("WELCOME....")
                l1.update()
     
    def update():
        if (id.get()==""):
            status.set("PLEASE ENTER THE ID....")
            l1.update()
            tmsg.showinfo("MESSAGE","PLEASE ENTER THE ID....")
            time.sleep(1)
            status.set("WELCOME....")
            l1.update()
        else:
            i = 0
            c = False
            to_up_dic = {"emp_id":id.get()}
            up_dic = {}

            if name.get()!="":
                up_dic.update({"emp_name":name.get()})
            if mobile.get()!="":
                up_dic.update({"mobile":mobile.get()})
            if email.get()!="":
                up_dic.update({"email":email.get()})
            if d.get()!="":
                up_dic.update({"department":d.get()})
            if ds.get()!="":
                up_dic.update({"desigination":ds.get()})
            if salary.get()!="":
                up_dic.update({"salary":salary.get()})

            up_count = collection.update_one(to_up_dic,{"$set":up_dic})
            if(up_count.modified_count>0):
                c = True

            if c:
                status.set("UPDATING DETAILS....")
                l1.update()
                time.sleep(2)
                status.set("DETAILS UPDATED....")
                l1.update()
                tmsg.showinfo("MESSAGE","DETAILS UPDATED....")
                time.sleep(1)
                status.set("WELCOME....")
                l1.update()
            else:
                status.set("EMPLOYEE NOT FOUND....")
                l1.update()
                tmsg.showerror("ERROR","EMPLOYEE NOT FOUND....")
                time.sleep(1)
                status.set("WELCOME....")
                l1.update()

    def clear():
        id.set("")
        name.set("")
        mobile.set("")
        email.set("")
        d.set("Select your department")
        ds.set("Select your desigination")
        salary.set("")
        status.set("CLEARED....")
        l1.update()
        tmsg.showinfo("MESSAGE","CLEARED....")
        time.sleep(1)
        status.set("WELCOME....")
    
    def exit():
        root.destroy()
    
    def clearfile():
        status.set("CLEARING FILE DATA....")
        l1.update()
        time.sleep(1)
        status.set("FILE CLEARED....")
        l1.update()
        tmsg.showinfo("MESSAGE","FILE CLEARED....")
        time.sleep(1)
        status.set("WELCOME")

        collection.delete_many({})
    
    # adding buttons
    b = Button(f,text="ADD RECORD",command=add,font="Times 13",padx=10)
    b.grid(row=8,pady=20)

    b = Button(f,text="DELETE RECORD",command=delete,font="Times 13")
    b.grid(row=8,column=2,pady=20)

    b = Button(f,text="UPDATE RECORD",command=update,font="Times 13")
    b.grid(row=9,pady=20)

    b = Button(f,text="CLEAR FILE",command=clearfile,font="Times 13",padx=20)
    b.grid(row=9,column=2,pady=20)

    b = Button(f,text="EXIT",command=exit,font="Times 13",padx=20)
    b.grid(row=10,pady=20)

    b = Button(f,text="CLEAR",command=clear,font="Times 13",padx=20)
    b.grid(row=10,column=2,pady=20)

    root.mainloop()

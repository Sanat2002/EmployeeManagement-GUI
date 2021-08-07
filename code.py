from tkinter import * 
import time
import os
import tkinter.messagebox as tmsg
    


if __name__ == '__main__':
    
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
            with open("file-1.txt","r") as f1:
                for lines in f1.readlines():
                    if (id.get()+'\n') in lines:
                        status.set("SORRY,EMPLOYEE ALREADY EXISTS....")
                        l1.update()
                        tmsg.showerror("ERROR","SORRY,EMPLOYEE ALREADY EXISTS....")
                        time.sleep(2)
                        status.set("WELCOME....")
                        l1.update()
                        a = False
                        break
            if a:
                with open("file-1.txt","a") as f:
                    f.write("\n************************************************************\n")
                    f.write(f"EMPLOYEE ID : {id.get()}\n")
                    f.write(f"EMPLOYEE NAME : {name.get()}\n")
                    f.write(f"MOBILE : {mobile.get()}\n")
                    f.write(f"EMAIL : {email.get()}\n")
                    f.write(f"DEPARTMENT : {d.get()}\n")
                    f.write(f"DESIGINATION : {ds.get()}\n")
                    f.write(f"SALARY : {salary.get()}\n")
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
            time.sleep(1)
            status.set("WECOME....")
            l1.update()
        else:
            c = False
            with open("file-1.txt","r") as f:
                lines = f.readlines()
                i = 0 
                for j in range(len(lines)):
                    if i>(len(lines)-1):
                        break
                    if str(id.get()+'\n') == str(lines[i][14:len(lines[i])]):
                        i+=9
                        c = True
                    if i>(len(lines)-1):
                        break
                    with open("file-2.txt","a") as f1:
                        f1.write(lines[i])
                    i+=1
                f.close()
                f1.close()
            os.remove("file-1.txt")
            os.rename("file-2.txt","file-1.txt")
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
            with open("file-1.txt","r") as f:
                lines = f.readlines()
                for j in range(len(lines)):
                    if i>(len(lines)-1):
                        break
                    if (id.get()+'\n') == lines[i][14:len(lines[i])]:
                        print("hel")
                        with open("file-2.txt","a") as f1:
                            f1.write(f"{lines[i]}")
                            if name.get()!="":
                                f1.write(f"EMPLOYEE NAME : {name.get()}\n")
                            else:
                                f1.write(f"{lines[i+1]}")
                            if mobile.get()!="":
                                f1.write(f"MOBILE : {mobile.get()}\n")
                            else:
                                f1.write(f"{lines[i+2]}")
                            if email.get()!="":
                                f1.write(f"EMAIL : {email.get()}\n")
                            else:
                                f1.write(f"{lines[i+3]}")
                            if d.get()!="":
                                f1.write(f"DEPARTMENT : {d.get()}\n")
                            else:
                                f1.write(f"{lines[i+4]}")
                            if ds.get()!="":
                                f1.write(f"DESIGINATION : {ds.get()}\n")
                            else:
                                f1.write(f"{lines[i+5]}")
                            if salary.get()!="":
                                f1.write(f"SALARY : {salary.get()}\n")
                            else:
                                f1.write(f"{lines[i+6]}")
                        i+=7
                        c = True
                    if i>(len(lines)-1):
                        break
                    with open("file-2","a") as f1:    
                        f1.write(lines[i])
                    i+=1
            f.close()
            f1.close()
            os.remove("file-1.txt")
            os.rename("file-2.txt","file-1.txt")
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

        with open("file-1.txt","w") as f:
            f.write("")
    
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

import tkinter as tk
import gui_Basics_2 as g2
import pymysql
from tkinter import messagebox

conn =  pymysql.connect("localhost", "root", "nithish24", "attendance")
cur = conn.cursor()



def login():
    LecturerID = e1.get().strip()
    Password = e2.get().strip()
    
    if LecturerID == "" or Password == "" :
        messagebox.showinfo("INFO","Please fill in all the fields")
    else:
        conn =  pymysql.connect("localhost", "root", "nithish24", "attendance")
        cur = conn.cursor()
        query = "SELECT password FROM LECTURER WHERE lecturerID = "+LecturerID+";"
        cur.execute(query)
        row = cur.fetchone()
        if(row[0] == Password):
            global root
            root.destroy()
            g2.login_options()
            print("login successful")
            
        else:
            messagebox.showerror("ERROR","Password is incorrect")



root = tk.Tk()
root.title("attendance management")
root.state('zoomed')
frame = tk.Frame(root,width=300,height=1500)


l1 = tk.Label(root,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).pack()

fw = tk.Frame(frame,width=500)
l2 = tk.Label(fw,text="Lecturer Login",font=("Courier",20),pady=50).grid(row=0,column=0,columnspan=2)


l3 = tk.Label(fw,text="Lecturer ID",font=("Courier",20)).grid(row=1,column=0,sticky='w')
e1 = tk.Entry(fw,font=("Courier",15))
e1.grid(row=1,column=1,padx=50)
l4 = tk.Label(fw,text="Password",font=("Courier",20)).grid(row=2,column=0,sticky='w')
e2 = tk.Entry(fw,show='*',font=("Courier",15))
e2.grid(row=2,column=1,padx=50)

l5 = tk.Label(fw,text="",font=("Courier",20))
l5.grid(row=4,column=0,sticky='w')

b1 = tk.Button(fw,text="login",font=("Courier",20),command=login)
b1.grid(row=5,column=1,sticky='w')
fw.pack()
frame.pack()

root.mainloop()


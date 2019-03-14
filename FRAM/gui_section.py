import tkinter as tk
import pymysql
from tkinter import messagebox
def add_section():
    conn =  pymysql.connect("localhost", "root", "nithish24", "attendance")
    cur = conn.cursor()

    global r   
    r = tk.Tk()
    r.title("attendance management")
    r.state('zoomed')
    frame = tk.Frame(r)
    l1 = tk.Label(r,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).pack()
    l2 = tk.Label(r,text="ADD SECTION",pady=20,font=("Courier",30)).pack()
    l1 = tk.Label(frame,text="Section ID:",font=("Courier",20)).grid(row=0,column=0,sticky='w')
    l2 = tk.Label(frame,text="Section Name:",font=("Courier",20)).grid(row=1,column=0,sticky='w')


    e1 = tk.Entry(frame,font=("Courier",20))
    e1.grid(row=0,column=1)
    e2 = tk.Entry(frame,font=("Courier",20))
    e2.grid(row=1,column=1)
    

    l8 = tk.Label(frame,text=" ",font=("Courier",20),fg="#ff0000").grid(row=7,column=0,columnspan=2)
    def display():
        l8 = tk.Label(frame,text=" ",font=("Courier",20),fg="#ff0000").grid(row=7,column=0,columnspan=2)
        Section = e1.get().strip()
        Name = e2.get().strip()
        
        if Section == "" or Name == ""  :
            l8 = tk.Label(frame,text="Please fill in all the fields",font=("Courier",20)).grid(row=7,column=0,columnspan=2)
        else:
            conn =  pymysql.connect("localhost", "root", "nithish24", "attendance")
            cur = conn.cursor()
            query =  "INSERT INTO SECTION VALUES ('" + Section + "', '" + Name + "');"
            try:
                cur.execute(query)
                conn.commit()
                messagebox.showinfo("INFO","Section added sucessfully to the database")
                r.destroy()
            except:
                print("An exception occured")
            
    
    b1 = tk.Button(frame,text="submit",font=("Courier",20),command=display).grid(row=8,column=0,columnspan=2)

    
    cur.close()
    conn.close()

    frame.pack()
    r.mainloop()




import tkinter as tk
import pymysql
from tkinter import ttk
from tkinter import messagebox
def genrep():
    def disrep():
        
        conn =  pymysql.connect("localhost", "root", "nithish24", "attendance")
        cur = conn.cursor()
        sectionid = e1.get()
        subjectid = e2.get()
        hour = e3.get()
        date = e4.get()
    
        sid = "SectionID = " + str(sectionid)
        sbid = "SubjectID = "+ str(subjectid)
        hid = "Hour = " + str(hour)
        did = "Date = " + str(date)

        try:
            query1 = "CREATE VIEW ATTENDANCE_FOR_TODAY AS SELECT A.USN, S.stuName, A.status FROM ATTENDANCEDETAILS A, STUDENT S WHERE A.USN = S.USN AND A.sectionID="+str(sectionid)+ " AND subjectID = "+str(subjectid)+ " AND date_att='" + str(date)+"' AND hour_att ="+str(hour)+";"
            cur.execute(query1)
            conn.commit()
            query2 = "SELECT * FROM ATTENDANCE_FOR_TODAY;"
            cur.execute(query2)
            row = cur.fetchall()
            query3 = "DROP VIEW ATTENDANCE_FOR_TODAY;"
            cur.execute(query3)
            conn.commit()
            if (len(row) == 0):
                messagebox.showerror("ERROR","NO RECORDS TO DISPLAY.PLEASE ENTER THE VALID VALUES!")
                return
        except:
            print("something went wrong")


        root = tk.Tk()
        root.title("attendance management")
        root.state('zoomed')

        l1 = tk.Label(root,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).grid(row=0,column=4,padx=350)
        l2 = tk.Label(root,text="Displaying View",font=("Courier",30),pady=10).grid(row=1,column=4)
        l3 = tk.Label(root,text=sid,font=("Courier",20)).grid(row=2,column=4)
        l4 = tk.Label(root,text=sbid,font=("Courier",20)).grid(row=3,column=4)
        l5 = tk.Label(root,text=did,font=("Courier",20)).grid(row=4,column=4)
        l6 = tk.Label(root,text=hid,font=("Courier",20)).grid(row=5,column=4)
        l7 = tk.Label(root,text="",font=("Courier",30)).grid(row=6,column=4)
        l7 = tk.Label(root,text="",font=("Courier",30)).grid(row=8,column=4)
        def close():
            root.destroy()
            

        b1 = tk.Button(root,text="close",font=("Courier",20),command=close)
        b1.grid(row=9,column=4)

        treeview = tk.ttk.Treeview(root)    #create a table in form of tree
        treeview["columns"] = ["USN","Name","STATUS"] #important donot miss enter the colimn names
        treeview["show"] = "headings"   #without this their will be error

        treeview.heading("USN",text="USN")  #inorder of column name inserted above
        treeview.heading("Name",text="Name")
        treeview.heading("STATUS",text="STATUS")

        treeview.column('#1', width=90)     #adding numbering to columns 
        treeview.column('#2', stretch=tk.YES, minwidth=50, width=120)
        treeview.column('#3', stretch=tk.YES, minwidth=50, width=45)

        treeview.config(height=len(row))    #setting the height of tree
        treeview.grid(row=7,column=4)       #placing it on the window

        index = 0
        for row in row:
            treeview.insert("", index, index, values=row)   #inserting values into table if you wont get youtube it :(
            index =index + 1
            
        root.mainloop()

    rook = tk.Tk()
    rook.title("attendance management")
    rook.state('zoomed')
    frame = tk.Frame(rook,width=300,height=1500)


    l1 = tk.Label(rook,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).pack()

    frame = tk.Frame(rook)
    l2 = tk.Label(frame,text="Generate Report",font=("Courier",20),pady=50).grid(row=0,column=0,columnspan=2)
    l3 = tk.Label(frame,text="",font=("Courier",20)).grid(row=1,column=0,columnspan=2)
    l4 = tk.Label(frame,text="Section ID: ",font=("Courier",20)).grid(row=2,column=0,sticky='w')
    l5 = tk.Label(frame,text="Subject ID: ",font=("Courier",20)).grid(row=3,column=0,sticky='w')
    l6 = tk.Label(frame,text="Hour : ",font=("Courier",20)).grid(row=4,column=0,sticky='w')
    l7 = tk.Label(frame,text="Date : ",font=("Courier",20)).grid(row=5,column=0,sticky='w')

    e1 = tk.Entry(frame,font=("Courier",20),width=10)
    e1.grid(row=2,column=1)
    e2 = tk.Entry(frame,font=("Courier",20),width=10)
    e2.grid(row=3,column=1)
    e3 = tk.Entry(frame,font=("Courier",20),width=10)
    e3.grid(row=4,column=1)
    e4 = tk.Entry(frame,font=("Courier",20),width=10)
    e4.grid(row=5,column=1)
    
    l3 = tk.Label(frame,text="",font=("Courier",20)).grid(row=6,column=0,columnspan=2)
    b1 = tk.Button(frame,text="Submit",font=("Courier",20),width=10,command=disrep)
    b1.grid(row=7,column=0,columnspan=2)
    def closep():
        rook.destroy()
    l3 = tk.Label(frame,text="",font=("Courier",20)).grid(row=8,column=0,columnspan=2)
    b2 = tk.Button(frame,text="Close",font=("Courier",20),width=10,command=closep)
    b2.grid(row=9,column=0,columnspan=2)
    frame.pack()    
    rook.mainloop()



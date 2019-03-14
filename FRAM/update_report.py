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

        query = "SELECT USN,STATUS F FROM ATTENDANCEDETAILS A WHERE  A.sectionID="+str(sectionid)+ " AND subjectID = "+str(subjectid)+ " AND date_att='" + str(date)+"' AND hour_att ="+str(hour)+";"
        try:
            cur.execute(query)
            row = cur.fetchall()
            conn.commit()
            if (len(row) == 0):
                messagebox.showerror("ERROR","NO RECORDS TO DISPLAY.PLEASE ENTER THE VALID VALUES!")
                return
        except:
            print("something went wrong")
        

        root = tk.Tk()
        root.title("attendance management")
        root.state('zoomed')
        frame = tk.Frame(root,width=300,height=1500)


        l1 = tk.Label(root,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).pack()

        frame = tk.Frame(root)
        l2 = tk.Label(root,text="Update Attendance",font=("Courier",20)).pack()
        l3 = tk.Label(frame,text="",font=("Courier",20)).grid(row=0,column=0)
        l4 = tk.Label(frame,text=sid,font=("Courier",20)).grid(row=1,column=0,columnspan=2)
        l5 = tk.Label(frame,text=sbid,font=("Courier",20)).grid(row=2,column=0,columnspan=2)
        l6 = tk.Label(frame,text=hid,font=("Courier",20)).grid(row=3,column=0,columnspan=2)
        l7 = tk.Label(frame,text=did,font=("Courier",20)).grid(row=4,column=0,columnspan=2)
        l8 = tk.Label(frame,text="",font=("Courier",20)).grid(row=5,column=0,columnspan=2)
        l8 = tk.Label(frame,text="",font=("Courier",20)).grid(row=6,column=0,columnspan=2)
        def close():
            root.destroy()
            
        def update():
            c=0   
            for i in range(int(len(count)/2)):
                usnup = count[c].get().strip()
                status = count[c+1].get().strip()
                c=c+2
                try:
                    query = "UPDATE ATTENDANCEDETAILS SET STATUS=" + status + " WHERE USN='" +usnup+"' AND sectionID=" +  sectionid + " AND subjectID=" + subjectid + " AND hour_att=" + hour + " AND date_att='"+date+"';"
                    cur.execute(query)
                    conn.commit()
                except:
                    print(usnup)
                    print("something went wrong")
            messagebox.showinfo("INFO","UPDATED SUCCESSFULLY")
            close()
            

            
        l8 = tk.Label(frame,text="",font=("Courier",20)).grid(row=10,column=0,columnspan=2)
        b1 = tk.Button(frame,text="UPDATE",font=("Courier",20),command=update)
        b1.grid(row=11,column=0,columnspan=2)
        l8 = tk.Label(frame,text="",font=("Courier",20)).grid(row=12,column=0,columnspan=2)
        b2 = tk.Button(frame,text="close",font=("Courier",20),command=close)
        b2.grid(row=13,column=0,columnspan=2)

        l7 = tk.Label(frame,text="USN",font=("Courier",20)).grid(row=5,column=0)
        l8 = tk.Label(frame,text="STATUS",font=("Courier",20)).grid(row=5,column=1)
        count={}
        c=0
        for i in range(len(row)):
            for j in range(2):
                text1=row[i][j]
                count[c] = tk.Entry(frame,font=("Courier",20),width=10)
                count[c].grid(row=(6+i),column=j)
                count[c].insert("end",row[i][j])
                c=c+1
        
        frame.pack()
        rook.mainloop()

    rook = tk.Tk()
    rook.title("attendance management")
    rook.state('zoomed')
    frame = tk.Frame(rook,width=300,height=1500)


    l1 = tk.Label(rook,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).pack()

    frame = tk.Frame(rook)
    l2 = tk.Label(frame,text="Update Attendance",font=("Courier",20),pady=50).grid(row=0,column=0,columnspan=2)
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





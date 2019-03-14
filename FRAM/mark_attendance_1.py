import tkinter as tk
import pymysql
from tkinter import ttk
import upload_photo
import cv2
import face_recognize as fr





def genrep():
    def disrep(sectionid,subjectid,hour,date):
        root = tk.Tk()
        root.title("attendance management")
        root.state('zoomed')
        conn =  pymysql.connect("localhost", "root", "nithish24", "attendance")
        cur = conn.cursor()
        
        
        sid = "SectionID = " + str(sectionid)
        sbid = "SubjectID = "+ str(subjectid)
        hid = "Hour = " + str(hour)
        did = "Date = " + str(date)
    

        l1 = tk.Label(root,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).grid(row=0,column=4,padx=350)
        l2 = tk.Label(root,text="Attendance",font=("Courier",30),pady=10).grid(row=1,column=4)
        l3 = tk.Label(root,text=sid,font=("Courier",20)).grid(row=2,column=4)
        l4 = tk.Label(root,text=sbid,font=("Courier",20)).grid(row=3,column=4)
        l5 = tk.Label(root,text=did,font=("Courier",20)).grid(row=4,column=4)
        l6 = tk.Label(root,text=hid,font=("Courier",20)).grid(row=5,column=4)
        l7 = tk.Label(root,text="",font=("Courier",30)).grid(row=6,column=4)
        l7 = tk.Label(root,text="",font=("Courier",30)).grid(row=8,column=4)
        def close():
            root.destroy()


        try:
            query1 = "CREATE VIEW ATTENDANCE_FOR_TODAY AS SELECT A.USN, S.stuName, A.status FROM ATTENDANCEDETAILS A, STUDENT S WHERE A.USN = S.USN AND A.sectionID="+str(sectionid)+ " AND subjectID = "+str(subjectid)+ " AND date_att='" + str(date)+"' AND hour_att ="+str(hour)+";"
            cur.execute(query1)
            conn.commit()
            query2 = "SELECT * FROM ATTENDANCE_FOR_TODAY;"
            cur.execute(query2)
            row1 = cur.fetchall()
            query3 = "DROP VIEW ATTENDANCE_FOR_TODAY;"
            cur.execute(query3)
            conn.commit()
        except:
            print("something went wrong")

        treeview = tk.ttk.Treeview(root)
        treeview["columns"] = ["USN","Name","STATUS"]
        treeview["show"] = "headings"

        treeview.heading("USN",text="USN")
        treeview.heading("Name",text="Name")
        treeview.heading("STATUS",text="STATUS")

        treeview.column('#1', width=90)
        treeview.column('#2', stretch=tk.YES, minwidth=50, width=120)
        treeview.column('#3', stretch=tk.YES, minwidth=50, width=45)

        treeview.config(height=len(row1))
        treeview.grid(row=7,column=4)

        index = 0
        for row in row1:
            print(row)
            treeview.insert("", index, index, values=row)
            index =index + 1


        b1 = tk.Button(root,text="close",font=("Courier",20),command=close)
        b1.grid(row=9,column=4)   
        root.mainloop()
        

    
    def mark_attendance():
        conn = pymysql.connect('localhost', 'root', 'nithish24', 'attendance')
        cur = conn.cursor()
        ids = []
        usn_no = []

        sectionid = e1.get()
        subjectid = e2.get()
        hour = e3.get()
        date = e4.get()
        imgPath = "classPhoto/"+str(date)+str(sectionid)+str(subjectid)+str(hour)+".jpg"
        cam = cv2.VideoCapture(0)
        while True:
            red, im = cam.read()
            cv2.imshow("PRESS c TO CAPTURE", im)
            if(cv2.waitKey(1) & 0xFF == ord('c')):
                break
        
        cv2.imwrite(imgPath, im)
        cam.release()
        cv2.destroyAllWindows()

        query = "INSERT INTO CLASSPHOTO(imgPath, sectionID, subjectID, date_, hour) VALUES ('" + imgPath +"', '"+ str(sectionid) +"', '"+ str(subjectid) +"', '"+ str(date) +"', '"+ str(hour) + "')"
        cur.execute(query)
        conn.commit()

        query = "SELECT imgPath FROM CLASSPHOTO WHERE sectionID =" + sectionid + " AND subjectID =" + subjectid + " AND date_ ='" + str(date) + "' AND hour =" + hour + ";"

        cur.execute(query)
        row = cur.fetchone()
        print(row)
        ids = fr.face_recognize(row[0])
        print(ids)

        #corresponding USN fetch
        for i in range(len(ids)):
            query1 = "SELECT USN FROM TRAINIMAGES WHERE label = " + str(ids[i]) + ";"
            cur.execute(query1)
            wow = cur.fetchone()
            usn_no.append(wow[0])
        print(usn_no)

        for usn in usn_no:
            print(usn)
            query2 = "INSERT INTO ATTENDANCEDETAILS VALUES('" + usn + "', '"+ sectionid + "', '"+ subjectid + "', '"+ str(date) + "', '"+ hour + "', '" + "1" + "');"
            print(query2)
            cur.execute(query2)
            conn.commit()

        cur.close()
        conn.close()
        disrep(sectionid,subjectid,hour,date)
        
        
        


    
    rook = tk.Tk()
    rook.title("attendance management")
    rook.state('zoomed')
    frame = tk.Frame(rook,width=300,height=1500)


    l1 = tk.Label(rook,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).pack()

    frame = tk.Frame(rook)
    l2 = tk.Label(frame,text="Mark Attendance",font=("Courier",20),pady=50).grid(row=0,column=0,columnspan=2)
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
   
    
    l3 = tk.Label(frame,text="",font=("Courier",20)).grid(row=7,column=0,columnspan=2)
    b1 = tk.Button(frame,text="Submit",font=("Courier",20),width=10,command=mark_attendance)
    b1.grid(row=8,column=0,columnspan=2)
    def closep():
        rook.destroy()
    l3 = tk.Label(frame,text="",font=("Courier",20)).grid(row=9,column=0,columnspan=2)
    b2 = tk.Button(frame,text="Close",font=("Courier",20),width=10,command=closep)
    b2.grid(row=10,column=0,columnspan=2)
    frame.pack()    
    rook.mainloop()




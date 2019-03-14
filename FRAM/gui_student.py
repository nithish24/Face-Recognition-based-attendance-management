import tkinter as tk
import pymysql
from tkinter import messagebox
import dataSetGenerator
import trainer
import cv2,os
import numpy as np
from PIL import Image 




def add_student():


    def display():
        l8 = tk.Label(frame,text=" ",font=("Courier",20),fg="#ff0000").grid(row=7,column=0,columnspan=2)
        USN = e1.get().strip()
        Name = e2.get().strip()
        Dob = e3.get().strip()
        Address = e4.get().strip()
        Phone = e5.get().strip()
        SectionID = e6.get().strip()
        Email = e7.get().strip()
        if USN == "" or Name == "" or Dob == "" or Address  =="" or Phone == "" or SectionID == "" or Email == "" :
            l8 = tk.Label(frame,text="Please fill in all the fields",font=("Courier",20)).grid(row=7,column=0,columnspan=2)
        else:
            conn =  pymysql.connect("localhost", "root", "nithish24", "attendance")
            cur = conn.cursor()
            query =  "INSERT INTO STUDENT VALUES ('" + USN + "', '" + Name + "', '" + Dob + "', '" + Address + "', '" + Phone + "', '" + SectionID + "', '" + Email + "');"
            cur.execute(query)
            conn.commit()
            dataSetGenerator.create_training_data(USN, SectionID)
            trainer.train()
            messagebox.showinfo("INFO","Student added sucessfully to the database")
            r.destroy()
            
                
            

    conn =  pymysql.connect("localhost", "root", "nithish24", "attendance")
    cur = conn.cursor()
    global r
    r = tk.Tk()
    r.title("attendance management")
    r.state('zoomed')
    frame = tk.Frame(r)
    l1 = tk.Label(r,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).pack()
    l2 = tk.Label(r,text="ADD STUDENT",pady=20,font=("Courier",30)).pack()
    l1 = tk.Label(frame,text="USN:",font=("Courier",20)).grid(row=0,column=0,sticky='w')
    l2 = tk.Label(frame,text="Student Name:",font=("Courier",20)).grid(row=1,column=0,sticky='w')
    l3 = tk.Label(frame,text="DOB(YYYY-MM-DD):",font=("Courier",20)).grid(row=2,column=0,sticky='w')
    l4 = tk.Label(frame,text="Addres:",font=("Courier",20)).grid(row=3,column=0,sticky='w')
    l5 = tk.Label(frame,text="Phone No. :",font=("Courier",20)).grid(row=4,column=0,sticky='w')
    l6 = tk.Label(frame,text="SectionID:",font=("Courier",20)).grid(row=5,column=0,sticky='w')
    l7 = tk.Label(frame,text="Email ID:",font=("Courier",20)).grid(row=6,column=0,sticky='w')
    e1 = tk.Entry(frame,font=("Courier",20))
    e1.grid(row=0,column=1)
    e2 = tk.Entry(frame,font=("Courier",20))
    e2.grid(row=1,column=1)
    e3 = tk.Entry(frame,font=("Courier",20))
    e3.grid(row=2,column=1)
    e4 = tk.Entry(frame,font=("Courier",20))
    e4.grid(row=3,column=1)
    e5 = tk.Entry(frame,font=("Courier",20))
    e5.grid(row=4,column=1)
    e6 = tk.Entry(frame,font=("Courier",20))
    e6.grid(row=5,column=1)
    e7 = tk.Entry(frame,font=("Courier",20))
    e7.grid(row=6,column=1)
    l8 = tk.Label(frame,text=" ",font=("Courier",20),fg="#ff0000").grid(row=7,column=0,columnspan=2)
    b1 = tk.Button(frame,text="submit",font=("Courier",20),command=display).grid(row=8,column=0,columnspan=2)
    frame.pack()
    cur.close()
    conn.close()
    r.mainloop()




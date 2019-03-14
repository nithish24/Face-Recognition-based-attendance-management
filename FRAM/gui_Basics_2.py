import tkinter as tk
import gui_Basics_3 as g3
import fill_up as fp
import mark_attendance_1 as ma1
import update_report as up



def login_options():
    r = tk.Tk()
    r.title("attendance management")
    r.state('zoomed')
    frame = tk.Frame(r)
    l1 = tk.Label(r,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).pack()
    l2 = tk.Label(r,text="WELCOME",pady=20,font=("Courier",25)).pack(side='top')
    b1 = tk.Button(frame,text="Mark Attendance",font=("Courier",20),command=ma1.genrep)
    b1.grid(row=0,column=0)
    l1 = tk.Label(frame,text="",font=("Courier",10))
    l1.grid(row=1,column=0)
    b2 = tk.Button(frame,text="Generate Report",font=("Courier",20),command=fp.genrep)
    b2.grid(row=2,column=0)
    l2 = tk.Label(frame,text="",font=("Courier",10))
    l2.grid(row=3,column=0)
    b3 = tk.Button(frame,text="Update Attendance",font=("Courier",20),command=up.genrep)
    b3.grid(row=4,column=0)
    l3 = tk.Label(frame,text="",font=("Courier",10))
    l3.grid(row=5,column=0)
    b4 = tk.Button(frame,text="Insert Values into tables",font=("Courier",20),command=g3.options)
    b4.grid(row=6,column=0)
    l4 = tk.Label(frame,text="",font=("Courier",10))
    l4.grid(row=7,column=0)
    frame.pack()
    r.mainloop()




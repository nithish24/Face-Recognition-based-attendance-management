import tkinter as tk
import gui_student as gs
import gui_lecturer as gl
import gui_section as gsc
import gui_subject as gsb

def options():

    def close():
        r.destroy()
    
    r = tk.Tk()
    r.title("attendance management")
    r.state('zoomed')
    l1 = tk.Label(r,text="ATTENDANCE MANAGEMENT",pady=20,font=("Courier",44)).pack()
    frame = tk.Frame(r)
    b1 = tk.Button(frame,text="Add Student",font=("Courier",20),command=gs.add_student)
    b1.grid(row=0,column=0,sticky='w')
    l1 = tk.Label(frame,text="",font=("Courier",10))
    l1.grid(row=1,column=0,sticky='w')
    b2 = tk.Button(frame,text="Add Lecturer",font=("Courier",20),command=gl.add_lecturer)
    b2.grid(row=2,column=0,sticky='w')
    l2 = tk.Label(frame,text="",font=("Courier",10))
    l2.grid(row=3,column=0,sticky='w')
    b3 = tk.Button(frame,text="Add Subject",font=("Courier",20),command=gsb.add_subject)
    b3.grid(row=4,column=0,sticky='w')
    l3 = tk.Label(frame,text="",font=("Courier",10))
    l3.grid(row=5,column=0,sticky='w')
    b4 = tk.Button(frame,text="Add Section",font=("Courier",20),command=gsc.add_section)
    b4.grid(row=6,column=0,sticky='w')
    l4 = tk.Label(frame,text="",font=("Courier",10))
    l4.grid(row=7,column=0,sticky='w')
    b4 = tk.Button(frame,text="Close",font=("Courier",20),command=close)
    b4.grid(row=8,column=0)
    frame.pack()
    r.mainloop()




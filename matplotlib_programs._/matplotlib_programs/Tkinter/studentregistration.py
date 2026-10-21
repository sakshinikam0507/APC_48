
import tkinter as tk
from tkinter import messagebox
def register():
    name=name_entry.get()
    roll=roll_entry.get()
    course=course_entry.get()
    gender=gender_var.get()
    if name=="" or roll=="" or course=="" or gender=="":
        messagebox.showwarning("Warning","Please fill all fields")
    else:
        messagebox.showinfo("Registration Successful",f"Name: {name}\nRoll No: {roll}\nCourse: {course}\nGender: {gender}")
root=tk.Tk()
root.title("Student Registration Form")
root.geometry("350x350")
tk.Label(root,text="Student Registration Form",font=("Arial",16,"bold")).pack(pady=10)
tk.Label(root,text="Student Name").pack()
name_entry=tk.Entry(root)
name_entry.pack()
tk.Label(root,text="Roll Number").pack()
roll_entry=tk.Entry(root)
roll_entry.pack()
tk.Label(root,text="Course").pack()
course_entry=tk.Entry(root)
course_entry.pack()
tk.Label(root,text="Gender").pack()
gender_var=tk.StringVar()
tk.Radiobutton(root,text="Male",variable=gender_var,value="Male").pack()
tk.Radiobutton(root,text="Female",variable=gender_var,value="Female").pack()
tk.Button(root,text="Register",command=register).pack(pady=15)
root.mainloop()
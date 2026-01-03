import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from pymongo import MongoClient
import cv2
import os
import numpy as np
from datetime import datetime
from time import strftime
import csv
from tkinter import filedialog

mydata=[]
class attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Training")
        self.root.geometry("1530x790+0+0")

        # text variables
        self.var_attend_id=tk.StringVar()
        self.var_attend_roll=tk.StringVar()
        self.var_attend_name=tk.StringVar()
        self.var_attend_dep=tk.StringVar()
        self.var_attend_time=tk.StringVar()
        self.var_attend_date=tk.StringVar()
        self.var_attend_status=tk.StringVar()

        title_label = tk.Label(self.root, text="Attendance System", font=("times new roman", 35, "bold"),bg="white",fg="blue")
        title_label.place(x=0, y=0, width=1530, height=55)

        main_frame = tk.Frame(self.root, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=800)

        # Left Label
        Left_frame = tk.LabelFrame(
            main_frame,
            bd=2,
            text="Attendance Details",
            bg="white",
            relief=tk.RIDGE,
            font=("times new roman", 12, "bold")
        )
        Left_frame.place(x=10, y=10, width=720, height=780)

        left_inside_frame = tk.Frame(Left_frame, bd=2, relief=tk.RIDGE, bg="white")
        left_inside_frame.place(x=0, y=0, width=715, height=650)

        #label and entry
        attendance_id_label = tk.Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        attendance_id_entry = tk.Entry(left_inside_frame, width=20, textvariable=self.var_attend_id,font=("times new roman", 12, "bold"))
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        roll_no_label = tk.Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)
        roll_no_entry = tk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_roll, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=0, column=3, padx=10, pady=10, sticky=tk.W)

        name_label = tk.Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        name_entry = tk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        department_label = tk.Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)
        department_entry = tk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_dep, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=10, sticky=tk.W)

        time_label = tk.Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)
        time_entry = tk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=3, padx=10, pady=10, sticky=tk.W)

        date_label= tk.Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        date_entry = tk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        

        attendance_label = tk.Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        attendance_combo = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"),textvariable=self.var_attend_status, state="readonly", width=18)
        attendance_combo["values"] = ("Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
        

        #buttons frame
        btn_frame = tk.Frame(left_inside_frame, bd=2, relief=tk.RIDGE, bg="white")
        btn_frame.place(x=0, y=400, width=710, height=50)
        import_btn = tk.Button(btn_frame, text="Import CSV",command=self.import_csv, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0, padx=10, pady=10)
        export_btn = tk.Button(btn_frame, text="Export CSV", command=self.export_csv,width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1, padx=10, pady=10)
        update_btn = tk.Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=10, pady=10)
        reset_btn = tk.Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=10, pady=10)


        # Right Label
        Right_frame = tk.LabelFrame(
            main_frame,
            bd=2,
            text="Attendance Panel",
            bg="white",
            relief=tk.RIDGE,
            font=("times new roman", 12, "bold")
        )
        Right_frame.place(x=740, y=10, width=720, height=780)

        table_frame = tk.Frame(Right_frame, bd=2, relief=tk.RIDGE, bg="white")
        table_frame.place(x=0, y=0, width=715, height=650)
        scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)  
        self.attendance_table = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)
        self.attendance_table.heading("id", text="Attendance ID")
        self.attendance_table.heading("roll", text="Roll No")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("department", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table["show"] = "headings"
        self.attendance_table.column("id", width=100)
        self.attendance_table.column("roll", width=100)
        self.attendance_table.column("name", width=100)
        self.attendance_table.column("department", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("status", width=100)
        self.attendance_table.pack(fill=tk.BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)
        
    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("", tk.END, values=i)

    #===========import csv================        

    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)


    #===========export csv================        
    def export_csv(self):
        try:
            if  len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            if not fln:
                return 
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported", "Your data has been exported to " + os.path.basename(fln) + " successfully")   
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)     


    def get_cursor(self, event=""):
        cursor_row = self.attendance_table.focus()
        if not cursor_row:
            return

        content = self.attendance_table.item(cursor_row)
        data = content.get("values", [])
    # 🛑 SAFETY CHECK
        if len(data) < 7:
            return

        self.var_attend_id.set(data[0])
        self.var_attend_roll.set(data[1])
        self.var_attend_name.set(data[2])
        self.var_attend_dep.set(data[3])
        self.var_attend_time.set(data[4])
        self.var_attend_date.set(data[5])
        self.var_attend_status.set(data[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_status.set("")      

    def update_data(self):
        selected = self.attendance_table.focus()

        if not selected:
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
            return

        updated_row = (
            self.var_attend_id.get(),
            self.var_attend_roll.get(),
            self.var_attend_name.get(),
            self.var_attend_dep.get(),
            self.var_attend_time.get(),
            self.var_attend_date.get(),
            self.var_attend_status.get()
        )
        if "" in updated_row or self.var_attend_status.get() == "Status":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        # Update Treeview
        self.attendance_table.item(selected, values=updated_row)

        # Update mydata list
        selected_index = self.attendance_table.index(selected)
        mydata[selected_index] = list(updated_row)

        messagebox.showinfo("Success", "Attendance updated successfully", parent=self.root)

if __name__ == "__main__":
     root = tk.Tk() 
     app = attendance(root)
     root.mainloop()
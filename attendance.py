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


class attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Training")
        self.root.geometry("1530x790+0+0")

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
        attendance_id_entry = tk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        roll_no_label = tk.Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)
        roll_no_entry = tk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=0, column=3, padx=10, pady=10, sticky=tk.W)

        name_label = tk.Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        name_entry = tk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        department_label = tk.Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W)
        department_entry = tk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=10, sticky=tk.W)

        time_label = tk.Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)
        time_entry = tk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=3, padx=10, pady=10, sticky=tk.W)

        date_label= tk.Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        date_entry = tk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        

        attendance_label = tk.Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        attendance_combo = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="readonly", width=18)
        attendance_combo["values"] = ("Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
        

        #buttons frame
        btn_frame = tk.Frame(left_inside_frame, bd=2, relief=tk.RIDGE, bg="white")
        btn_frame.place(x=0, y=400, width=710, height=50)
        import_btn = tk.Button(btn_frame, text="Import CSV", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0, padx=10, pady=10)
        export_btn = tk.Button(btn_frame, text="Export CSV", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1, padx=10, pady=10)
        update_btn = tk.Button(btn_frame, text="Update", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=10, pady=10)
        reset_btn = tk.Button(btn_frame, text="Reset", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
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
        


if __name__ == "__main__":
    root = tk.Tk()
    app = attendance(root)
    root.mainloop()  
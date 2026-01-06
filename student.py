import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
# from pymongo import MongoClient
import sqlite3
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # Register validation for integers
        vcmd = (self.root.register(self.only_numbers), "%S")
        #variables

        self.var_department=tk.StringVar()
        self.var_course=tk.StringVar()
        self.var_year=tk.StringVar()
        self.var_semester=tk.StringVar()
        self.var_std_id=tk.StringVar()
        self.var_std_name=tk.StringVar()
        self.var_div=tk.StringVar()
        self.var_roll=tk.StringVar()
        self.var_gender=tk.StringVar()
        self.var_dob=tk.StringVar()
        self.var_email=tk.StringVar()
        self.var_phone=tk.StringVar()
        self.var_address=tk.StringVar()
        self.var_teacher=tk.StringVar()
        self.search_var = tk.StringVar()
        self.search_entry_var = tk.StringVar()
       


        # Background image
        bg_img = Image.open(r"images\image background 1.jpg")
        bg_img = bg_img.resize((1530, 990))
        self.photoimg = ImageTk.PhotoImage(bg_img)

        img_l = tk.Label(self.root, image=self.photoimg)
        img_l.place(x=0, y=0, width=1530, height=990)

        title_lbl = tk.Label(
            img_l,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = tk.Frame(img_l, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=800)

        # Left Label
        Left_frame = tk.LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=tk.RIDGE,
            font=("times new roman", 12, "bold")
        )
        Left_frame.place(x=10, y=10, width=720, height=780)

        #current course frame
        current_course_frame = tk.LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=tk.RIDGE,
            text="Current Course Information",
            font=("times new roman", 12, "bold")
        )
        current_course_frame.place(x=10, y=10, width=700, height=150)
        #dept
        dep_label = tk.Label(
            current_course_frame,
            text="Department",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        dep_label.grid(row=0, column=0, padx=2, pady=15,sticky=tk.W)
        dep_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_department,
            font=("times new roman", 12, "bold"),
            state="readonly"
        )
        dep_combo['values'] = ("Select Department", "Computer Science", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1,padx=2, pady=15,sticky=tk.W)

        #course
        course_label = tk.Label(
            current_course_frame,
            text="Course",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        course_label.grid(row=0, column=2, padx=10, pady=15,sticky=tk.W)
        course_combo = ttk.Combobox(
            current_course_frame,
             textvariable=self.var_course,
            font=("times new roman", 12, "bold"),
            state="readonly"
        )
        course_combo['values'] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=10, pady=15,sticky=tk.W)

        #year
        year_label = tk.Label(
            current_course_frame,
            text="Year",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        year_label.grid(row=1, column=0, padx=2, pady=15,sticky=tk.W)
        year_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_year,
            font=("times new roman", 12, "bold"),
            state="readonly"
        )
        year_combo['values'] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=2, pady=15,sticky=tk.W)

        #semester
        sem_label = tk.Label(
            current_course_frame,
            text="Semester",

            font=("times new roman", 12, "bold"),
            bg="white"
        )
        sem_label.grid(row=1, column=2, padx=10, pady=10)
        sem_combo = ttk.Combobox(
            current_course_frame,
             textvariable=self.var_semester,
            font=("times new roman", 12, "bold"),
            state="readonly"
        )
        sem_combo['values'] = ("Select Semester", "Semester-1", "Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3,padx=10, pady=10,sticky=tk.W)

        #class student frame
        class_student_frame = tk.LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=tk.RIDGE,
            text="Class Student Information",
            font=("times new roman", 12, "bold")
        )
        class_student_frame.place(x=10, y=170, width=700, height=400)
        #student id
        student_id_label = tk.Label(
            class_student_frame,
            text="Student ID",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        student_id_label.grid(row=0, column=0, padx=10, pady=10)
        student_id_entry = tk.Entry(
            class_student_frame,
            textvariable=self.var_std_id,
            font=("times new roman", 12, "bold"),
            bg="white",
            validate="key",
            validatecommand=vcmd
        )
        student_id_entry.grid(row=0, column=1,padx=10, pady=10,sticky=tk.W)
        #student name
        student_name_label = tk.Label(
            class_student_frame,
            text="Student Name",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        student_name_label.grid(row=0, column=2, padx=10, pady=10)
        student_name_entry = tk.Entry(
            class_student_frame,
             textvariable=self.var_std_name,
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        student_name_entry.grid(row=0, column=3,padx=10, pady=10,sticky=tk.W)
        #class division
        class_div_label = tk.Label(
            class_student_frame,
            text="Class Division",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        class_div_label.grid(row=1, column=0, padx=10, pady=10)
        class_div_entry = tk.Entry(
            class_student_frame,
             textvariable=self.var_div,
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        class_div_entry.grid(row=1, column=1,padx=10, pady=10,sticky=tk.W)
        #roll no
        roll_no_label = tk.Label(
            class_student_frame,
            text="Roll No",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        roll_no_label.grid(row=1, column=2, padx=10, pady=10)
        roll_no_entry = tk.Entry(
            class_student_frame,
             textvariable=self.var_roll,
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        roll_no_entry.grid(row=1, column=3,padx=10, pady=10,sticky=tk.W)
        #email
        email_label = tk.Label(
            class_student_frame,
            text="Email",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        email_label.grid(row=2, column=0, padx=10, pady=10)
        email_entry = tk.Entry(
            class_student_frame,
             textvariable=self.var_email,
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        email_entry.grid(row=2, column=1,padx=10, pady=10,sticky=tk.W)
        #phone no
        phone_label = tk.Label(
            class_student_frame,
            text="Phone No",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        phone_label.grid(row=2, column=2, padx=10, pady=10)
        phone_entry = tk.Entry(
            class_student_frame,
             textvariable=self.var_phone,
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        phone_entry.grid(row=2, column=3,padx=10, pady=10,sticky=tk.W)
        #address
        address_label = tk.Label(
            class_student_frame,
            text="Address",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        address_label.grid(row=3, column=0, padx=10, pady=10)
        address_entry = tk.Entry(
            class_student_frame,
             textvariable=self.var_address,
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        address_entry.grid(row=3, column=1,padx=10, pady=10,sticky=tk.W)
        #teacher name
        teacher_label = tk.Label(
            class_student_frame,
            text="Teacher Name",
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        teacher_label.grid(row=3, column=2, padx=10, pady=10)
        teacher_entry = tk.Entry(
            class_student_frame,
             textvariable=self.var_teacher,
            font=("times new roman", 12, "bold"),
            bg="white"
        )
        teacher_entry.grid(row=3, column=3,padx=10, pady=10,sticky=tk.W)
        btn_frame = tk.Frame(
            class_student_frame,
            relief=tk.RIDGE,
            bg="white"
        )
        btn_frame.place(x=3, y=210, width=690, height=40)

        save_btn=tk.Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=17
        )
        save_btn.grid(row=0,column=0,padx=4,pady=10)

        update_btn=tk.Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=17
        )
        update_btn.grid(row=0,column=1,padx=4,pady=10)

        delete_btn=tk.Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=17
        )
        delete_btn.grid(row=0,column=2,padx=4,pady=10)

        reset_btn=tk.Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=17
        )
        reset_btn.grid(row=0,column=3,padx=4,pady=10)
        btn_frame1 = tk.Frame(
            class_student_frame,
            relief=tk.RIDGE,
            bg="white"
        )
        btn_frame1.place(x=3, y=251, width=690, height=40)
        btn_frame1.grid_columnconfigure(0, weight=1)
        take_photo_btn=tk.Button(
            btn_frame1,
            text="Take Photo Sample",
            command=self.generatedataset,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=36
        )
        take_photo_btn.grid(row=0,column=0,padx=4,pady=1)

        # Right Label
        Right_frame = tk.LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=tk.RIDGE,
            font=("times new roman", 12, "bold")
        )
        Right_frame.place(x=740, y=10, width=720, height=780)
        #====Search system======
        search_frame = tk.LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=tk.RIDGE,
            text="Search System",
            font=("times new roman", 12, "bold")
        )
        search_frame.place(x=10, y=5, width=700, height=150)
        search_label = tk.Label(
            search_frame,
            text="search by:",
            font=("times new roman", 15, "bold"),
            bg="white"
        )
        search_label.grid(row=0, column=0, padx=10, pady=10,sticky=tk.W)
        search_combo = ttk.Combobox(
            search_frame,
            textvariable=self.search_var,
            font=("times new roman", 12, "bold"),
            state="readonly",
            width=15
        )
        search_combo['values'] = ("Select", "Student ID", "Name", "Roll No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=10, pady=10,sticky=tk.W)
        

        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_entry_var,
            font=("times new roman", 12, "bold"),
            bg="white",
            width=20
        )
        search_entry.grid(row=0, column=2,padx=10, pady=10,sticky=tk.W)

        search_btn=tk.Button(
            search_frame,
            command=self.search_data,
            text="Search",
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=15
        )
        search_btn.grid(row=1,column=1,padx=4,pady=10)
        showall_btn=tk.Button(
            search_frame,
            text="Show All",
            command=self.fetch_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=15
        )
        showall_btn.grid(row=1,column=2,padx=4,pady=10)
        #===table frame===
        table_frame = tk.Frame(
            Right_frame,
            bd=2,
            bg="white",
            relief=tk.RIDGE
        )
        table_frame.place(x=10, y=160, width=700, height=600)
        scrooll_x = ttk.Scrollbar(
            table_frame,
            orient=tk.HORIZONTAL
        )
        scrooll_y = ttk.Scrollbar(
            table_frame,
            orient=tk.VERTICAL
        )
        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "email",
                "phone",
                "address",
                "teacher",
                "photo"
            ),
            xscrollcommand=scrooll_x.set,
            yscrollcommand=scrooll_y.set
        ) 
        scrooll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scrooll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrooll_x.config(command=self.student_table.xview)
        scrooll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course") 
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table['show'] = 'headings'
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=150)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        self.student_table.pack(fill=tk.BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
    #function declaration

    def only_numbers(self, char):
        """Allow only digits"""
        return char.isdigit()
    #add data
    def add_data(self):
        if self.var_department.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            conn= get_db_connection()
            cursor=conn.cursor()
            cursor.execute("""INSERT INTO students(department,course,year,semester,student_id,name,division,roll,email,phone,address,teacher,photo_sample) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(
                self.var_department.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                int(self.var_std_id.get()),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                "No"
            ))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
           
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #fetch data
    def fetch_data(self):
        conn= get_db_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", tk.END, values=row)
            conn.commit()
            conn.close()

    #   GET CURSOR
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content['values']
        # SAFETY CHECK
        if not data or len(data) < 13:
            return

        self.var_department.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_email.set(data[8])
        self.var_phone.set(data[9])
        self.var_address.set(data[10])
        self.var_teacher.set(data[11])


    #update function
    def update_data(self):
        if self.var_department.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
            if Update > 0:
                conn= get_db_connection()
                cursor=conn.cursor()
                cursor.execute("""UPDATE students SET department=?,course=?,year=?,semester=?,name=?,division=?,roll=?,email=?,phone=?,address=?,teacher=? WHERE student_id=?""",(
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    int(self.var_std_id.get())
                ))
            else:
                if not Update:
                    return
            conn.commit()
            conn.close()
            self.fetch_data()
            
            messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    #delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
            return
        try:
            Delete = messagebox.askyesno("Delete", "Do you want to delete this student details?", parent=self.root)
            if Delete > 0:
                conn= get_db_connection()
                cursor=conn.cursor()
                cursor.execute("DELETE FROM students WHERE student_id=?", (int(self.var_std_id.get()),))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Student details successfully deleted", parent=self.root)
            else:
                if not Delete:
                    return
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #reset function
    def reset_data(self):
        self.var_department.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        

    #generate data set or take photo samples
    def generatedataset(self):
        if (
            self.var_department.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            # ================= sqlite3 =================
            conn=get_db_connection()
            cursor=conn.cursor()
            cursor.execute("""SELECT * FROM students WHERE student_id=?""",(int(self.var_std_id.get()),))
            row=cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", f"Student ID- {self.var_std_id.get()} not found in database", parent=self.root)
                return       
            conn.close()
            # ================= Face Classifier =================
            face_classifier = cv2.CascadeClassifier(
                "haarcascade_frontalface_default.xml"
            )

            if face_classifier.empty():
                messagebox.showerror("Error", "Haarcascade file not found", parent=self.root)
                return

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5) #It detects faces (or objects) in an image and returns their locations.LBPH cannot find faces by itself.LBPH only recognizes a face.Thus we use detectMultiScale to find faces first.

                for (x, y, w, h) in faces:
                    return img[y:y+h, x:x+w]

                return None

            # ================= Camera =================
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                messagebox.showerror("Error", "Camera not accessible", parent=self.root)
                return

            import os
            os.makedirs("data", exist_ok=True)

            img_id = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                cropped_face = face_cropped(frame)

                if cropped_face is not None:
                    img_id += 1
                    face = cv2.resize(cropped_face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    data_dir = "data"
                    os.makedirs(data_dir, exist_ok=True)

                    file_name_path = os.path.join(
                            data_dir,
                            f"user.{self.var_std_id.get()}.{img_id}.jpg"
)


                    cv2.imwrite(file_name_path, face)
                    cv2.putText(
                        face,
                        str(img_id),
                        (50, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        2,
                        (255, 255, 255),
                        2,
                    )
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            # Update photo sample status in database
            conn=get_db_connection()
            cursor=conn.cursor()
            cursor.execute("""SELECT * FROM students WHERE student_id=?""",(int(self.var_std_id.get()),))
            row=cursor.fetchone()
            cursor.execute("""UPDATE students SET photo_sample=? WHERE student_id=?""",(
                "Yes",
                int(self.var_std_id.get())
            ))
            cap.release()
            cv2.destroyAllWindows()
            conn.commit()
            conn.close()
            messagebox.showinfo("Result", "Generating dataset completed!!!", parent=self.root)
            
            self.fetch_data()

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #search function
    def search_data(self):
        try:
            conn= get_db_connection()
            cursor=conn.cursor()
            search_by = self.search_var.get()
            search_value = self.search_entry_var.get()

            if search_by == "Select" or search_value == "":
                messagebox.showerror("Error", "Please select a search criterion and enter a search value", parent=self.root)
                return

            query = ""
            if search_by == "Student ID":
                try:
                    sid = int(search_value)
                except ValueError:
                    messagebox.showerror("Error", "Student ID must be a number", parent=self.root)
                    return
                query = "SELECT * FROM students WHERE student_id = ?"
                cursor.execute(query, (int(search_value),))

            elif search_by == "Name":
                query = "SELECT * FROM students WHERE name LIKE ?"
                cursor.execute(query, ('%' + search_value + '%',)) 
            elif search_by == "Roll No":
                query = "SELECT * FROM students WHERE roll LIKE ?"
                cursor.execute(query, ('%' + search_value + '%',))   

            rows = cursor.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", tk.END, values=row)
            else:
                messagebox.showinfo("Info", "No records found", parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


def get_db_connection():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect("database/student.db")
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            department TEXT,
            course TEXT,
            year TEXT,
            semester TEXT,
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            division TEXT,
            roll TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            teacher TEXT,
            photo_sample TEXT
        )
    """)
    conn.commit()
    return conn


if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()       #root.mainloop() starts the Tkinter event loop that keeps the GUI running and responsive until the window is closed.
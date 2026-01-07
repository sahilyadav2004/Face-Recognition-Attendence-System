import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from student import Student
from train import Train
from face_recognition import face_recognition
from attendance import attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x990+0+0")
        self.root.title("Face Recognition System")

        # ================= WINDOW REFERENCES =================
        self.student_window = None
        self.train_window = None
        self.face_window = None
        self.attendance_window = None
        self.developer_window = None
        self.help_window = None

        # ================= BACKGROUND =================
        bg_img = Image.open(r"images\image background 1.jpg")
        bg_img = bg_img.resize((1530, 990))
        self.photoimg = ImageTk.PhotoImage(bg_img)

        img_l = tk.Label(self.root, image=self.photoimg)
        img_l.place(x=0, y=0, width=1530, height=990)

        title_lbl = tk.Label(
            img_l,
            text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ================= BUTTONS =================
        tk.Button(
            img_l, text="Student",
            command=self.open_student,
            font=("times new roman", 26, "bold"),
            bg="darkblue", fg="white", cursor="hand2"
        ).place(x=200, y=200, width=220, height=100)

        tk.Button(
            img_l, text="Attendance",
            command=self.open_attendance,
            font=("times new roman", 26, "bold"),
            bg="darkblue", fg="white", cursor="hand2"
        ).place(x=500, y=200, width=220, height=100)

        tk.Button(
            img_l, text="Train",
            command=self.open_train,
            font=("times new roman", 26, "bold"),
            bg="darkblue", fg="white", cursor="hand2"
        ).place(x=800, y=200, width=220, height=100)

        tk.Button(
            img_l, text="Developer",
            command=self.open_developer,
            font=("times new roman", 26, "bold"),
            bg="darkblue", fg="white", cursor="hand2"
        ).place(x=1100, y=200, width=220, height=100)

        tk.Button(
            img_l, text="Detect Face",
            command=self.open_face,
            font=("times new roman", 26, "bold"),
            bg="darkblue", fg="white", cursor="hand2"
        ).place(x=200, y=500, width=220, height=100)

        tk.Button(
            img_l, text="Help",
            command=self.open_help,
            font=("times new roman", 26, "bold"),
            bg="darkblue", fg="white", cursor="hand2"
        ).place(x=500, y=500, width=220, height=100)

        tk.Button(
            img_l, text="Photos",
            command=self.open_img,
            font=("times new roman", 26, "bold"),
            bg="darkblue", fg="white", cursor="hand2"
        ).place(x=800, y=500, width=220, height=100)

        tk.Button(
            img_l, text="Exit",
            command=self.exit_app,
            font=("times new roman", 26, "bold"),
            bg="darkblue", fg="white", cursor="hand2"
        ).place(x=1100, y=500, width=220, height=100)

    # ================= GENERIC WINDOW OPENER =================
    def _open_window(self, window_attr, window_class, modal=False):
        win = getattr(self, window_attr)

        if win is None or not win.winfo_exists():
            win = tk.Toplevel(self.root)
            setattr(self, window_attr, win)

            if modal:
                win.grab_set()

            window_class(win)

            win.protocol(
                "WM_DELETE_WINDOW",
                lambda: self._close_window(window_attr)
            )
        else:
            win.deiconify()
            win.focus_force()
            win.lift()

    def _close_window(self, window_attr):
        win = getattr(self, window_attr)
        if win:
            win.destroy()
            setattr(self, window_attr, None)

    # ================= OPEN METHODS =================
    def open_student(self):
        self._open_window("student_window", Student)

    def open_train(self):
        self._open_window("train_window", Train)

    def open_face(self):
        self._open_window("face_window", face_recognition)

    def open_attendance(self):
        self._open_window("attendance_window", attendance, modal=True)

    def open_developer(self):
        self._open_window("developer_window", Developer)

    def open_help(self):
        self._open_window("help_window", Help)

    # ================= UTILITIES =================
    def open_img(self):
        try:
            os.startfile("data")
        except Exception as e:
            print("Error opening folder:", e)

    def exit_app(self):
        if tk.messagebox.askyesno(
            "Face Recognition",
            "Are you sure you want to exit?",
            parent=self.root
        ):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Face_Recognition_System(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x990+0+0")
        self.root.title("Face Recognition System")

        # Background image
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

        # ===== First Row =====
        b1 = tk.Button(img_l, text="Student",
                       font=("times new roman", 26, "bold"),command=self.student_details,
                       bg="darkblue", fg="white", cursor="hand2")
        b1.place(x=200, y=200, width=220, height=100)

        b3 = tk.Button(img_l, text="Attendence",
                       font=("times new roman", 26, "bold"),
                       bg="darkblue", fg="white", cursor="hand2")
        b3.place(x=500, y=200, width=220, height=100)

        b5 = tk.Button(img_l, text="Train",
                       font=("times new roman", 26, "bold"),
                       bg="darkblue", fg="white", cursor="hand2")
        b5.place(x=800, y=200, width=220, height=100)

        b7 = tk.Button(img_l, text="Developer",
                       font=("times new roman", 26, "bold"),
                       bg="darkblue", fg="white", cursor="hand2")
        b7.place(x=1100, y=200, width=220, height=100)

        # ===== Second Row =====
        b2 = tk.Button(img_l, text="Detect Face",
                       font=("times new roman", 26, "bold"),
                       bg="darkblue", fg="white", cursor="hand2")
        b2.place(x=200, y=500, width=220, height=100)

        b4 = tk.Button(img_l, text="Help",
                       font=("times new roman", 26, "bold"),
                       bg="darkblue", fg="white", cursor="hand2")
        b4.place(x=500, y=500, width=220, height=100)

        b6 = tk.Button(img_l, text="Photos",
                       font=("times new roman", 26, "bold"),
                       bg="darkblue", fg="white", cursor="hand2")
        b6.place(x=800, y=500, width=220, height=100)

        b8 = tk.Button(img_l, text="Exit",
                       font=("times new roman", 26, "bold"),
                       bg="darkblue", fg="white", cursor="hand2")
        b8.place(x=1100, y=500, width=220, height=100)
    #function button

    def student_details(self):
        self.new_window=tk.Toplevel(self.root)
        self.app=Student(self.new_window)


if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

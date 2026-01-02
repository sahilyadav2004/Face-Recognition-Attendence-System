import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from pymongo import MongoClient
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = tk.Label(
            self.root,
            text="Help Desk",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main frame (proper size)
        main_frame = tk.Frame(self.root, bd=2, bg="white", relief=tk.RIDGE)
        main_frame.place(x=0, y=45, width=1530, height=745)

        # Text label
        lbl = tk.Label(
            main_frame,
            text=(
                "For assistance with the Face Recognition System, please contact our support team at:\n\n"
                "Email:sahillawaniya4@gmail.com\n"
            ),
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="black",
            justify=tk.LEFT,
            wraplength=1400,   # ✅ VERY IMPORTANT
            anchor="nw",       # top-left alignment
            padx=20,
            pady=20
        )
        lbl.place(x=0, y=0, width=1530, height=745)


if __name__ == "__main__":
    root = tk.Tk()
    obj = Help(root)
    root.mainloop()

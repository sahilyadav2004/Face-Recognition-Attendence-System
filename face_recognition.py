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


class face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Training")
        self.root.geometry("1530x790+0+0")

        title_label = tk.Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"),bg="white",fg="blue")
        title_label.place(x=0, y=0, width=1530, height=55)
        update_btn=tk.Button(
            self.root,
            text="Detect Face",
            command=self.recognition,
            font=("times new roman", 20, "bold"),
            bg="blue",
            fg="white",
            width=17
        )
        update_btn.place(x=570, y=350, width=400, height=55)


    #attendence
    def mark_attendance(self, sid, name):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if (sid not in name_list) and (name not in name_list):
                now = datetime.now()
                dtString = now.strftime("%Y-%m-%d %H:%M:%S")
                f.writelines(f"\n{sid},{name},{dtString},Present")
            

        #===============face recognition=================
    def recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
                id, distance = clf.predict(gray_image[y:y + h, x:x + w])
                
                
                if distance < 70:
                    client = MongoClient("mongodb://localhost:27017/")
                    db = client["student_db"]
                    collection = db["students"]

                    student = collection.find_one({"student_id": str(id)})

                    if student:
                        name = student["name"]
                        sid = student.get("student_id", "N/A")
                    else:
                        name = "Unknown"
                        sid = "N/A"

                    confidence_text = f"{int(100 - distance)}%"
                else:
                    name = "Unknown"
                    sid = "N/A"
                    confidence_text = "0%"
                cv2.putText(img, f"ID: {sid}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                cv2.putText(img, str(name), (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                cv2.putText(img, str(confidence_text), (x, y + h + 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                self.mark_attendance(sid, name)
                coord.append((x, y, w, h))

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("face_trainer.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break
            if cv2.getWindowProperty("Welcome to Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = face_recognition(root)
    root.mainloop()        
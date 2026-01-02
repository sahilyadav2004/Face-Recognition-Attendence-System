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


    #====================attendence====================
    def mark_attendance(self, sid, name, dep):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()

            sid_list = []
            last_attendance_id = 0

            for line in myDataList:
                line = line.strip()
                if not line:
                    continue

                entry = line.split(",")

                if len(entry) < 2:
                    continue

                # entry format:
                # [attendance_id, sid, name, dep, date, time, status]

                last_attendance_id = int(entry[0])   # keep updating → last row
                sid_list.append(entry[1])

            if sid not in sid_list:
                new_attendance_id = last_attendance_id + 1

                now = datetime.now()
                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")

                f.write(
                    f"{new_attendance_id},{sid},{name},{dep},{date},{time},Present\n"
                )
            

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
                        dep= student.get("department", "N/A")
                    else:
                        name = "Unknown"
                        sid = "N/A"
                        dep="N/A"

                    confidence_text = f"{int(100 - distance)}%"
                else:
                    name = "Unknown"
                    sid = "N/A"
                    dep="N/A"
                    confidence_text = "0%"
                cv2.putText(img, f"ID: {sid}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                cv2.putText(img, str(name), (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                cv2.putText(img, str(confidence_text), (x, y + h + 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                if(name!="" and name!="unknown" and sid!="N/A"):
                    self.mark_attendance(sid, name,dep)
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
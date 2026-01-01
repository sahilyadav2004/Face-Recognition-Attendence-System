import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from pymongo import MongoClient
import cv2
import os
import numpy as np
class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Training")
        self.root.geometry("1530x790+0+0")

        title_label = tk.Label(self.root, text="Train Face Recognition Model", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20)

        train_button = ttk.Button(self.root, text="Start Training", command=self.start_training)
        train_button.pack(pady=10)

    def start_training(self):
        try:
        
            # Fetch face data from the database
            data_dir=("data")
            path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

            faces=[]
            ids=[]

            for image_path in path:
                img=Image.open(image_path).convert('L') # Grayscale
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image_path)[1].split(".")[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13

            ids=np.array(ids)
            # Train the model
            model=cv2.face.LBPHFaceRecognizer_create()
            model.train(faces,ids)
            model.write("face_trainer.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training Completed Successfully!")


        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Train(root)
    root.mainloop()
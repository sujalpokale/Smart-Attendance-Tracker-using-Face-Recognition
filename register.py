import cv2 
import face_recognition
import numpy as np
from database import get_connection

def register_face(name ,roll_no):
    conn = get_connection()
    cursor = conn.cursor()
    cam = cv2.VideoCapture(0)
    print("Press 's' to capture your face.")
    
    while True:
        ret ,frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Register Face", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            encoding = face_recognition.face_encodings(rgb)
            if encoding:
                encoding = encoding[0]
                cursor.execute("INSERT INTO students (name, roll_no, face_encoding) VALUES (?, ?, ?)", 
                               (name, roll_no, encoding.tobytes()))
                conn.commit()
                print(f"Face registered for {name} with roll number {roll_no}.")
            else:
                print("No face detected. Please try again.")
    cam.release()
    cv2.destroyAllWindows()
    conn.close()
    
if __name__ == "__main__":
    name = input("Enter your name: ")
    roll_no = int(input("Enter your roll number: "))
    register_face(name, roll_no)
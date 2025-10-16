import cv2 
import face_recognition
import numpy as np
from datetime import datetime
from database import get_connection

def mark_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id,name, roll_no ,face_encoding FROM students")
    known_face = [(r[0],r[1],r[2],np.frombuffer(r[3],dtype=np.float64)) for r in cursor.fetchall()]
    
    if not known_face:
        print("No student data found in the database.")
        return

    cam = cv2.VideoCapture(0)
    print("Press 'q' to quit the attendance marking process.")
    while True:
        ret ,frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        face = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb,face)
        
        for encodeFace ,faceLoc in zip(encodings,face):
            matches = face_recognition.compare_faces([f[3] for f in known_face],encodeFace)
            faceDis = face_recognition.face_distance([f[3] for f in known_face],encodeFace)
            matchIndex = np.argmin(faceDis)
            
            if matches[matchIndex]:
                id,name,roll_no, _ = known_face[matchIndex]
                y1,x2,y2,x1 = faceLoc
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(frame,f"{name} ({roll_no})",(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
                
                date = datetime.now().strftime("%Y-%m-%d")
                time = datetime.now().strftime("%H:%M:%S")
                cursor.execute("SELECT * FROM attendance WHERE id=? AND date=?", (id, date))
                
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO attendance (student_id, date, time) VALUES (?, ?, ?)", (id, date, time))
                    conn.commit()
                    print(f"Attendance marked for {name} ({roll_no}) at {time} on {date}")
        cv2.imshow("Attendance System",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cam.release()
    cv2.destroyAllWindows()
    conn.close()

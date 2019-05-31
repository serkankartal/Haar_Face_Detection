import cv2
import imageio

face_cascade=cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade-eye.xml")

def Detect(frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(frame,1.5,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        face_gray=gray[x:x+w, y:y+h]
        face_color=frame[x:x+w, y:y+h]
        eyes=eye_cascade.detectMultiScale(face_gray,1.1,3)
        for (xe,ye,we,he) in eyes:
            cv2.rectangle(face_color,(xe,ye),(xe+we,ye+he),(0,255,0),2)

    return frame

reader=imageio.get_reader('1.mp4')
fps=reader.get_meta_data()['fps']
writer=imageio.get_writer('output.mp4',fps=fps)

for i,frame in enumerate(reader):
    frame=Detect(frame)
    if(i%10 == 0):
        print(i)
    writer.append_data(frame)

writer.close();

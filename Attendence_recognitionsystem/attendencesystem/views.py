from urllib import request
from django.shortcuts import render, redirect
import time
import cv2
import csv
import os
from imutils import paths
import numpy as np
import imutils, pickle, cv2, os
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC 
from .models import Contact, Login

def create_dataset(username):
    cascade = "attendencesystem\haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(cascade)

    Name = str(input("Enter your name: "))
    Roll_number = int(input("Enter Your Roll_number: "))
    dataset = "attendencesystem\Dataset_AttendenceSysytemFaceRecognition"
    sub_data = Name
    path = os.path.join(dataset, sub_data)

    if not os.path.isdir(path):
        os.mkdir(path)
        print(sub_data)

    info = [str(Name), str(Roll_number)]
    with open("student.csv",'a') as csvFile:
        write = csv.writer(csvFile)
        write.writerow(info)
    csvFile.close()

    print("Starting Video Stream...")
    cam = cv2.VideoCapture(0)
    time.sleep(2.0)
    total = 0

    while total < 100:
        print(total)
        _, frame = cam.read()
        img = imutils.resize(frame, width=400)
        rects = detector.detectMultiScale(
            cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), scaleFactor=1.1,
            minNeighbors= 5, minSize=(30,30))

        for(x,y,w,h) in rects:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            p = os.path.sep.join([path, "{}.png".format(
                str(total).zfill(5))])
            cv2.imwrite(p,img)
            total+=1

        cv2.imshow('Frame', frame)
        key= cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()

    

def preprocessing(self):
    return render(request, exec(open('attendencesystem\Training_Processing\ex23_2_PreprocessingEmbeddings.py').read()))

def Training(self):
    return render(request, exec(open('attendencesystem\Training_Processing\ex23_3_trainingFaceML.py').read()))
    
def recognize(self):
    return render(request, exec(open('attendencesystem\Training_Processing\ex23_4_recognizingPerson.py').read()))
    

# Create your views here.

def homePageView(request):
    return render(request,'attendencesystem/Home.html')

def contactPageView(request):
    if request.method=='GET':
         return render(request,'attendencesystem/Contact.html')
    elif request.method=='POST':
        email =  request.POST.get('email')
        Password =  request.POST.get('inputPassword4')
        Address =  request.POST.get('inputAddress')
        City =  request.POST.get('inputCity')
        State =  request.POST.get('inputState')
        zip =  request.POST.get('inputZip')

        c1 = Contact(email=email, password=Password, Address=Address, City=City, State=State, zip=zip)
        c1.save()

        print("Email:", email)
        print("Password:", Password)
        print("Address:", Address)
        print("City:", City)
        print("State:", State)
        print("zip:", zip)

        return redirect('/Contact')

def loginPageView(request):
    if request.method=='GET':
         return render(request,'attendencesystem/Login.html')
    elif request.method=='POST':
        Username =  request.POST.get('username')
        Password =  request.POST.get('password')
        
        c1 = Login(username=Username, password=Password)
        c1.save()

        print("Username:", Username)
        print("Password:", Password)
       

        return redirect('/Login')

def aboutPageView(request):
    return render(request,'attendencesystem/About.html')







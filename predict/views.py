from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np


# Create your views here.
def home_page(request):
    return render(request,"home_page.html")

def success(request):
    return render(request,"success.html")

def login(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['psw']
        user=auth.authenticate(username=u,password=p)
        if user is not None:
            auth.login(request,user)
            return render(request,"home.html")
        else:
            return render(request,"login.html")
    return render(request,"login.html")


# def login(request):
#     return render(request,'login.html')
def home(request):
     return render(request,"home.html")


def register(request):
    return  render(request,'register.html')

def saveuser(request):
    username=request.POST['uname']
    password = request.POST['psw']
    # name = request.POST['name']
    # email = request.POST['email']
    # phone = request.POST['phone']
    # address = request.POST['address']

    newusers=User(username=username,password=password)
    newusers.save()
    return render(request, 'login.html')
def verifyuser(request):
    username = request.POST.get('uname')
    password = request.POST.get('psw')

    user= User.objects.filter(username=username)

    for u in user:
        if u.password==password:
            return render(request,'home.html')
        else:
            return render(request,'login.html')
def result(request):
    Pregnancies= request.POST['Pregnancies']
    Glucose= request.POST['Glucose']
    BloodPressure= request.POST['BloodPressure']
    SkinThickness= request.POST['SkinThickness']
    Insulin= request.POST['Insulin']
    BMI= request.POST['BMI']
    DiabetesPedigreeFunction= request.POST['DiabetesPedigreeFunction']
    Age= request.POST['Age']
    
    values=[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    values=np.reshape(values,(1,-1))

    df=pd.read_csv(r"diabetes.csv")
    X=df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
    y=df['Outcome']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # scaler = RandomForestClassifier()
    # X_train = scaler.fit(X_train)
    # X_test = scaler.transform(X_test)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    result=model.predict(values)
    result=result[0]
    if result==0:
        result="You are not diabetic."
    else:
        result="You are diabetic."
    print(result)
    return render(request,'result.html',{'result':result})
from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,"home.html")

def result(request):

    model = joblib.load("election.sav")

    lis = []

    lis.append(request.GET['one'])
    lis.append(request.GET['two'])
    lis.append(request.GET['three'])
    lis.append(request.GET['four'])
    lis.append(request.GET['five'])
    lis.append(request.GET['six'])

    print(lis)

    ans = model.predict([lis])
    print(ans)

    return render(request,"result.html",{"ans":ans})
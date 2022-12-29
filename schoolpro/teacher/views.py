from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# function based view
# class based view


def menuu(request):
    name='hotel sager'
    # li=["apple","orenge","kiwi"]
    # c=True
     
    menu=[{"item":"CB","category":"Non-veg","price":120},{"item":"BB","category":"veg","price":121},{"item":"AB","category":"Non-veg","price":120}]
    return render(request,"menu.html",{"data":name,"table":menu})
        
        
    # table=[{"item":"CB","category":"Non-veg","price":120},{"item":"BB","category":"veg","price":121},{"item":"AB","category":"Non-veg","price":120}]
    # return render(request,"menu.html",{"data":name,"table":table})


def home(request):
    return render(request,"home.html")


def logi(request):
    return render(request,"login.html")


def log(request):
    if request.method=="POST":
        user=request.POST.get('un')
        psw=request.POST.get('ps')
        return HttpResponse("POST:<br>username:"+user+"<br>password:"+psw)
    elif request.method=="GET":
        return render(request,"log.html")


        
def index(request):
    name='Anaswara'
    li=["apple","orenge","kiwi"]
    c=False

    
    
    table=[{"name":"arun","age":40,"class":"4B"},{"name":"varun","age":41,"class":"5B"},{"name":"aruna","age":90,"class":"6B"}]
    return render(request,"index.html",{"data":name,"frts":li,"table":table,"condition":c})

def registr(request):
    if request.method=="GET":
        return render(request,"registr.html")
    elif request.method=="POST":
        fn=request.POST.get("fname")
        ln=request.POST.get("lname")
        em=request.POST.get("email")
        uname=request.POST.get("user")
        pass1=request.POST.get("ps1")
        pass2=request.POST.get("ps2")
        if pass1==pass2:
            return HttpResponse(fn+","+ln+","+em+","+uname+","+pass1)
        else:
            return HttpResponse("Passwords mismatch")

 
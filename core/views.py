
from pyexpat.errors import messages
from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect # type: ignore
from .models import Car
from django.conf import settings # type: ignore
from PIL import Image # type: ignore
import os
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth import login as lg # type: ignore



def home(request):
   
        if request.user.is_authenticated:
         cars = Car.objects.all()
         return render(request, "index.html", {"car_list": cars})
        else:
             return redirect (login)
        



def save(request):
    vmodel = request.POST.get("model")
    vbrand = request.POST.get("brand")
    vplate = request.POST.get("plate")
    vname = request.POST.get("name")
    file = request.FILES.get("photo")

    # Cria o objeto Car e associa a imagem
    car = Car(model=vmodel, brand=vbrand, plate=vplate, name=vname, photo=file)
    car.save()  

    
    cars = Car.objects.all()


    return render(request,"index.html", {"car_list":cars})


def update(request, id):

    carId = Car.objects.get(id=id)
    return render(request,"update.html", {"car": carId})


def updating(request, id):
  
        vmodel = request.POST.get("model")
        vbrand = request.POST.get("brand")
        vplate = request.POST.get("plate")
        vname = request.POST.get("name")
        file = request.FILES.get("photo")

       
        car = Car.objects.get(id=id)
        car.model = vmodel
        car.brand = vbrand
        car.plate = vplate
        car.name = vname
        if file:
            car.photo = file
        car.save()
        return redirect('home')
     

def delete(request, id):
        car = Car.objects.get(id=id)
        car.delete()
        return redirect('home')



def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('password')

        user = User.objects.filter(username = username).first()
        if user:
             return HttpResponse("Já Existe um usuário com este nome!")
        
        user = User.objects.create_user(username,email,password)
        user.save()

        return HttpResponse("Usuário Cadastrado com sucesso!")  # Retorna HttpResponse com a mensagem

        


def login(request):
    if request.method =="GET":
        return render(request, 'login.html')
    else:
         username = request.POST.get('username')
         password = request.POST.get('password')
         
         user = authenticate(username = username, password = password)

         if user:
              lg(request,user)

              return redirect(home)
         else:
             
              return redirect(login)
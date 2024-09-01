
from pyexpat.errors import messages
from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect # type: ignore
from .models import Car
from django.conf import settings # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth import login as lg # type: ignore
from django.contrib.auth import logout as lgout # type: ignore
from django.contrib import messages # type: ignore
from django.shortcuts import render, get_object_or_404 # type: ignore


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
    vowner =request.POST.get("createdby")
    file = request.FILES.get("photo")

    # Cria o objeto Car e associa a imagem
    car = Car(model=vmodel, brand=vbrand, plate=vplate, name=vname, photo=file, createdby = vowner, like =0)
    car.save()  

    
   


    return redirect(home)


def update(request, id):
    user = get_object_or_404(User, id=id)
    print(user)

    car_list = Car.objects.filter(createdby=user.id)

    for i in range(len(car_list)):
     print(car_list[i])

    return render(request, "update.html", {"car_list": car_list, "user": user})


def updateMyCar(request, id):
    
    car = Car.objects.get(id=id) 


    return render(request, "updateMyCar.html", {"car": car})
 

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

def toAssess(request, id):
        car = Car.objects.get(id=id)
        car.like += 1
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
             messages.success(request, "Usuário já existe!")
             return redirect('login')
        else:
            user = User.objects.create_user(username,email,password)
            user.save()
            return redirect(login)
          # Retorna HttpResponse com a mensagem

        


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
         
def logout(request):
    lgout(request)
    return redirect(login)
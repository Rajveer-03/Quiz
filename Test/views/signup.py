from django.shortcuts import render, redirect
from ..models.student import Student
from ..models.user import User
from django.views import View


class Signup(View):
    def get(self, request):
        try:
            if(request.session['email']):
                return render(request, "signup.html")
        
        except:
            try:
                if(request.session['user']):
                    return redirect('home')
            except:
                return redirect("createuser")

    def post(self, request):
        email = request.session['email']
        Email = User.objects.get(Email = email)
        Fname = request.POST.get('fname')
        Lname = request.POST.get('lname')
        Age = request.POST.get('age')
        Phone = request.POST.get('phone')
        Gender = request.POST.get('gender')
        Country = request.POST.get('country')
        State = request.POST.get('state')
        City = request.POST.get('city')
        Address = request.POST.get('address')

        student = Student(Email= Email, Fname=Fname, Lname=Lname, Age=Age, Contact=Phone,
                           Gender=Gender, Country=Country, State=State, City=City, Address=Address)
        student.save()
        request.session.clear()
        return redirect("login")
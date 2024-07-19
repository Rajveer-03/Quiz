from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from ..models.student import Student
from ..models.user import User
from django.views import View

class Login(View):
    def get(self, request):
        try:
            if(request.session['user']):
                return redirect('home')
        except:
            return render(request, 'login.html')
                
    
    def post(self, request):
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        flag = 0

        def isExist(Email):
            try:
                if (User.objects.get(Email=Email)):
                    return True
            except:
                return False
            
        if(isExist(Email)):
            try:
                if(Student.objects.get(Email=(User.objects.get(Email=Email)))):
                    user = User.objects.get(Email=Email)
                    flag = check_password(Password, user.Password)
                else:
                    request.session['email']
                    return redirect('signup')
            except:
                request.session['email']
                return redirect('signup')

            
        if(flag):
            stu = Student.objects.get(Email=user)
            request.session['user'] = Email
            request.session['name'] = stu.Fname
            return redirect('home')
        else:
            data = {
            'error':'Invalid Credentials'
            }
            return render(request, 'login.html', data)
            
            

def Logout(request):
    request.session.clear()
    return redirect('login')
    



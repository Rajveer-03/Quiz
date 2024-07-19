from django.core.mail import send_mail
from ..models.student import Student
from django.shortcuts import render, redirect
from ..models.user import User
from django.views import View
from random import randint
from Quiz import settings

class CreateUser(View):
    def get(self, request):
        try:
            if (request.session['OTP']):
                print(request.session['OTP'])
                return redirect('verify')
        
        except:
            try:
                if(request.session['user']):
                    return redirect('home')
            except:
                request.session.clear()
                return render(request, 'createuser.html')
    
    def post(self, request):
        error_message = None
        if(request.POST.get('type')=="Verify"):
            Email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            def isExist(Email):
                return User.objects.filter(Email=Email)

            if(password1!=password2):
                error_message = "Password Mismatch"

            if(isExist(Email)):
                error_message="Email already Exists"

            if(not error_message):
                request.session['email'] = Email
                request.session['password'] = password1
                request.session['OTP'] = randint(100000,999999)

                message = "Dear "+str(Email)+",\n\nWe hope this email finds you well.\nThank you for registering with us. To complete your account verification, please use the following One-Time Password (OTP):\n\n  Your OTP: "+str(request.session['OTP'])+"\n\nFor security purposes, please do not share this code with anyone. If you did not request this verification, please ignore this email.\nIf you have any questions or need further assistance, feel free to contact our support team at narinder0624@gmail.com.\n\nThank you for choosing our Service."


                subject = "Account Verification"

                send_mail(subject, message, settings.EMAIL_HOST_USER, [Email])
                print(request.session['OTP'])
                return render(request, 'verify.html')

            return render(request, 'createuser.html', {"error":error_message})
        
from django.contrib.auth.hashers import make_password
from django.shortcuts import render,redirect
from ..models.user import User
from django.views import View

class Verify(View):
    def get(self, request):
        try:
            if(request.session['OTP']):
                return render(request, 'verify.html')
        except:
            return redirect('home')
    
    def post(self, request):
        OTP = request.POST.get('otp')
        if(OTP == str(request.session['OTP'])):
            Password = make_password(request.session['password'])
            # Password = request.session['password']
            usr = User(Email = request.session['email'], Password = Password)
            usr.save()
            del request.session['password']
            del request.session['OTP']
            return render(request, 'signup.html')
        else:
            error_message = "OTP Mismatched"
            request.session.clear()
            return render(request, 'createuser.html', {"error":error_message})
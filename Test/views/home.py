from django.shortcuts import render
from ..models.user import User
from ..models.student import Student
from django.views import View

class Home(View):
    def get(self,request):
        try:
            if(request.session['user']):
                user = User.objects.get(Email = request.session['user'])
                student = Student.objects.get(Email=user)
                return render(request, 'index.html', {'student':student})
        except:
            return render(request, "index.html")

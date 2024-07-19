from django.shortcuts import redirect, render
from django.views import View

class Instruction(View):
    def get(self, request):
        try:
            if (request.session['test'] and request.session['user']):
                return render(request, "instruction.html")

        except:
            return redirect('test_series')
    
    def post(self, request):
        pass
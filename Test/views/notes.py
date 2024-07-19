from django.shortcuts import render, redirect
from django.views import View
from ..models.catagory import Catagory
from ..models.note import Notes as Note

class Notes(View):
    def get(self, request):
        c_id = Catagory.objects.all()[0].id
        try:
            if (request.GET.get('catagory_id')):
                c_id = request.GET.get('catagory_id')
        except:
            pass
        catagory = Catagory.objects.all()
        notes = Note.notes_by_catagory(c_id)
        return render(request, "notes.html" , {'notes':notes, 'catagories':catagory, 'check_catagory':int(c_id)})
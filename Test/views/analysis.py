from django.shortcuts import render, redirect
from django.views import View
from ..models.result import Result
from ..models.test import Test
from ..models.student import Student
from ..models.user import User

class Analysis(View):
    def get(self, request):
        try:
            rank = 1
            test = Test.objects.get(id = request.session['test'])
            user = User.objects.get(Email=request.session['user'])
            student = Student.objects.get(Email=user)
            attempted_student = Result.objects.get(Student=student, Test=test)
            attempted_students = Result.objects.filter(Test=test).exclude(Student=student)
            number_of_students = attempted_students.count() + 1

            for i in attempted_students:
                if attempted_student.Total_Marks <= i.Total_Marks:
                    rank += 1
            
            attempted_student.Rank = rank
            
            percentile = ((number_of_students-(rank-1))/number_of_students)*100
            attempted_student.Percentile = percentile
            attempted_student.save()

            # return render(request, 'analysis.html')
            return render(request, 'analysis.html', {'student':attempted_student, 'test':test.id})
        except:
            return redirect('test_series')
    
    def post(self, request):
        rank = 1
        t = request.POST.get('testid')
        test = Test.objects.get(id = t)
        user = User.objects.get(Email=request.session['user'])
        student = Student.objects.get(Email=user)
        attempted_student = Result.objects.get(Student=student, Test=test)
        attempted_students = Result.objects.filter(Test=test).exclude(Student=student)
        number_of_students = attempted_students.count() + 1

        for i in attempted_students:
            if attempted_student.Obtained_Marks <= i.Total_Marks:
                rank += 1
            
        attempted_student.Rank = rank
            
        percentile = ((number_of_students-(rank-1))/number_of_students)*100
        attempted_student.Percentile = percentile
        attempted_student.save()

        # return render(request, 'analysis.html')
        return render(request, 'analysis.html', {'student':attempted_student, 'test':test.id})
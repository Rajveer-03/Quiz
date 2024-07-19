from django.shortcuts import redirect, render
from django.views import View
from ..models.answer import Answer
from ..models.question import Question
from ..models.student import Student
from ..models.test import Test
from ..models.user import User
from ..models.student_attempt import Student_Attempt
from ..models.result import Result as Student_Result

class Result(View):
    def get(self, request):
        return redirect('home')
    
    def post(self, request):
        marks = 0
        correct = 0
        acc = 0
        user = User.objects.get(Email=request.session['user'])
        student = Student.objects.get(Email=user)
        test = Test.objects.get(id=int(request.session['test']))

        answers = {}
        for key in request.POST:
            if key.startswith('question'):
                question_id = key.replace('question', '')
                answers[question_id] = request.POST.getlist(key)[0]


        attempt = len(answers)

        
        for i,j in answers.items():
            question = Question.objects.get(id=int(i))
            ans = Answer.objects.get(id=int(j))

            if(ans.is_Correct):
                marks += question.Marks
                correct += 1
            else:
                marks -= (question.Marks/4)

            student_attempt = Student_Attempt(Student=student, Test=test, Question=question, Answer=ans)
            student_attempt.save()
        
        if(marks!=0):
            acc = (correct/attempt)*100

        result = Student_Result(Test = test, Student=student, Total_Marks = test.Total_Marks, Obtained_Marks = marks, Total_Attempted = attempt, Accuracy = acc )
        result.save()

        return redirect('analysis')

from django.shortcuts import render, redirect
from ..models.test import Test
from ..models.question import Question
from ..models.student import Student
from ..models.user import User
from ..models.student_attempt import Student_Attempt
from django.views import View

class Solution(View):
    def get(self, request):
        return redirect('test_series')
    
    def post(self, request):
        try:
            t = request.POST.get('testid')
            test = Test.objects.get(id=t)
            questions = Question.objects.filter(Test=test).prefetch_related('question')

            user = User.objects.get(Email = request.session['user'])
            student = Student.objects.get(Email=user)  # Assuming the user is logged in and associated with the Student model

            student_attempts = Student_Attempt.objects.filter(Student=student, Test=test)

            questions_with_answers = []
            for question in questions:
                correct_answer = question.question.get(is_Correct=True)
                selected_answer = student_attempts.get(Question=question).Answer if student_attempts.filter(Question=question).exists() else None
                questions_with_answers.append({
                    'question_text': question,
                    'answers': question.question.all(),
                    'correct_answer_id': correct_answer.id,
                    'selected_answer_id': selected_answer.id if selected_answer else None,
                })

            context = {
                'test': test,
                'questions': questions_with_answers,
            }

            return render(request, 'Solution.html', context)






            # t = request.POST.get('testid')
            # test = Test.objects.get(id=t)

            # questions = Question.objects.filter(Test=test).prefetch_related('question')

            # return render(request, 'Solution.html', {'questions':questions})
        except:
            return redirect('test_series')
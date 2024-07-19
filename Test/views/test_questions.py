from django.shortcuts import render, redirect
from ..models.question import Question
from ..models.test import Test
from django.views import View


class Test_Questions(View):
    def get(self, request):
        try:
            test = Test.objects.get(id=int(request.session['test']))

            questions = Question.objects.filter(Test=test).prefetch_related('question')
            q_id = questions[0].id
            data = {
            'f_ques':q_id,
            'test': test,
            'questions': questions,
            'timing': test.Timing
            }

            return render(request, 'test.html', data)
        except:
            return redirect('test_series')
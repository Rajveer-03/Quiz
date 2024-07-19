from django.contrib import admin
from .models.user import User
from .models.student import Student
from .models.answer import Answer
from .models.question import Question
from .models.result import Result
from .models.test import Test
from .models.student_attempt import Student_Attempt
from .models.note import Notes
from .models.catagory import Catagory

class UserAdmin(admin.ModelAdmin):
    list_display = ['Email', 'Password']

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['Name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['Fname', 'Lname', 'Email', 'Contact']

class TestAdmin(admin.ModelAdmin):
    list_display = ['Name']

class NotesAdmin(admin.ModelAdmin):
    list_display = ['Title']

class ResultAdmin(admin.ModelAdmin):
    list_display = ['Test', 'Student', 'Rank', 'Total_Marks', 'Obtained_Marks', 'Accuracy', 'Percentile']
    ordering = ('Student',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['Question', 'Answer']

class AnswerStacked(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['Test', 'Question', 'Marks']
    inlines = [AnswerStacked]

class AttemptAdmin(admin.ModelAdmin):
    list_display = ['Student', 'Test', 'Question', 'Answer']



admin.site.site_header = 'Utkarsh Academy Admin'
admin.site.index_title = 'Tables'
admin.site.site_title = 'HTML title from adminsitration'

admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Student_Attempt, AttemptAdmin)
admin.site.register(Notes, NotesAdmin)
admin.site.register(Catagory, CatagoryAdmin)
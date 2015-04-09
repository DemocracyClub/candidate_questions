from django.contrib import admin
from .models import Question, Answer

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'candidate', 'answer', 'completed')
    list_filter = ('question__question', 'completed')
    search_fields = ('question__question', 'answer', 'candidate__name')

admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)

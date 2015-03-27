
from questions.models import Answer
from django.forms import ModelForm

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']

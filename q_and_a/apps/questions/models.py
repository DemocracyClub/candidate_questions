from django.db import models
from organisations.models import Organisation
from candidates.models import Candidate
from django.forms import ModelForm, Textarea, NullBooleanSelect, RadioSelect
from django.forms.models import modelform_factory

class Question(models.Model):
    TYPES = (
        ('text', 'text'),
        ('bool', 'yes/no'),
        ('options', 'multiple choice'),
    )

    organisation = models.ForeignKey(Organisation)
    question = models.CharField(blank=True, max_length=100)
    type = models.CharField(max_length=8, choices=TYPES, default='text')
    choices = models.CharField(blank=True, max_length=100)
    added = models.DateTimeField(blank=True, auto_now_add=True)
    asked = models.BooleanField(default=False)

    def __unicode__(self):
        text = u"%s" % self.question
        if self.asked:
            text = u"%s (asked)" % text
        return text

    def type_label(self):
        types = dict(self.TYPES)
        if self.type == u'options':
            return types[self.type] + u': ' + self.choices.split()
        return types[self.type]

    def widget(self):
        if self.type == 'text':
            return Textarea()
        if self.type == 'options':
            choices = [(i, i) for i in self.choices.split(',')]
        elif self.type == 'bool':
            choices = [('yes', 'yes'), ('no', 'no')]
        return RadioSelect(choices=choices)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    candidate = models.ForeignKey(Candidate)
    answer = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    completed_timestamp = models.DateField(null=True)

    class Meta:
        unique_together = (('candidate', 'question'),)

    def make_form(self):
        return modelform_factory(Answer,
                                 fields=['answer'],
                                 widgets={'answer': self.question.widget()})()



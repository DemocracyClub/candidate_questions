from django.db import models
from organisations.models import Organisation
from candidates.models import Candidate

class Question(models.Model):
    organisation = models.ForeignKey(Organisation)
    question = models.CharField(blank=True, max_length=100)
    added = models.DateTimeField(blank=True, auto_now_add=True)
    asked = models.BooleanField(default=False)

    def __unicode__(self):
        text = "%s" % self.question
        if self.asked:
            text = "%s (asked)" % text
        return text

class Answer(models.Model):
    question = models.ForeignKey(Question)
    candidate = models.ForeignKey(Candidate)
    answer = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    completed_timestamp = models.DateField(null=True)
    



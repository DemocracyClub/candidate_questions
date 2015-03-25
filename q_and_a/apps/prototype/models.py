from django.db import models
from django.core.urlresolvers import reverse


class Organisation(models.Model):
    name = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organisation', kwargs={'pk': self.id})


class Question(models.Model):
    organisation = models.ForeignKey(Organisation)
    question = models.CharField(blank=True, max_length=100)
    added = models.DateTimeField(blank=True, auto_now_add=True)
    asked = models.BooleanField(default=False)

    def __unicode__(self):
        text =  "%s" % self.question
        if self.asked:
            text = "%s (asked)" % text
        return text

class Answer(models.Model):
    question = models.ForeignKey(Question)
    person_id = models.CharField(blank=True, max_length=100)
    answer = models.TextField(blank=True)

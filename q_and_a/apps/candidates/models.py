from django.db import models
from django.db.models.signals import post_save
from token_auth.models import TokenAuthModel
from django.core.urlresolvers import reverse
from django.conf import settings


class Candidate(TokenAuthModel):
    popit_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    contact_address = models.CharField(null=True, blank=True, max_length=255)
    constituency_id = models.CharField(max_length=20)
    constituency_name = models.CharField(max_length=64)
    party = models.CharField(max_length=64, null=True)
    participating = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.get_questions_url()

    def get_questions_url(self):
        return reverse('candidate_questions', kwargs={'pk': self.popit_id})

    def get_open_question_count(self):
        from questions.models import Answer
        open_questions = Answer.objects.filter(candidate=self,completed=False).count()
        return open_questions

    def assign_questions(self, count):
        """Add empty Answer records for <n> previously unassigned questions.
        Returns the number of questions added."""

        from questions.models import Question,Answer

        # Get questions that have not previously been assigned
        # to this candidate

        new_questions = Question.objects.raw("""SELECT
            questions_question.* 
            FROM questions_question
            LEFT JOIN questions_answer ON 
                questions_answer.question_id = questions_question.id
                AND
                questions_answer.candidate_id = %s
            WHERE questions_answer.id IS NULL
            ORDER BY questions_question.id
            LIMIT %s""", 
            [self.popit_id, count])

        # add up to (new question count) incomplete answers, depending
        # on how many questions are available
        n=0
        for new_question in new_questions:
            answer = Answer()
            answer.candidate = self
            answer.question = new_question
            answer.save()
            n += 1
        # return the number of answers added
        return n
            

def candidate_created_cb(sender, instance, created, **kwargs):
    """post-save hook that automatically lines up questions when
    a new candidate is created"""
    if instance.participating:
        instance.assign_questions(settings.OPEN_QUESTION_TARGET)

post_save.connect(candidate_created_cb, sender=Candidate)

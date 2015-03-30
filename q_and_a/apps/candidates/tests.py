from django.db import IntegrityError
from django.test import TestCase

from django.contrib.auth.models import User
from questions.models import Question,Answer
from organisations.models import Organisation
from candidates.models import Candidate

# Create your tests here.

class TestQuestionAssignment(TestCase):
    def setUp(self):
        # create an organisation
        user = User(username='test_org_user')
        user.save()
        org = Organisation(name='test_org')
        org.user = user
        org.save()

        # create three questions
        self.q1 = Question(question='What is your name?', organisation=org)
        self.q1.save()
        q2 = Question(question='What is your quest?', organisation=org)
        q2.save()
        q3 = Question(question='What is your favourite colour?',organisation=org)
        q3.save()

        # create a candidate
        self.candidate = Candidate(name='Terry', participating=True, popit_id=1234)
        self.candidate.save()

        # assign 1 question to the candidate
        self.answer = Answer(question=self.q1)
        self.answer.candidate = self.candidate
        self.answer.save()

    def test_question_assignment_count(self):
        """Open question count increases when a new question is assigned"""
        self.assertEquals(self.candidate.get_open_question_count(), 1)
        existing = Answer.objects.filter(candidate=self.candidate)
        self.candidate.assign_questions(1)
        self.assertEquals(self.candidate.get_open_question_count(), 2)
        pass

    def test_question_assignment_count_close(self):
        """Open question count decreases when a question is completed"""
        self.assertEquals(self.candidate.get_open_question_count(), 1)
        self.answer.completed=True
        self.answer.save()
        self.assertEquals(self.candidate.get_open_question_count(), 0)
        pass

    def test_question_assignment(self):
        """Questions are assigned in age order"""
        # complete the existing assignment
        self.answer.completed=True
        self.answer.save()
        # assign a new one
        count = self.candidate.assign_questions(1)
        self.assertEquals(count,1)
        newanswer = Answer.objects.filter(candidate=self.candidate,completed=False)[0]
        self.assertEquals(newanswer.question.question, "What is your quest?")

    def test_no_more_questions(self):
        """No more questions are available"""
        self.candidate.assign_questions(2)
        count = self.candidate.assign_questions(1)
        self.assertEquals(count,0)


    def test_unique(self):
        """Question/Answer combinations must be unique"""
        answer = Answer(candidate=self.candidate, question=self.q1)
        self.assertRaises(IntegrityError,answer.save)

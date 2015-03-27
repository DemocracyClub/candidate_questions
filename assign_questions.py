import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'q_and_a.settings'

import q_and_a.settings
from q_and_a.apps.candidates.models import Candidate
from q_and_a.apps.questions.models import Answer,Question

OPEN_QUESTION_TARGET=10

# for each candidate that is participating
for candidate in Candidate.objects.filter(participating=True):
    print candidate
    # get open question count for candidate
    open_questions = Answer.objects.filter(candidate=candidate,completed=False).count()
    if open_questions >= OPEN_QUESTION_TARGET:
        continue
    # find questions that have not already been assigned to this candidate
    new_question_count = OPEN_QUESTION_TARGET - open_questions
    # questions are selected in age order. We could do clever shuffling here to 
    # get a cross-section of questions from different organisations
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
        [candidate.popit_id, new_question_count])

    # add up to (new question count) incomplete answers, depending
    # on how many questions are available
    for new_question in new_questions:
        answer = Answer()
        answer.candidate = candidate
        answer.question = new_question
        answer.save()
        print "Added answer record for {} <=> {}".format(
            candidate, new_question
            )



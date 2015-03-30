from django.core.management.base import BaseCommand, CommandError

from q_and_a.settings import OPEN_QUESTION_TARGET
from candidates.models import Candidate
from questions.models import Answer,Question


class Command(BaseCommand):
    args = ""
    help = "Assigns unanswered questions to candidates"

    def handle(self, *args, **options):
        # for each candidate that is participating
        for candidate in Candidate.objects.filter(participating=True):
            self.stdout.write("Assigning questions for: {}".format(candidate))
            # get open question count for candidate
            open_questions = candidate.get_open_question_count()
            if open_questions >= OPEN_QUESTION_TARGET:
                continue
            # find questions that have not already been assigned to this candidate
            new_question_count = OPEN_QUESTION_TARGET - open_questions

            candidate.assign_questions(new_question_count)
                


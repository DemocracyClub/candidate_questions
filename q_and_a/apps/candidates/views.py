import datetime

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404

from forms import AnswerForm
from models import Candidate
from questions.models import Answer
from token_auth.views import BaseAuthView

class CandidateAuthenticateView(BaseAuthView):
    def get_redirect_url(self, *args, **kwargs):
        if (not self.request.user.is_authenticated()
                or not hasattr(self.request.user, 'candidate_id')):
            self.login()
        return self.request.user.candidate.get_absolute_url()

class CandidateQuestionsView(TemplateView):
    template_name = "candidates/candidate_questions.html"

    def get_context_data(self, **kwargs):
        context = super(CandidateQuestionsView, self).get_context_data(**kwargs)
        context['candidate'] = get_object_or_404(Candidate, popit_id=kwargs['pk'])
        context['answers'] = Answer.objects.filter(candidate=context['candidate'], completed=False)
        return context

class CandidateAnswer(FormView):
    form_class = AnswerForm

    def get_form_kwargs(self):
        kwargs = super(CandidateAnswer, self).get_form_kwargs()
        kwargs.update({'instance': Answer.objects.get(id=self.kwargs['pk'])})
        return kwargs

    def get_success_url(self):
        return self.object.candidate.get_questions_url()

    def form_valid(self, form):
        self.object = form.save()
        self.object.completed = True
        self.object.completed_timestamp = datetime.datetime.utcnow()
        self.object.save()

        return super(CandidateAnswer, self).form_valid(form)

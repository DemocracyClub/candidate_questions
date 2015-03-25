from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from forms import QuestionForm

from .models import Organisation, Question, Answer

class HomePageView(TemplateView):
    template_name = "home.html"

class OrganisationsView(ListView):
    model = Organisation

class OrganisationDetailView(DetailView):
    model = Organisation

    def get_context_data(self, **kwargs):
        context = super(OrganisationDetailView, self).get_context_data(**kwargs)
        context['form'] = QuestionForm
        return context

class AddQuestion(FormView):
    form_class = QuestionForm

    def get_form_kwargs(self):
        kwargs = super(AddQuestion, self).get_form_kwargs()
        kwargs.update({'instance': Question(organisation_id=self.kwargs['org'])})
        return kwargs

    def get_success_url(self):
        return self.object.organisation.get_absolute_url()

    def form_valid(self, form):
        self.object = form.save()
        return super(AddQuestion, self).form_valid(form)

class AllQuestionsView(ListView):
    model = Question

class AllAnswersView(ListView):
    model = Answer

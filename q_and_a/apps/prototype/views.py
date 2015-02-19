from django.views.generic import TemplateView, ListView


from .models import (Organisation, Question, Answer)

class HomePageView(TemplateView):
    template_name = "home.html"

class OrganisationsView(ListView):
    model = Organisation

class AllQuestionsView(ListView):
    model = Question

class AllAnswersView(ListView):
    model = Answer

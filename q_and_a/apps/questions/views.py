from django.views.generic.edit import FormView
from forms import QuestionForm
from .models import Question

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



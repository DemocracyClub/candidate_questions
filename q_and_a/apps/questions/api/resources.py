from tastypie.resources import ModelResource
from questions.models import Answer

class AnswerResource(ModelResource):
    class Meta:
        queryset = Answer.objects.all()
        allowed_methods = ['get']

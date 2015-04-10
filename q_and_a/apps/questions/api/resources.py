import json
from tastypie.resources import ModelResource
from questions.models import Answer
from django.core.serializers.json import DjangoJSONEncoder
from tastypie.serializers import Serializer

# From the Tastypie Cookbook: Pretty-printed JSON Serialization
# http://django-tastypie.readthedocs.org/en/latest/cookbook.html#pretty-printed-json-serialization
class PrettyJSONSerializer(Serializer):
    json_indent = 2

    def to_json(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        return json.dumps(data, cls=DjangoJSONEncoder,
                sort_keys=True, ensure_ascii=False, indent=self.json_indent)

class AnswerResource(ModelResource):
    class Meta:
        queryset = Answer.objects.all()
        allowed_methods = ['get']
        serializer = PrettyJSONSerializer()

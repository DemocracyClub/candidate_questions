from django.contrib import admin

from .models import (Organisation, Question, Answer)

admin.site.register(Organisation)
admin.site.register(Question)
admin.site.register(Answer)
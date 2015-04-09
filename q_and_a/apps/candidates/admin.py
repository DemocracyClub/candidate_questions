from django.contrib import admin
from .models import Candidate

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_address', 'constituency_name', 'party')
    list_filter = ('party', )

admin.site.register(Candidate, CandidateAdmin)

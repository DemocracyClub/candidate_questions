from django.core.management.base import BaseCommand
from candidates.models import Candidate
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string

def make_email(candidate):
    subject = 'Questions for candidates in the 2015 election'
    email_from = 'questions@campaignreply.org'
    to = candidate.contact_address

    text_content = render_to_string('candidates/email.txt', {'candidate': candidate})
    html_content = render_to_string('candidates/email.html', {'candidate': candidate})
    msg = EmailMultiAlternatives(subject, text_content, email_from, [to])
    msg.attach_alternative(html_content, "text/html")
    return msg

class Command(BaseCommand):
    def handle(self, *args, **options):
        candidates_with_email = [candidate for candidate in Candidate.objects.all() if candidate.contact_address]
        reply = raw_input(u'this will e-mail {} candidates, are you sure? [y/n] '.format(len(candidates_with_email)))
        if not reply or reply[0].lower() != u'y':
            return
        messages = [make_email(c) for c in candidates_with_email]
        print 'sending e-mails'
        get_connection().send_messages(messages)

import os
import json
import urllib2
import sys
import csv

os.environ['DJANGO_SETTINGS_MODULE'] = 'q_and_a.settings'

import q_and_a.settings
from q_and_a.apps.candidates.models import Candidate
from django.contrib.auth import get_user_model

def load_from_csv():
    filename = sys.argv[1]

    csv_file = csv.reader(open(filename))
    headings = csv_file.next()
    User = get_user_model()
    for row in csv_file:
        record = dict(zip(headings, row))
        try:
            testrec = Candidate.objects.get(popit_id=record['id'])
            print "Skipping: ", testrec.name
            continue
        except Candidate.DoesNotExist:
            pass
        user = User(username="candidate-" + record['id'])
        user.save()
        candidate = Candidate(
            popit_id=record['id'],
            user=user,
            name=record['name'].decode('utf-8'),
            contact_address=record['email'].decode('utf-8'),
            constituency_id=record['mapit_id'],
            constituency_name=record['constituency'].decode('utf-8'),
            party=record['party'].decode('utf-8'))
        candidate.save()
        print u"Added: {} ({}, {})".format(candidate.name, candidate.party, candidate.constituency_name)


def load_from_api():
    url = "http://yournextmp.popit.mysociety.org/api/v0.1/search/persons?q=_exists_:standing_in.2015.post_id&page=16"

    while url:
        print "Fetching url: ", url
        fp = urllib2.urlopen(url)
        data = json.load(fp)
        fp.close()
        for record in data['result']:
            try:
                testrec = Candidate.objects.get(popit_url=record['url'])
                print "Skipping: ", testrec.name
                continue
            except Candidate.DoesNotExist:
                pass

            candidate = Candidate(
                name=record['name'],
                contact_address=record['email'],
                popit_url=record['url'],
                constituency_id=record['standing_in']['2015']['post_id'],
                constituency_name=record['standing_in']['2015']['name'],
                party=record['party_memberships']['2015']['name'])
            candidate.save()
            print u"Added: {} ({}, {})".format(candidate.name, candidate.party, candidate.constituency_name)
        if 'next_url' not in data:
            break
        url = data['next_url']

if __name__ == '__main__':
    load_from_csv()

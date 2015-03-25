import os
import json
import urllib2

os.environ['DJANGO_SETTINGS_MODULE'] = 'q_and_a.settings'

import q_and_a.settings
from q_and_a.apps.prototype.models import Candidate

url = "http://yournextmp.popit.mysociety.org/api/v0.1/search/persons?q=_exists_:standing_in.2015.post_id&page=16"

while url:
	print "Fetching url: ", url
	fp = urllib2.urlopen(url)
	data = json.load(fp)
	for record in data['result']:
		try:
			testrec = Candidate.objects.get(popit_url=record['url'])
			print "Skipping: ", testrec.name
			continue
		except Candidate.DoesNotExist:
			pass

		candidate = Candidate(
			name = record['name'],
			contact_address = record['email'],
			popit_url = record['url'],
			constituency_id = record['standing_in']['2015']['post_id'],
			constituency_name = record['standing_in']['2015']['name'],
			party = record['party_memberships']['2015']['name'],
			)
		candidate.save()
		print u"Added: {} ({}, {})".format(candidate.name, candidate.party, candidate.constituency_name)
	if 'next_url' not in data:
		break
	url = data['next_url']


# -*- coding: utf-8 -*-
from lettuce import *
from lettuce.django import django_url

from organisations.tests.test_authenticate import make_organisation

@before.each_feature
def setup_orginisation(server):
    world.orginisation = make_organisation('111')


@step(u'Given that I have received an invitation to use the site')
def received_invitation(step):
    """
    Stub, as we can't really test this.
    """
    assert True

@step(u'When I follow the instructions in the invitation')
def click_token_link(step):
    world.browser.visit(django_url('/organisations/authenticate/111/'))
    assert world.browser.status_code.code in [301, 200]

@step(u'I am taken to the Questions List')
def view_questions_list(step):
    assert world.browser.html == "QUESTIONS"

@step(u'Given that I have identified myself to the site previously by following the instructions I received in an invitation')
def given_that_i_have_identified_myself_to_the_site_previously_by_following_the_instructions_i_received_in_an_invitation(step):
    return click_token_link(step)

@step(u'Then I am authenticated and identified automatically')
def then_i_am_authenticated_and_identified_automatically(step):
    assert 'sessionid' in world.browser.cookies.all()

@step(u'When I visit the site subsequently \(going directly, without necessarily following those instructions\)')
def when_i_visit_the_site_subsequently_going_directly_without_necessarily_following_those_instructions(step):
    return view_questions_list(step)

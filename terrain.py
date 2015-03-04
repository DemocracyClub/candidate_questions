from lettuce import *
from splinter.browser import Browser

@before.harvest
def initial_setup(server):
    world.browser = Browser('django')

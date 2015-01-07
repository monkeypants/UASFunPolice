#!/usr/bin/env python
from ontology import *

# these could be factory/singleton patterns
#ucp_cat = UCPCatalogue()
#uc_cat = UCCatalogue()

######################
# Requirements model
#
ucp_manage_account = ucp('manage account','Manage Account')
ucp_manage_org = ucp('manage organisation', 'Manage Organisation')

uc_register_new_org = use_case(
    ucp_manage_org, 'register organisation', 'Register Organisation')

anon_visitor = actor('anon_visitor', 'Anonymous website visitor')
auth_user = actor('auth_user','Authenticated website user')

# for <<is-a>> relationships between actors/nouns
# iterate over scenarios and call alternate_actor()
# unless explicit forbidden relationship exists
# - do we require a second type of alternate? so we
# can chunk up "as a foo, you extend bar" rather than
# repeating all bar for foo?
# resolve that later, with RDF/logic program version.

#######################
# Feature Language
#
new_organisation = noun('new organisation','Newly registered organisation')
org_registration_page = noun('org registration page','Organisation registration page')
create = verb('create', 'Create')

#HIA artefacts
hia_report = noun('HIA report', 'Hazard, Incident or Acident submission')
hia_media = noun('HIA media', 'Media supporting an HIA report')
hia_url = noun('HIA URL', 'URL supporting an HIA report')

s = scenario(
    uc_register_new_org,
    create, new_organisation, org_registration_page,
    "Register new organisation on the orginastion registration page",
    auth_user)
#s.alternate_actor(manager)
s.given('I access the "org_registration" page')
s.then('and I fill in valid details (TODO: elaborate)')
s.and_('I click the submit button')
s.then('I a see the "org_created" page')
s.and_('the new organisation is created in the database')
s.and_('I am the only organisation manager of the new organisation')
s.and_('I can assign other orgamisation managers to the new organisation')
s.and_('I can assign other members to the new organisation')

s.sad_given('I try something naughty')
s.sad_then('nothing happens')


if __name__ == "__main__":
    runapp()

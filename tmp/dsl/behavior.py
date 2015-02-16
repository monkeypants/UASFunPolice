#!/usr/bin/env python
from ontology import *

######################
# Requirements model
#

#TODO: load the *.ucp files
'''
for foo_bar in glob ./*.ucp:
    var_name = "ucp_foo_bar"
    obj_reference = "foo bar"
    obj_heading = "Foo Bar"
    obj_description = everything after the first blank line of `cat foo_bar.ucp`

    eval("""%s = ucp('''%s''', '''%s''', '''%s''')""" % (
        var_name, obj_reference, obj_heading, obj_description))
'''

import glob
for fname in glob.glob('*.ucp'):
    print fname

uc_submit_hazard_report = use_case(
    ucp_submit_report_to_safety_team,
    'submit hazard report',
    'Submit Hazard Report',
    '''A hazard is the potential for an incident or accident. The risk is percieved, the hazard report is simply an issue or problem for the safety team to evaluate, with some potential to improve safety.

The submitter may request that the Hazard report is treated in-confidence. In this situation, the safety team may disclose "lessons learned" and other topics related to the hazard, but keep the specifics of the hazard report private (for example, who reported it and exactly when).''')

uc_submit_accident_report = use_case (
    ucp_submit_report_to_safety_team,
    'submit accident report',
    'Submit Accident Report',
    '''An accident is an incident with bad consequences. For example, personal injury significant damage to equipment.

The safety team will investigate all reported accidents. As appropriate, they will also forward the accident report to relevant parties and authorities. It may not be possible to agree to keep accident reports confidential, however if requested the safety team can assure maximum possible discretion (as oposed to discussing the accident openly).

Note the accident reporting process should have a wizard-like start, and when appropriate, direct the reporter to postpone submitting an organisational accident report until after they have fulfilled their obligations with the national transport safety processes''')

uc_submit_incident_report = use_case(
    ucp_submit_report_to_safety_team,
    'submit incident report',
    'Submit Incident Report',
    '''An incident is something that actually happened (at a time and place). Nobody was hurt, nothing was significantly damaged, but a percieved risk was validated by events.

The safety team will investigate every reported incident, using the same sort of analysis as used for more serious accidents. The investigation will generally be conducted internaly (within the Safety Team), without resorting to external parties. Where appropriate, incident investigations may be reviewed by a third party, for example by an aviation safety auditor.

Submitters may request that an incident report is kept confidential. In this case, the details of the incident report will be discussed among the safety team. It may also be shared with appropriate third parties, but it will not be released into the public domain. The safety team may disclose "lessons learned" and other non-specific details, but keep the specifics of the incident report private.

If a submitter nominates that they do not wish for the incident report to be kept private, the safety team may release it into the public domain at their discression.''')

uc_directly_attach_media_to_an_hia_report = use_case(
    ucp_suppliment_hia_report,
    'directly attach media files to an HIA report',
    'Directly Attach Media Files to an HIA Report',
    '''At the time a HIA report is submitted, the submitter may attach media files directly. For example, attach them to an email that they send to an HIA report submission inbox, or use upload features of the online HIA reporting tool. Where practical to do so, this would usually be the preferred method.''')

uc_link_media_to_an_hia_report = use_case(
    ucp_suppliment_hia_report,
    'link media to an HIA report',
    'Link Media to an HIA Report',
    '''At the time a HIA report is submitted, the submitter may include hyperlink references to media hosted elseware, such as youtube videos or droneshare telemetry. Where this media is password protected, the sumitter would need to provide access credentials.

In some situations this might be the most practical way to provide supplimentary data, for example where a significantly large volume of data were involved, or where the origional source material is not available to the submitter. However, the downside of hyperlinks to remotely hosted data is that it may cease to be available at some point in the future, making future reviews or audits more difficult.''')    

uc_provide_supplimentary_data_after_hia_report_submission = use_case(
    ucp_suppliment_hia_report,
    'provide supplimentary data after HIA report submission',
    'Provide Supplimentary Data after HIA Report Submission',
    '''Either at the request of the safety team or unprompted, a HIA report submitter may chose to augment a HIA report with supplimentary data after the report has been submitted. This may be linked media or directly attached files.''')

uc_manage_system_configuration = use_case(
    ucp_administer_system,
    'manage system configuration',
    'Manage System Configuration',
    '''Basically, modifying the behavior of the software by changing settings. What software? What behavior? What settings? Who knows?

This is a supporting use-case package, it does not directly improve safety.

If we are changing the behavior of the system, we will require some sort of governance arangement (to analyse impacts of changes on users). This will also require record keeping that is auditable.''')

uc_manage_equipment = use_case(
    ucp_administer_system,
    'manage equipment',
    'Manage Equipment',
    '''This is a placeholder, in anticipation that we will need to manage some information about the equipment we use. A supporting use-case package.''')

uc_manage_people_and_groups = use_case(
    ucp_administer_system,
    'manage people and groups',
    'Manage People and Groups',
    '''The SMS is comprised of processes and systems to make the enterprise safer. Those systems are used by people. People participate in those processes (probably with explicit roles).

Manage people includes manage accounts / access control to the systems.

If we end up designing a multi-tennanted solution, we may well need a concept of "groups" as in, each person may belong to zero or more groups, and people can create/join/leave groups.''')


anon_visitor = actor(
    'anon_visitor',
    'Anonymous website visitor')

auth_user = actor(
    'auth_user',
    'Authenticated website user')

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
    uc_manage_people_and_groups,
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

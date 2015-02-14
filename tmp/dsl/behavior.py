#!/usr/bin/env python
from ontology import *

######################
# Requirements model
#

# Management Requirements

ucp_promote_safety = ucp(
    'promote safety', # label used in prose
    'Promote Safety', # label used in headings, followed by description
    '''Management requirement:
 * Follow up on incidents, accidents and hazards by creating agenda items for group meetings (e.g. the Monday Mumble session).
 * Publish, distribute and promote relevant artefacts.

CanberraUAV is a self-organising, non-profit group "staffed" by volenteers that work on open source research and development projects. We are a registerd community organisation with a bank account and a comittee (etc), but we do not have a command structure or hirarchy like a conventional organisation.

The cultural context of self-organised community groups is a significant factor in the way we can promote safety. There is very little scope for authoratitave mandates. The communication strategies most likely to succeed will involve the safety management system (and team) continuously demonstrating the merits of their activities.
''')

ucp_improve_safety = ucp(
    'improve safety',
    'Improve Safety',
    '''Management requirement. This is where we figure out what needs to be done and do it. It's a continuous improvement, closed-loop feedback process.

It probably involves improving policies and procedures, initiating cultural change as well as other safety-improving actions.

One idea is to utilise a ticketing system (such as GitLab) for safety issues, which are referenced (or even closed) by changes to policy and procedure documentation in a version control system (such as git).''')

ucp_asses_safety = ucp(
    'assess safety',
    'Assess Safety',
    '''Management requirement. Opreational data (including planned activity) is systematically reviewed, evaluated, discussed and analysed in a timely fashion. The results of this work is fed into safety improving and promoting activities.''')

# OK, I'm really sick of typing the same thing three times in a row.
# I should type it once in a yaml file or something, then use code to type it thrice
# or even, one file extension class (e.g. foo.use_case_package),
# where the foo is the thrice-typed bit
# and the lines before the first blank line are the positional parameters.
# (or maybe with "paramname: paramvalue" for easier reading) 

# Operational requirements
ucp_plan_standard_operations = ucp(
    'plan standard operations',
    'Plan Standard Operations',
    '''There is probably a standard set of generic procedures, and activities that comply with those procedures might not require aditional planning. They are performed at the operators discression and the activity is recorded after the fact. Changes to these procedures would be subject to safety assessment.

For example, CanberraUAV flys multiple missions most weeks at the CMAC airfield. These usually involve flight testing incremental changes to software, airframes or avionics. These flights comply with the range safety plan of the CMAC site, and the Standard Operating Procedures of the Model Aircraft Association of Australia. They are usually observed by a gallery of experienced aeromodellers and always flown by a suitably qualified safety pilot.

It would be difficult and disruptive to impose manditory planning steps to Standard Operations such as these.
''')

ucp_plan_extraordinary_operations = ucp(
    'plan extraordinary operations',
    'Plan Exteraordinary Operations',
    '''Extraordinary activity is defined as anything outside the bounds of Standard Operations. These require advanced planning, which is subject to safety assessment prior to activity occuring. New standard operations would be subject to equivalent process as extraordinary activities.

The activity planning domain probably inclueds concepts like:

 * range safety plan
 * class of airspace
 * class of activity

The scope of the risk assessment associated with activity planning is greater than safety; it also includes risks related to regulatory compliance, financial, reputation and others. We probably need to link up to a "risk management plan" framework of which safety management is a subset.''')

ucp_record_activity = ucp(
    'record activity',
    'Record Activity',
    '''Activity is recorded in a number of contexts:

 * workshop (construction/maintenance)
 * flight planning
 * packing and unpacking equipment from transport/storage
 * pre-flight checking
 * telemetry/telecommand/payload data
 * post-flight checking
 * communication logs
 * incident/accident management

Some activities must be very simple (low effort) to record. For example, upload telemetry/telecommand log files along with the absolute minimum of information. To the maximum extend possible, this sort of information management should be handled automatically.

The complicated cases include all the incident, accident and hazard reporting features.

This will not be limited to flight operation activities. Inspection and maintenance of equipment. Maybe even our meeting minutes belong here. Much to elaborate on...''')

ucp_submit_report_to_safety_team = ucp(
    'submit a report to the safety team',
    'Submit a Report ro the Safety Team',
    '''Typically this would be done by a UAS operator, but the safety team would accept reports from anyone.

A report might be submitted automatically as part of a flight log post-processing activity, or it might be submitted manually on other channels.''')

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

ucp_suppliment_hia_report = ucp(
    'suppliment HIA report with additional data',
    'Suppliment HIA Report with Additional Data',
    '''Hazards, Incidents and Accidents are reported using a standard form, becuase it prompts the submitter to provide certain details that are considered useful a-priori. Where available, it may be beneficial to include additional data to augment the information in the standard form. For example telemetry logs, video and still images, audio, diagrams, journalism references, additional witness statements, etc. Unlike the fields of the standard form, these are essentially unstructured data.''')

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

ucp_anonymously_report_concerns = ucp(
    'anonymously report concerns',
    'Anonymously Report Concerns',
    '''Anonymous reporting has a crucial role in aviation safety. The functional requirements are simple - anyone can report a hazard or incident (concern) anonymously, and these will be (at the very least) reviewed and considered by the safety management team.

This might be slightly more complicated than it seems at first:

 * If the incident involved loss of life or other very serious consequences, and the Australian Transport Safety Beuro (or equivalent authority in foreign jurisdictions) are required to investigate, then it is better if we are able to break anonaminity. If this subjective opinion withstands community debate, then something like a psudoanonymous remailer (type 0) is actually preferable to something with strong identity confidentiality.
 * It would be better if the safety team could engage in a dialog with the anonymous reporter (without breaking psudoanyminity), with follow up questions etc. This requirement rules out Mixmaster and Cypherpunk remailers (types I and II remailers).
 * The process of submitting an anonymous report should be trivially simple. For example "send a message to the safety team anonymous reporting email address". This rules out a Mixminion remailers, unless some intermediate (trusted) component recieved the email from conventional email relays, then did the mixing/SURB stuff on the reporter's behalf. That kind of defeats the point, but if it could be trusted then it woud potentially meet all requirements.

''')


ucp_administer_system = ucp(
    'administer system',
    'Administer System',
    '''We assume there will be administrative tasks that support operations and management. We are not really sure what they are yet...''')

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

Requirements
============

I will attempt to capture important quality requirements with prose, interspersed throughout the documentation. 

At a high level, the functional requirements will be described as a number of packages that group related use-cases together (use-case packages). Detailed individual use-cases will eventually be described, including who participates in them and how.

Note that in the testing documentation, individual use-cases will be validated with one or more scenarios. Some scenarios will attempt to reflect the significant messyness of real life, while other's will be deliberately simplified for the sake of clarity. These scenarios will "explain by demonstration" what the use-case is about, and also serve to drive (automated) functional tests.

The use-case packages grouped into operational, management and administrative categories.

Operational:
 * plan activity
 * record activity
 * anonymously report concerns

Management:
 * assess safety
 * improve safety
 * promote safety

Administrative:
 * manage system configuration
 * manage equipment
 * manage people

Throughout this document, the <<UCP>> steryotype will be used to denote that something is a Use Case Package (optionally, as <<UCP:FOO>> where FOO is the use case package grouping).

<<UCP:Operational>> Plan Activity
---------------------------------
All recorded activity occurs agains some kind of plan.

There is probably a standard set of generic procedures, and activities that comply with those procedures might not require aditional planning. They are performed at the operators discression and the activity is recorded after the fact. Changes to these procedures would be subject to safety assessment.

There are probably types of extraordinary activity that are not covered by the standard procedures. These require advanced planning, which is subject to safety assessment prior to activity occuring. New standard procedures are would be subject to equivalent process as extraordinary activities.

The activity planning domain probably inclueds concepts like:
 * range safety plan
 * class of airspace
 * class of activity

The scope of the risk assessment associated with activity planning is greater than safety; it also includes risks related to regulatory compliance, financial, reputation and others. We probably need to link up to a "risk management plan" framework of which safety management is a subset.


<<UCP:Operational>> Record Activity
-----------------------------------
The simplest case must be very, very simple. For example, upload machine flight log files along with the absolute minimum of information. as much information as possible should be parsed from the logs automatically, minimising human intervention. This could probably be done via UI and/or API for truely hands-free operation.

The complicated cases include all the incident, accident and hazard reporting features.

This will not be limited to flight operation activities. Inspection and maintenance of equipment. Maybe even our meeting minutes belong here. Much to elaborate on...


Submit a report to the Safety Team
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Typically this would be done by a UAS operator, but the safety team would accept reports from anyone. In other words, it might be reported when flight logs were uploaded, or it might be reported independant of uploading flight logs.


Report a Hazard
^^^^^^^^^^^^^^^

A hazard is the potential for an incident or accident. The risk is percieved, the hazard report is simply an issue or problem for the safety team to evaluate, with some potential to improve safety.

The submitter may request that the Hazard report is treated in-confidence. In this situation, the safety team may disclose "lessons learned" and other topics related to the hazard, but keep the specifics of the hazard report private (for example, who reported it and exactly when).


Report an Incident
^^^^^^^^^^^^^^^^^^

An incident is something that actually happened (at a time and place). Nobody was hurt, nothing was significantly damaged, but a percieved risk was validated by events.

The safety team will investigate every reported incident, using the same sort of analysis as used for more serious accidents. The investigation will generally be conducted internaly (within the Safety Team), without resorting to external parties. Where appropriate, incident investigations may be reviewed by a third party, for example by an aviation safety auditor.

Submitters may request that an incident report is kept confidential. In this case, the details of the incident report will be discussed among the safety team. It may also be shared with appropriate third parties, but it will not be released into the public domain. The safety team may disclose "lessons learned" and other non-specific details, but keep the specifics of the incident report private. 

If a submitter nominates that they do not wish for the incident report to be kept private, the safety team may release it into the public domain at their discression,


Report an Accident
^^^^^^^^^^^^^^^^^^

An accident is an incident with bad consequences. For example, personal injury significant damage to equipment.

The safety team will investigate all reported accidents. As appropriate, they will also forward the accident report to relevant parties and authorities. It may not be possible to agree to keep accident reports confidential, however if requested the safety team can assure maximum possible discretion (as oposed to discussing the accident openly).


Suppliment HIA reports with additional data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hazards, Incidents and Accidents are reported using a standard form, becuase it prompts the submitter to provide certain details that are considered useful a-priori. Where available, it may be beneficial to include additional data to augment the information in the standard form. For example telemetry logs, video and still images, audio, diagrams, journalism references, additional witness statements, etc. Unlike the fields of the standard form, these are essentially unstructured data.


Directly attach media files to an HIA report
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the time a HIA report is submitted, the submitter may attach media files directly. For example, attach them to an email that they send to an HIA report submission inbox, or use upload features of the online HIA reporting tool. Where practical to do so, this would usually be the preferred method.


Link media to an HIA report
^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the time a HIA report is submitted, the submitter may include hyperlink references to media hosted elseware, such as youtube videos or droneshare telemetry. Where this media is password protected, the sumitter would need to provide access credentials.

In some situations this might be the most practical way to provide supplimentary data, for example where a significantly large volume of data were involved, or where the origional source material is not available to the submitter. However, the downside of hyperlinks to remotely hosted data is that it may cease to be available at some point in the future, making future reviews or audits more difficult.


Provide supplimentary data after submission
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Either at the request of the safety team or unprompted, a HIA report submitter may chose to augment a HIA report with supplimentary data after the report has been submitted. This may be linked media or directly attached files.



<<UCP:Operational>> Anonymously Report Concerns
-----------------------------------------------
At the very least, these will be reviewed and considered by the safety management team.


<<UCP:Management>> Assess Safety
--------------------------------
Opreational data (including planned activity) is systematically reviewed, evaluated, discussed and analysed in a timely fashion. The results of this work is fed into safety improving and promoting activities.


<<UCP:Management>> Improve Safety
---------------------------------
This is where we figure out what needs to be done and do it. It's a continuous improvement, closed-loop feedback process.

It probably involves improving policies and procedures, initiating cultural change as well as other safety-improving actions.

One idea is to utilise a ticketing system (such as GitLab) for safety issues, which are referenced (or even closed) by changes to policy and procedure documentation in a version control system (such as git).


<<UCP:Management>> Promote Safety
---------------------------------

Follow up on incidents, accidents and hazards by creating agenda items for group meetings (e.g. the Monday Mumble session)

Publish, distribute and promote relevant artefacts.

Other stuff too - please elaborate!


<<UCP:Administrative>>Manage System Configuration
-------------------------------------------------
Basically, modifying the behavior of the software by changing settings.

There will certainly be global settings of one kind or another, i.e. settings that apply to the whole system. There may be settings that apply to an individual person or to a group.

This is a supporting use-case package, it does not directly improve safety.


<<UCP:Administrative>>Manage Equipment
--------------------------------------
This is a placeholder, in anticipation that we will need to manage some information about the equipment we use. A supporting use-case package.


<<UCP:Administrative>>Manage People
-----------------------------------
this might be "people and groups" if we end up with some sort of multi-tennanted solution (i.e. the "groups" would be the tennants). Maybe one person could be a member of multiple groups... A supporting use-case package.


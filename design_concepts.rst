Design Concepts
===============

HIA (Hazard, Incident, Accident)
--------------------------------


HIA Artefacts
^^^^^^^^^^^^^
Three kinds:
   * Report Submission
   * Supporting Media
   * Supporting URL


HIA Involvement
^^^^^^^^^^^^^^^
TODO, elaborate:
   * Person
   * HIA_Role
   * Involvement: HIA_Role --< Involvement >-- HIA
   * Involved: Person --< Involved >-- Involvement


Team
----

UAS Operation, the group with the SMS:
 * HIA >-- Team
 * Vehicle >-- Team
 * TeamRole: Safety Officer, Chief Pilot, etc.
 * Team --< TeamInvolvement >-- TeamRole
 * TeamInvolvement --< TeamInvolved >-- Person

Note on Teams:
 * system may be configured as multi-tenanted solution (software as a service, multiple teams)
 * system may be configured for a single team, "self-hosted" configuration
 
Privacy
-------

Private: only visible to the Team's Chief Pilot and Safety Officer(s). Note local laws may require the Chief Pilot to report all data on certain accidents to authorities.

Public: may be published, at Chief Pilot or any Safety Officer's discression.

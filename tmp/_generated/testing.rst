.. _testing:

Testing / Acceptance Criteria
=============================

Functional requirements are documented as scenarios. For convenience
during testing, these are organised by Actor, then Use Case.



auth_user - Register Organisation
---------------------------------

auth_user has COUNT-ME allowable and COUNT_ME dissallowed scenarios for Register Organisation.



.. _(auth_user) Register new organisation on the orginastion registration page:

Scenario: (auth_user) Register new organisation on the orginastion registration page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Actor: :ref:`auth_user`

Acceptance criteria for :ref:`Create the Newly registered organisation on the Organisation registration page`




Steps:

 * Given I access the "org_registration" page
 * Then and I fill in valid details (TODO: elaborate)
 * And I click the submit button
 * Then I a see the "org_created" page
 * And the new organisation is created in the database
 * And I am the only organisation manager of the new organisation
 * And I can assign other orgamisation managers to the new organisation
 * And I can assign other members to the new organisation



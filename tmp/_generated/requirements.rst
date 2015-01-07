.. _requirements:

Requirements
============




.. _Register Organisation:

Manage Organisation - Register Organisation
-------------------------------------------

Package: Manage Organisation

Use-case: Register Organisation



.. graphviz::

   digraph d {
      rankdir="LR";
      label="Register Organisation";
      // verbs
      code_7e13cda97075c705ee3335ed80fec87f [shape="ellipse" label="Create"]
      
      // nouns
      code_2437b7905b7bcddbc575d60c0b152a8b [shape="rectangle" label="Organisation registration page"];
      code_63981274e806820353354efb33cef1a4 [shape="rectangle" label="Newly registered organisation"];
      
      // acted on
      
        code_7e13cda97075c705ee3335ed80fec87f -> code_2437b7905b7bcddbc575d60c0b152a8b'
        code_7e13cda97075c705ee3335ed80fec87f -> code_63981274e806820353354efb33cef1a4;
      
   }


.. toctree::


   features/Create_the_Newly_registered_organisation_on_the_Organisation_registration_page.rst



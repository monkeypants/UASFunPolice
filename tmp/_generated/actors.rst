Actors
======

For the purpose of this dicument, an **actor** is defined
as a type of person that interacts with the system. It's related to the concept
of *roles*, but while one person may have multiple roles, they can only ever be
a single type of actor. The distinction may not be quite so clean cut in general
use, but this is how the term *actor* is used in this document.

Actor definitions are an element of defining how the system is
expected to behave in different situations (including system security / 
access control).


2 types of actor have been specified:

 * anon_visitor
 * auth_user





.. _anon_visitor:

anon_visitor
------------




**Analysis Required**: anon_visitor inadequately described (no or empty description).



An **anon_visitor** has been defined, but they can not perform any actions yet.

**MORE ANALYSIS REQUIRED**




.. List scenarios by Verb




.. _auth_user:

auth_user
---------




**Analysis Required**: auth_user inadequately described (no or empty description).



The **auth_user** can only perform one type action; Create



.. graphviz::

   digraph d {
      rankdir="LR";
      label="Allowable actions for auth_user";
      node [shape="ellipse"];

      actor [label="auth_user" shape=rectangle];
      
      code_7e13cda97075c705ee3335ed80fec87f [ label="Create"];
      actor -> code_7e13cda97075c705ee3335ed80fec87f;
      
   }


.. List scenarios by Verb


.. _auth_user - Create:

auth_user - Create
^^^^^^^^^^^^^^^^^^


From 1
subject,
:ref:`auth_user` is allowed to :ref:`Create`
to 1 
predicate. 




.. graphviz::

   digraph d {
      rankdir="LR";
      node [shape="rectangle"];

      action [label="Create" shape=ellipse];
      
      code_2437b7905b7bcddbc575d60c0b152a8b [ label="Organisation registration page"];
      code_63981274e806820353354efb33cef1a4 [ label="Newly registered organisation"];
      
      code_2437b7905b7bcddbc575d60c0b152a8b -> action;
      
      action -> code_63981274e806820353354efb33cef1a4;
      
   }



Create features that auth_user is allowed to action:

 * :ref:`Create the Newly registered organisation on the Organisation registration page`








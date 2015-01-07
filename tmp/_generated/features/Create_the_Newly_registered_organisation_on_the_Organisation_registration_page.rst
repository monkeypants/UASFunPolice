
.. _Create the Newly registered organisation on the Organisation registration page:

Feature: Create the Newly registered organisation on the Organisation registration page
=======================================================================================

.. graphviz::

   digraph d {
      rankdir = "LR";
      node [shape="rectangle"];
      action [label="Create" shape="ellipse"];
      result [label="Newly registered organisation"];
      object [label="Organisation registration page"];
      object -> action -> result;
   }


Use Case: :ref:`Register Organisation`

Action: :ref:`Create`

Result: :ref:`Newly registered organisation`

Object: :ref:`Organisation registration page`


There are 1
actor
with access to this feature:

 * :ref:`auth_user`


Scenarios (business accetpance criteria):

 * :ref:`(auth_user) Register new organisation on the orginastion registration page`

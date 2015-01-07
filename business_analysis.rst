Domain Model
============

Vehicle Configuration
---------------------

Overall picture (package diagram) of vehicle management database.

.. graphviz::

   digraph d {
      node [shape="folder"];
      ts [label="Aircraft\nType\nSpecification"];
      inv [label="Component\nInventory"];
      qal [label="Component\nQA Log"];
      cfg [label="Aircraft\nConfiguration\nData"];

      cfg -> inv;
      cfg -> ts;
      inv -> ts;
      qal -> inv
   }


Aircraft Type Specification

.. graphviz::

   digraph d {
      node [shape=rectangle];
      edge [arrowhead=crow];
      SystemType -> SystemType;
      SystemType -> QARule;
      SystemType ->ComponentTypeAppropriateness;
      ComponentType -> ComponentTypeAppropriateness;
   }

SystemType
^^^^^^^^^^

The core of the Aircraft Type Specification is the **SystemType**. The key concept here is that a system can be composed of subsystems, which are themselves systems that can be composed of subsystems (etc). A particular aircraft type specification is a tree of nested subsystems, implemented as a recursive "parent" relationship ("pig ear").

The top level node (which has no parent) is the aircraft type. Parentless nodes are totally unrelated from each other, and the model can hold an arbitrary number of aircraft types. Parentless nodes have no SemVer attribute, because they are abstract.

First generation nodes (with parentless parents) are concrete specifications of their abstract type. They must be semantically labeled with a non-nul SemVer attribute that is unique to the abstract type (but not globally unique, two versions may have the same SemVer attribute value if they are of a different abstract type).

Nodes of "greater than first generation" (whose parents have parents) form a subsystem hirarchy for that version of the abstract type. Where a subsystem has no children, we call it a component. Components and subsystems may optionally have non-nul SemVer attributes (why? because it's harmless, and potentially useful).

.. graphviz::

   digraph d {
      node [shape=rectangle]
      label="Example Aircraft Type Specification (simplified)"
      rankdir=LR;
      act [label="<<abstract type>>\nAcme Surveywing"];
      acv [label="<<version>>\nAcme Surveywing v0.1.4-beta"];
      act -> acv;
      wing [label="<<subsystem>>\nwing"];
      acv ->wing;
      Lservo [label="<<component>>\nleft elevon servo"];
      Rservo [label="<<component>>\nright elevon servo"];
      wing -> Lservo;
      wing -> Rservo;
      WSScout [label="<<component>>\nWindrider Scout\n(COTS chevron combat wing)"];
      wing -> WSScout;
      pod [label="<<subsystem>>\nrobotic pod"];
      acv -> pod;
      fuse [label="<<component>>\nfuselage"];
      pod -> fuse;
      av [label="<<subsystem>>\navionics"];
      pod -> av;
      rx [label="<<component>>\nRC reciever"];
      av -> rx;
      ap [label="<<component>>\nautopilot"];
      av -> ap;
      gps [label="<<component>>\nGPS"];
      av -> gps;
      modem [label="<<component>>\nmodem"];
      av -> modem;
      payload [label="<<subsystem>>\npayload"];
      pod -> payload;
      camera [label="<<component>>\ncamera"];
      payload -> camera;
      gimbal [label="<<component>>\ngimbal"];
      payload -> gimbal;
      ccomp [label="<<component>>\ncompanion computer"];
      payload -> ccomp;
   }


ComponentType and ComponentTypeAppropriateness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A **ComponentType** is an unambiguous specification of a physical kind of thing, for example a specific make and model of camera.

A **ComponentTypeAppropriateness** is a rule that says a ComponentType explicitly can (or explicitly can not) be employed in the role of a SystemType. For example, a particular make and model of camera is appropriate for the payload subsystem of the robotic pod of an Acme Surveywing v0.1.4-beta.

QARule
^^^^^^

Aircraft Types have a set of Quality Assurance Rules (QARules) that drive the behavior of checklist and maintenance systems. These may be bound to the abstract type (e.g. pilot certification), specific component (e.g. specific maintenance requirement) or any subsystem inbetween.

QARules probably form their own type hirarchy, but it requires more analysis. For example, something like this:

.. graphviz::

   digraph d {
      node [shape=ellipse];
      rankdir = LR;
      QARule -> check;
      check -> pre;
      pre -> assembly;
      pre -> flight;
      pre -> dissassembly
      check -> post;
      post -> assembly;
      post -> flight;
      post -> dissassembly;
      QARule -> maintenance;
      maintenance -> inspection;
      maintenance -> service;
   } 

QARules would be critical or non-critical. Failing a critical rule prevents takeoff, failing a non-critical rule results in a warning.

Checks would be assembled into checklists that are incorporated into operating procedures.

Maintenance rules would assessed against maintenance logs, resulting in warnings/blocks before flight (preflight checklist integration), post-flight alerts of maintenance falling due as a result of operational activity, as well as fleet management views that indicating upcoming maintenance requirements.
 

ComponentInventory
------------------

This is like an asset register of uniquely identified physical items. The items are of ComponentType.

Note that it is possible to posess Components (in the ComponentInventory) that are of a ComponentType that is not appropriate for any aircraft type specification. i.e. any type of stuff can be recorded on the asset register, even if it's not usefull.

ComponentQALog
--------------

This is a list of things that happened (to Components), which coresponds to QARules being followed.

.. graphviz::

   digraph d {
      node [shape=rectangle];
      edge [arrowhead=crow];
      subgraph cluster_qalog {
          label = "Component QA Log";
          QALogEvent;
      }
      subgraph cluster_inventory {
          label = "Component Inventory";
          Component;
      }
      subgraph cluster_ats {
          label = "Aircraft Type Specification";
	  SystemType;
	  ComponentType;
	  ComponentTypeAppropriateness;
	  QARule;
      }
      SystemType -> SystemType;
      SystemType -> QARule;
      ComponentType -> ComponentTypeAppropriateness;
      SystemType -> ComponentTypeAppropriateness;

      ComponentType -> Component;

      Component -> QALogEvent;
      QARule -> QALogEvent;
   }


Aircraft Configuration Data
---------------------------

This describes a fleet of aircraft. Instances of Aircraft Type Specifications.

An aircraft has a unique identity, but it is an assembly of components that can be swapped out.

.. graphviz::

   digraph d {
      node [shape=rectangle];
      edge [arrowhead=crow];
      subgraph cluster_config {
          label="Aircraft Configuration Data";
          Aircraft -> AircraftVersion;
	  AircraftVersion -> ComponentRole -> ConfigurationItem;
      }
      subgraph cluster_inventory {
          label = "Component Inventory";
          Component;
      }
      Component -> ConfigurationItem;
      subgraph cluster_ats {
          label = "Aircraft Type Specification";
	  SystemType;
      }
      SystemType -> Aircraft;
      SystemType -> AircraftVersion;
      SystemType -> ComponentRole;

   }


Aircraft
^^^^^^^^

A unique identifier. Registration number if you will. Note that it's bound to a SystemType - this must be an abstract type (system with no parents), because an aircraft can not change type!


AircraftVersion
^^^^^^^^^^^^^^^

Instance bound to a first generation SystemType. Note that an aircraft can be upgraded (and downgraded) to different versions of it's type.


ComponentRole
^^^^^^^^^^^^^

Logical entities for a particular version of an aircraft, that corespond to the components (leaves) in the aircraft type specification tree. If the aircraft type specifies a subsystem with a camera component, this specific aircraft's camera is defined as a coresponding ComponentRole.


ConfigurationItem
^^^^^^^^^^^^^^^^^

This represents that a specific component (e.g. camera) is employed in the ComponentRole.

When components are swapped out in an aircraft, this is represented as changes to ConfigurationItems. ConfigurationItems have timestamps ("from" and "to") and there are rules preventing contemporanious assignments of different Components to the same ConfigurationRole (and, the same component to multiple ConfigurationRoles). You can only be in one place at a time.


Old Stuff
---------

Rude notes from an earlier analysis session...


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


Safety Team
-----------

UAS Operation, the group with the SMS:
 * HIA >-- Team
 * Vehicle >-- Team
 * TeamRole: Safety Officer, Chief Pilot, etc.
 * Team --< TeamInvolvement >-- TeamRole
 * TeamInvolvement --< TeamInvolved >-- Person

Note on Teams:
 * system may be configured as multi-tenanted solution (software as a service, multiple teams)
 * system may be configured for a single team, "self-hosted" configuration
 

Confidentiality
---------------

Private: only visible to the Team's Chief Pilot and Safety Officer(s). Note local laws may require the Chief Pilot to report all data on certain accidents to authorities.

Public: may be published, at Chief Pilot or any Safety Officer's discression.

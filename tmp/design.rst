Design
======

Two distinct roles are defined; UAS/RPAS operators and safety teams. While the same
person may be involved in both activities, the system is structured in a way that
keeps the roles/activities at arms length.

The goal of operators is to operate safely. The goal of safety teams is to continuously improve the safety of operations. This includes promoting safety culture with the operators.

.. graphviz::

   digraph d {
      promote [label="promote\nsafety\nculture" shape=ellipse];
      opcom [label="UAS/RPAS\noperator" shape=house];
      operate [label="operate\nUAS/RPAS\nsafely"];
      opcom -> operate;
      hub [label="safety\nteam" shape=house];
      ci [label="continuously\nimprove\nsafety" shape=ellipse];
      hub -> ci;
      ci -> promote;
      opcom -> promote;
   }


In adition to distinctly separating these roles, the design intent of the system is
to support distrubuted safety colaboration. This means multiple safety teams and
multiple operators, who free to be as independant or colaborative as they wish.

 * They may run their own instances of the system, or co-tenant shared IT infrastructure.
 * Operators control what data they share (if any) with the wider community, and what they share with their safety team(s).
 * Safety teams can limit their view to the operators they service, or combine it with public data from the entire operator community.

There is an absolute minimum of "centralised adminisration", it's limited to a simple
interface where operators can register/publish the fact they exist and have chosen to make some data available.

Operator teams and the safety teams are loosely coupled. Each operator can share their data with multiple safety teams (or none). Each safety team can audit, analyse and monitor multiple operators, or they can limit themselves to analysing the public information from the wider comunity.

The next diagram is horendous, and could be replaced with an much simpler infographic at some stage.

.. graphviz::

   digraph d {
      subgraph cluster_opcom {
         label = "operations (private)"
         sms [label="management\ndatabase" shape=component];
	 sms_admin_ui [label="admin\nUI"];
	 sms_ui [label="web/tablet UI"];
	 sms_api [label="API"];
	 sms_rdf [label="linked-data\ninterface"];
	 
	 sms_admin_ui -> sms;
	 sms_ui -> sms;
	 sms_api -> sms;
	 sms_rdf -> sms;
	 integrate [label="SMS-integrated\ntools"];
	 integrate -> sms_api;

      }
      subgraph cluster_public {
         label = "open source (public)";
         enhance [label="enhance\nsoftware" shape=ellipse];
         src [label="UAS Fun Police\nsource code" shape=component];
	 pr [label="public\nregister" shape=component];
	 pri [label="optional\npublication\ninterface"];
	 pri -> pr -> src;
      }
      subgraph cluster_st {
         label = "governance (private)";
         aa [label="audit, analyse\nand monitor\noperations"];	 
         ag [label="data\naggregator" shape=component];
         gov [label="safety\ngovernance\ntools" shape=component];
      }
      ag -> pri -> sms_rdf;
      promote [label="promote\nsafety\nculture" shape=ellipse];
      opcom [label="operator\ncommunity" shape=house];
      operate [label="operate\nUAS/RPAS\nsafely"];
      operate -> integrate;
      operate -> sms_ui;
      operate -> sms_admin_ui;
      hub [label="safety\nteam" shape=house];
      ci [label="continuously\nimprove\nsafety" shape=ellipse];
      opcom -> promote;
      opcom -> operate;
      hub -> ci -> aa -> gov -> ag -> sms_rdf;
      ci -> promote;
      ci -> enhance -> src;
      sms -> src;
      gov -> src;
   }


The horrendogram shows:
 * Operators use a management database, which has multiple interfaces.
 * Safety teams use safety governance tools
 * both these tools are free software, part of the UAS Fun Police suite

It also shows that continuously improving safety breaks down into three kinds of activity:
 * enhancing the UAS Fun Police software
 * promoting safety culture
 * audit, analyse and monitor operations

Jargon alert: Those three things are the "use-case packages" that contain safety team's functional requirements.

The horrendogram also shows Operating a UAS/RPAS safely includes using a number of interfaces. Obviously there's more to it than that, but we will leave those details for later. What we can see here is that there are multiple interfaces:
 * admin UI: this is used for administration purposes. Someone is in full control of the UAS Fun Police instance that the operator uses. If they are self-hosting their own IT the administrator will be part of their team. If they are a tennant in shared infrastructure, the administrator may be servicing multiple operators.
 * web/tablet UI: this is the main user-interface that operators will see.
 * API: this is a machine-friendly equivalent to the web/tablet UI. It can be used by SMS-integrated tools.

SMS-integrated tools reffers to the possability to avoid manual work (avoid using the web/tablet UI) by getting your computers to talk to each other. For example, there is no need to register flights manually if your ground control station does that for you.

The last part of the horrendogram shows the linked data infrastructure that the safety governance tools depend on. I'll describe that later. 

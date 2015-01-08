Design
======

Two distinct roles are defined; UAS/RPAS operators and safety teams. While the same
person may be involved in both activities, the system is structured in a way that
keeps the roles/activities at arms length.

The goal of operators is to operate safely. The goal of safety teams is to continuously improve the safety of operations. This includes promoting safety culture with the operators.

.. graphviz::

   digraph d {
      label="figure 1; loose coupling of operations from safety management services";
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
multiple operators, who are free to be as independant or colaborative as they wish.

 * They may run their own instances of the system, or co-tenant shared IT infrastructure.
 * Operators control what data they share (if any) with the wider community, and what they share with their safety team(s).
 * Safety teams can limit their view to the operators they service, or combine it with public data from the entire operator community.

This introduces a third (loose coupled) domain, colaboration management. Again, this can be done privately or publically. Public colaboration management means that the information-sharing network between operators and safety teams is transparent. Private colaboration management means that information-sharing network is hidden (except to the participants). Both are expected to be usefull under different situations. The following diagram illustrates the public case.

.. graphviz::

   digraph d {
      label="figure 2; public colaboration management";
      subgraph cluster_pub {
         label="public domain";
         promote [label="promote\nsafety\nculture" shape=ellipse];
         colab [label="maintain\ncolaboration"];
	 orch [label="orchestration\ntools" shape=component];
	 colab -> orch;
	 promote -> orch;
      }
      subgraph cluster_op {
         label = "operator domain";
         opcom [label="UAS/RPAS\noperator" shape=house];
         operate [label="operate\nUAS/RPAS\nsafely"];
	 omd [label="operations\nmanagement\ndatabase" shape=component];
	 operate -> omd;
      }
      subgraph cluster_st {
         label = "safety team domain";
         hub [label="safety\nteam" shape=house];
         ci [label="continuously\nimprove\nsafety" shape=ellipse];
	 stt [label="governance\ntools" shape=component];
	 ci -> stt;
      }

      opcom -> operate;
      hub -> ci;
      ci -> promote;
      opcom -> promote;
      opcom -> colab;
      hub -> colab;
   }

The private colaboration is the same except instead of "public comain" the orchestration tools are private.

This diagram shows the three, loosly coupled components:
 * governance tools
 * orchestration tools
 * operations management database

In the private colaboration case, you would self-host your own orchestration tools and configure your operations management database and governance tools to include the private orchestration integration endpoints.

What it doesn't show is the integration layer between those tools. This is shown later.

The other thing that the above diagram doesn't make clear is just how decentralised and scalable this is. A single public set of orchestration tools could support an arbitrarially large web of colaborating operators and safety teams. Each safety team and operator can link into multiple sets of orchestration tools (public and private). This is not because the world actually needs an enormously rich web of colaborations, it's a natural consequence of the decentralised, linked-up design.

The next diagram ignores the operator domain, and expands on the public domain to include the open source dialog on tools. This is a significant safety strategy; place quality (through peer review and colaboration) above propietary interests.

.. graphviz::

   digraph d {
      subgraph cluster_pub {
         label="public domain";
         promote [label="promote\nsafety\nculture" shape=ellipse];
         colab [label="maintain\ncolaboration"];
         orch [label="orchestration\ntools" shape=component];
         colab -> orch;
         promote -> orch;

         foss [label="UAS Fun Police\nsource code repository" shape=component]
         enhance [label="enhance\nsystems"];
         enhance -> foss;
      }
      subgraph cluster_st {
         label = "safety team domain";
         hub [label="safety\nteam" shape=house];
         ci [label="continuously\nimprove\nsafety" shape=ellipse];
	 stt [label="governance\ntools" shape=component];
	 hub -> ci -> stt;
      }
      ci -> enhance;
      ci -> promote;
   }


The approach to integration is "control inverted". This means the components that have data and know how to use it (applications) provide interfaces, but they are purely servants; they provide services without consuming any, they wait pasively.

.. graphviz::

   digraph d {
      label="integration architecture";
      subgraph cluster_app {
         label="data-source service";
         app [shape=component]
	 ui [label="user\ninterface"];
	 api;
	 rdf [label="read-only\nlinked-data\ninterface"];
	 ui -> api -> app;
	 rdf -> app;
      }
      subgraph cluster_app2 {
         label="data-sink service";
         app2 [shape=component label="app"];
	 ui2 [label="user\ninterface"];
	 api2 [label="api"];
	 rdf2 [label="read-only\nlinked-data\ninterface"];
	 ui2 -> api2 -> app2;
	 rdf2 -> app2;
      }

      subgraph cluster_agent {
         label="integration agent";
         ag [label="data\naggregator" shape=component];
	 sparql [label="federated\ndata"];
	 sparql -> ag;
	 wrkr [label="worker" shape=component];
	 wrkr -> sparql;
      }
      ag -> rdf;
      wrkr -> api2;

      orch [label="orchestration\ntools" shape=component];
      rdf3 [label="read-only\nlinked-data\ninterface"];
      ag -> rdf3 -> orch;
   }

The above diagram shows an integration agent (working on behalf of the data-sink service, that is receiving data through it's API). The integration agent uses it's data aggregator to pulls data from relevant data-source at once, as though they were a single federated source. The data aggregator knows which source-services are relevant becauseit asks the orchestration tool using it's linked-data interface.

Both the governance tools and operations management tools would both have integration agents. Governance tools would use them in the most obvious way, to access information about operations from the various operators they service. Operations management tools would also have an integration agent to access information from safety management service providers, such as updates to rules etc.


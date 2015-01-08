Design
======

.. graphviz::

   digraph d {
      label="distrinuted, colaborative architecture";

      node [shape=ellipse];
      promote [label="promote\nsafety\nculture"];
      enhance [label="continuously\nimprove\nsafety management"];
      use [label="use\nUAS Fun Police\nsoftware"];

      node [shape=rectangle];
      opcom [label="operator\ncommunity"];
      hub [label="safety\nteam"];
      src [label="open\nsource\ncode"];

      promote -> opcom;
      promote -> hub;
      enhance -> src;
      enhance -> hub;
      hub -> opcom;
      hub -> use;
      opcom -> use;
      use -> src;
   }

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

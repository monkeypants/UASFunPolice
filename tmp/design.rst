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
         opcom [label="operator\ncommunity" shape=house];
         sms [label="operational\nmanagement\ndatabase" shape=component];
	 sms_admin_ui [label="admin\nUI"];
	 sms_ui [label="web/tablet UI"];
	 sms_api [label="API"];
	 sms_rdf [label="linked-data\ninterface"];
	 
	 sms_admin_ui -> sms;
	 sms_ui -> sms;
	 sms_api -> sms;
	 sms_rdf -> sms;

	 operate [label="operate\nUAS/RPAS\nsafely"];
	 opcom -> operate;
	 integrate [label="employ\nSMS-integrated\ntools"];
	 operate -> integrate;

	 integrate -> sms_api;
	 operate -> sms_ui;
	 operate -> sms_admin_ui;
    }
      hub [label="safety\nteam" shape=house];
      promote [label="promote\nsafety\nculture" shape=ellipse];
      opcom -> promote;

      ci [label="continuously\nimprove\nsafety" shape=ellipse];      
      aa [label="audit, analyse\nand monitor\noperations"];
      ag [label="data\naggregator" shape=component];

      hub -> ci -> aa -> ag -> sms_rdf;
      ci -> promote;
      enhance [label="enhance\nsoftware" shape=ellipse];
      src [label="UAS Fun Police\nsource code" shape=component];
      ci -> enhance -> src;
      sms -> src;
      gov [label="safety\ngovernance\ntools" shape=component];
      aa -> gov -> src;
   }

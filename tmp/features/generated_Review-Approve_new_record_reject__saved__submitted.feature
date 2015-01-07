Feature: reject with comments the page showing the current record (editable) on the page showing the current record (approvable)


    Scenario: (Manager) Review and reject submission (with comments)
    	Given I am a Manager
	Given I try something naughty
	Then nothing happens
    

    Scenario: (Peer) Review and reject submission (with comments)
    	Given I am a Peer
	Given I try something naughty
	Then nothing happens
    

    Scenario: (Compliance Officer) Review and reject submission (with comments)
    	Given I am a Compliance Officer
	Given I try something naughty
	Then nothing happens
    


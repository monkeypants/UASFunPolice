Feature: accept the page showing the current record (approved, loadable) on the page showing the current record (approvable)


    Scenario: (Manager) Review and accept sumbission (approve loading into CEMS)
    	Given I am a Manager
	Given I try something naughty
	Then nothing happens
    

    Scenario: (Peer) Review and accept sumbission (approve loading into CEMS)
    	Given I am a Peer
	Given I try something naughty
	Then nothing happens
    

    Scenario: (Compliance Officer) Review and accept sumbission (approve loading into CEMS)
    	Given I am a Compliance Officer
	Given I try something naughty
	Then nothing happens
    


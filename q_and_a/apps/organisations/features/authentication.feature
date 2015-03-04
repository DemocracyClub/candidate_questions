Feature: Organisation authentication
  # Scenario: invited to use the site
  #   Given that I have received an invitation to use the site
  #   When I follow the instructions in the invitation
  #   Then I am taken to the Questions List

  Scenario: returning user
    Given that I have identified myself to the site previously by following the instructions I received in an invitation
    When I visit the site subsequently (going directly, without necessarily following those instructions)
    Then I am authenticated and identified automatically
    And I am taken to the Questions List
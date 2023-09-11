# features/simple-addition.feature


  Feature: Simple Addition

    Showcase simple addition for the BDD Book

    Scenario: Addition of single digit numbers
      Given I have '1' and '3'
      When I add them
      Then The result must be '4'

    Scenario: Addition of double digit numbers
      Given I have '70' and '29'
      When I add them
      Then The result must be '99'


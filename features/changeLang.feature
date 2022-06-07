Feature: Verify change language function
  Scenario: Change language to ENG then RUS then to AZE
    Given Launch browser
    When Open URL
    When Click button to change page language to ENG
    Then Page language changed to ENG
    When Click button to change page language to RUS
    Then Page language changed to RUS
    When Click button to change page language to AZE
    Then Page language changed to AZE





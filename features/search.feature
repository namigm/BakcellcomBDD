Feature: Search functionality



  Background:
    Given Launch the browser
    When Open the bakcell.com
    When Click the search button



  Scenario: Check the search functionality
    When Input the "Tarif"
    Then Check the search result



  Scenario Outline: Check the search functionality
    When Input the "<value>"
    Then Check the search result


    Examples:
    | value |
    | pwsvb|
    | ptsaa |


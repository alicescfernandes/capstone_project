Feature: Data Visualization Platform
  As a group user
  I want to visualize and analyze data from XLSX files
  So that I can better understand and filter the data

  Background:
    Given I am logged in as a group user
    And I have access to the platform

  Scenario: Creating a new quarter
    Given I am on the Settings page
    When I click on "Create New Quarter"
    And I select "Quarter 2" from the dropdown
    And I click "Save"
    Then I should see "Quarter 2" listed in my quarters
    And I should be able to upload files to "Quarter 2"

  Scenario: Uploading an XLSX file
    Given I am on the Settings page
    And I have selected "Quarter 2"
    When I click "Upload File"
    And I select the file "CustomerNeeds-Q2.xlsx"
    And I click "Upload"
    Then I should see "CustomerNeeds-Q2.xlsx" listed in my files
    And the file should be associated with "Quarter 2"

  Scenario: Deleting an XLSX file
    Given I am on the Settings page
    And I have the file "CustomerNeeds-Q2.xlsx" uploaded
    When I click the delete button next to "CustomerNeeds-Q2.xlsx"
    And I confirm the deletion
    Then I should not see "CustomerNeeds-Q2.xlsx" in my files anymore

  Scenario: Viewing data visualization
    Given I am on the Homepage
    And I have uploaded "CustomerNeeds-Q2.xlsx"
    When the page loads
    Then I should see the data visualization charts
    And the charts should display data from "CustomerNeeds-Q2.xlsx"

  Scenario: Applying advanced filters to charts
    Given I am on the Homepage
    And I have uploaded "CustomerNeeds-Q2.xlsx"
    When I select specific filter criteria
    And I click "Apply Filters"
    Then the charts should update to show only the filtered data

  Scenario: Changing account password
    Given I am on the Settings page
    When I click "Change Password"
    And I enter my current password
    And I enter a new password
    And I confirm the new password
    And I click "Save"
    Then I should see a success message
    And I should be able to log in with the new password

  Scenario: Recovering forgotten password
    Given I am on the Login page
    When I click "Forgot Password"
    And I enter my registered email
    And I click "Send Recovery Link"
    Then I should receive a password recovery email
    And I should be able to reset my password using the link 
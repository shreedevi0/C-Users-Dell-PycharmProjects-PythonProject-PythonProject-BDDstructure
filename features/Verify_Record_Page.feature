Feature: Record page Verification

    Background: Reusable code
      Given Launch the Browser
      When Open the Website
      And Login with valid username "Admin" and Password "admin123"

    Scenario:Verification of Record Page
      Given Navigate to Time
      When User click on Attendance and select the My Records
      Then Record page should display


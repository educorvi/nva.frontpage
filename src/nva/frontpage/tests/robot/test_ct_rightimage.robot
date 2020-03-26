# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s nva.frontpage -t test_rightimage.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src nva.frontpage.testing.NVA_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/nva/frontpage/tests/robot/test_rightimage.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a rightimage
  Given a logged-in site administrator
    and an add rightimage form
   When I type 'My rightimage' into the title field
    and I submit the form
   Then a rightimage with the title 'My rightimage' has been created

Scenario: As a site administrator I can view a rightimage
  Given a logged-in site administrator
    and a rightimage 'My rightimage'
   When I go to the rightimage view
   Then I can see the rightimage title 'My rightimage'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add rightimage form
  Go To  ${PLONE_URL}/++add++rightimage

a rightimage 'My rightimage'
  Create content  type=rightimage  id=my-rightimage  title=My rightimage

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the rightimage view
  Go To  ${PLONE_URL}/my-rightimage
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a rightimage with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the rightimage title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

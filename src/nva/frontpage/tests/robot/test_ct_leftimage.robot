# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s nva.frontpage -t test_leftimage.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src nva.frontpage.testing.NVA_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/nva/frontpage/tests/robot/test_leftimage.robot
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

Scenario: As a site administrator I can add a Leftimage
  Given a logged-in site administrator
    and an add Landingpage form
   When I type 'My Leftimage' into the title field
    and I submit the form
   Then a Leftimage with the title 'My Leftimage' has been created

Scenario: As a site administrator I can view a Leftimage
  Given a logged-in site administrator
    and a Leftimage 'My Leftimage'
   When I go to the Leftimage view
   Then I can see the Leftimage title 'My Leftimage'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Landingpage form
  Go To  ${PLONE_URL}/++add++Landingpage

a Leftimage 'My Leftimage'
  Create content  type=Landingpage  id=my-leftimage  title=My Leftimage

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Leftimage view
  Go To  ${PLONE_URL}/my-leftimage
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Leftimage with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Leftimage title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

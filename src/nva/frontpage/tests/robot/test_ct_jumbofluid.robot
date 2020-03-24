# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s nva.frontpage -t test_jumbofluid.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src nva.frontpage.testing.NVA_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/nva/frontpage/tests/robot/test_jumbofluid.robot
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

Scenario: As a site administrator I can add a Jumbofluid
  Given a logged-in site administrator
    and an add Jumbofluid form
   When I type 'My Jumbofluid' into the title field
    and I submit the form
   Then a Jumbofluid with the title 'My Jumbofluid' has been created

Scenario: As a site administrator I can view a Jumbofluid
  Given a logged-in site administrator
    and a Jumbofluid 'My Jumbofluid'
   When I go to the Jumbofluid view
   Then I can see the Jumbofluid title 'My Jumbofluid'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Jumbofluid form
  Go To  ${PLONE_URL}/++add++Jumbofluid

a Jumbofluid 'My Jumbofluid'
  Create content  type=Jumbofluid  id=my-jumbofluid  title=My Jumbofluid

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Jumbofluid view
  Go To  ${PLONE_URL}/my-jumbofluid
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Jumbofluid with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Jumbofluid title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

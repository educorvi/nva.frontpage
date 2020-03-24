# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s nva.frontpage -t test_textbox.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src nva.frontpage.testing.NVA_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/nva/frontpage/tests/robot/test_textbox.robot
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

Scenario: As a site administrator I can add a textbox
  Given a logged-in site administrator
    and an add textbox form
   When I type 'My textbox' into the title field
    and I submit the form
   Then a textbox with the title 'My textbox' has been created

Scenario: As a site administrator I can view a textbox
  Given a logged-in site administrator
    and a textbox 'My textbox'
   When I go to the textbox view
   Then I can see the textbox title 'My textbox'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add textbox form
  Go To  ${PLONE_URL}/++add++textbox

a textbox 'My textbox'
  Create content  type=textbox  id=my-textbox  title=My textbox

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the textbox view
  Go To  ${PLONE_URL}/my-textbox
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a textbox with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the textbox title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

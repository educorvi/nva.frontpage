# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s nva.frontpage -t test_jumbotron.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src nva.frontpage.testing.NVA_FRONTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/nva/frontpage/tests/robot/test_jumbotron.robot
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

Scenario: As a site administrator I can add a jumbotron
  Given a logged-in site administrator
    and an add jumbotron form
   When I type 'My jumbotron' into the title field
    and I submit the form
   Then a jumbotron with the title 'My jumbotron' has been created

Scenario: As a site administrator I can view a jumbotron
  Given a logged-in site administrator
    and a jumbotron 'My jumbotron'
   When I go to the jumbotron view
   Then I can see the jumbotron title 'My jumbotron'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add jumbotron form
  Go To  ${PLONE_URL}/++add++jumbotron

a jumbotron 'My jumbotron'
  Create content  type=jumbotron  id=my-jumbotron  title=My jumbotron

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the jumbotron view
  Go To  ${PLONE_URL}/my-jumbotron
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a jumbotron with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the jumbotron title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

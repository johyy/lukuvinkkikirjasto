
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kurpitsa
    Set Password  salasana1234
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kurpitsa
    Set Password  salasana12345
    Submit Credentials
    Login Should Fail With Message  Käyttäjänimi tai salasana virheellinen

Login With Nonexistent Username
    Set Username  ${EMPTY}
    Set Password  salasana1234
    Submit Credentials
    Login Should Fail With Message  Käyttäjänimi tai salasana virheellinen

*** Keywords ***
Login Should Succeed
    Home Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Kirjaudu sisään

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Login Page
    Create User  kurpitsa  salasana1234
    Go To Login Page
    Login Page Should Be Open

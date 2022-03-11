*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Login

*** Test Cases ***
Add like
    Home Page Should Be Open
    Page Should Contain  ♥ 0
    Page Should Contain Button  Tykkään!
    Page Should Not Contain Button  Enpäs tykkääkään.
    Click Button  Tykkään!
    Page Should Not Contain  Tykkään!
    Page Should Contain Button  Enpäs tykkääkään.
    Page Should Contain  ♥ 1

Remove like
    Home Page Should Be Open
    Page Should Contain  ♥ 1
    Page Should Contain Button  Enpäs tykkääkään.
    Page Should Not Contain Button  Tykkään!
    Click Button  Enpäs tykkääkään.
    Page Should Contain Button  Tykkään!
    Page Should Not Contain Button  Enpäs tykkääkään.
    Page Should Contain  ♥ 0

*** Keywords ***
Create User And Login
    Create User  jee  sanasala1234
	Go To Login Page
    Set Username  jee
    Set Password  sanasala1234
    Submit Credentials
	
Submit Credentials
    Click Button  Kirjaudu sisään

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
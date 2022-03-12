*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Databases

*** Test Cases ***
Add like
    Create User and Login
    Add Recommendation
    Page Should Contain  ♥ 0
    Page Should Contain Button  Tykkään!
    Page Should Not Contain Button  Enpäs tykkääkään.
    Click Button  Tykkään!
    Page Should Not Contain  Tykkään!
    Page Should Contain Button  Enpäs tykkääkään.
    Page Should Contain  ♥ 1

Remove like    
    Create User and Login
    Add Recommendation
    Click Button  Tykkään!
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

Add Recommendation
    Go To Add Recommendation Page
    Add Recommendation Page Should Be Open
    Select From List By Label  media  Kirja
    Click Button  Valitse
    Set Title  Great Book
    Set Link  https://www.a.fi/
    Click Button  Lisää
    Home Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Link
    [Arguments]  ${url}
    Input Text  url  ${url}
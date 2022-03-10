*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Login

*** Test Cases ***
Remove recommendation
	Add Recommendation
    Go To Own Page
    Own Page Should Be Open
    Page Should Contain  Teos
    Click Button  Poista
    Home Page Should Be Open
	Go To Own Page
    Page Should Not Contain  Teos
	


*** Keywords ***
Create User And Login
    Create User  testi2  sanasala1234
	Go To Login Page
    Set Username  testi2
    Set Password  sanasala1234
    Submit Credentials
	
Add Recommendation
	Go To Add Recommendation Page
    Add Recommendation Page Should Be Open
    Select From List By Label  media  Kirja
    Click Button  Valitse
    Set Title  Teos
    Set Link  https://www.a.fi/
    Send Recommendation

Submit Credentials
    Click Button  Kirjaudu sisään

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Send Recommendation
    Click Button  Lisää

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Link
    [Arguments]  ${url}
    Input Text  url  ${url}
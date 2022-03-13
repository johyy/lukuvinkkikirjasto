*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Login

*** Test Cases ***

Index listing default
    Create Index Recommendations
    Table Row should contain  index_table  1  Third
    Table Row should contain  index_table  2  First
    Table Row should contain  index_table  3  Second

Index listing least likes
    Create Index Recommendations
    Select Radio Button  sort_option  2
    Table Row should contain  index_table  1  Second
    Table Row should contain  index_table  2  Third
    Table Row should contain  index_table  3  First

Index listing newest
    Create Index Recommendations
    Select Radio Button  sort_option  3
    Table Row should contain  index_table  1  Third
    Table Row should contain  index_table  2  Second
    Table Row should contain  index_table  3  First

Index listing oldest
    Create Index Recommendations
    Select Radio Button  sort_option  4
    Table Row should contain  index_table  1  First
    Table Row should contain  index_table  2  Second
    Table Row should contain  index_table  3  Third

*** Keywords ***

Create Index Recommendations
    Add Recommendation  First  http://www.First.com
    Page Should Contain  First
    Click Button  Tykkään!
    Sleep  2s
    Add Recommendation  Second  http://www.Second.com
    Page Should Contain  Second
    Sleep  2s
    Add Recommendation  Third  http://www.Third.com
    Page Should Contain  Third
    Click Button  Tykkään!

Create User And Login
    Reset Databases
    Create User  testi2  sanasala1234
	Go To Login Page
    Set Username  testi2
    Set Password  sanasala1234
    Submit Credentials
	
Add Recommendation
    [Arguments]  ${title}  ${url}
	Go To Add Recommendation Page
    Add Recommendation Page Should Be Open
    Select From List By Label  media  Blogi
    Click Button  Valitse
    Input Text  title  ${title}
    Input Text  url  ${url}
    Send Recommendation
    Go To Starting Page
    Home Page Should Be Open

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
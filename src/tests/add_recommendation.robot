
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Databases And Create User

*** Test Cases ***
Access to Add Recommendation Page Denied Without Login
    Go To Add Recommendation Page
    Add Recommendation Page Should Be Open
    Accessing Should Fail With Message  Ei oikeutta sivulle!

Add Recommendation With Valid Title And Link
    Go To Login Page
    Set Username  kurppa
    Set Password  sanasala1234
    Submit Credentials
    Go To Add Recommendation Page
    Add Recommendation Page Should Be Open
    Select From List By Label  media  Kirja
    Click Button  Valitse
    Set Title  Great Book
    Set Link  https://www.a.fi/
    Add Recommendation
    Adding Should Succeed With Message  Vinkki lisätty kirjastoon!

Add Recommendation With Nonexistent Title
    Go To Login Page
    Set Username  kurppa
    Set Password  sanasala1234
    Submit Credentials
    Go To Add Recommendation Page
    Add Recommendation Page Should Be Open
    Select From List By Label  media  Kirja
    Click Button  Valitse
    Set Title  ${EMPTY}
    Set Link  https://www.a.fi/
    Add Recommendation
    Adding Should Fail With Message  Täytä kaikki tiedot

Add Recommendation With Nonexistent Link
    Go To Login Page
    Set Username  kurppa
    Set Password  sanasala1234
    Submit Credentials
    Go To Add Recommendation Page
    Add Recommendation Page Should Be Open
    Select From List By Label  media  Kirja
    Click Button  Valitse
    Set Title  Another Great Book
    Set Link  ${EMPTY}
    Add Recommendation
    Adding Should Fail With Message  Täytä kaikki tiedot

Add Recommendation With Already Existing Title
    Go To Login Page
    Set Username  kurppa
    Set Password  sanasala1234
    Submit Credentials
    Go To Add Recommendation Page
    Add Recommendation Page Should Be Open
    Select From List By Label  media  Kirja
    Click Button  Valitse
    Set Title  Awesome Book
    Set Link  https://www.a.fi/
    Add Recommendation
    Adding Should Succeed With Message  Vinkki lisätty kirjastoon!
    Go To Add Recommendation Page
    Select From List By Label  media  Kirja
    Click Button  Valitse
    Set Title  Awesome Book
    Set Link  https://www.a.fi/
    Add Recommendation
    Adding Should Fail With Message  Awesome Book löytyy jo kirjastosta

*** Keywords ***
Adding Should Succeed
    Add Recommendation Page Should Be Open

Adding Should Fail With Message
    [Arguments]  ${message}
    Add Recommendation Page Should Be Open
    Page Should Contain  ${message}

Adding Should Succeed With Message
    [Arguments]  ${message}
    Home Page Should Be Open
    Page Should Contain  ${message}

Accessing Should Fail With Message
    [Arguments]  ${message}
    Add Recommendation Page Should Be Open
    Page Should Contain  ${message}

Add Recommendation
    Click Button  Lisää

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Link
    [Arguments]  ${url}
    Input Text  url  ${url}

Submit Credentials
    Click Button  Kirjaudu sisään

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Reset Databases And Create User
    Reset Databases
    Create User  kurppa  sanasala1234
    
    
    

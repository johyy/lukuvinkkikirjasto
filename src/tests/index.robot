*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Home Page Should Be Open

*** Test Cases ***
Click Login Link
    Click Link  Kirjaudu sisään
    Login Page Should Be Open

Click Register Link
    Click Link  Luo uusi tunnus
    Register Page Should Be Open



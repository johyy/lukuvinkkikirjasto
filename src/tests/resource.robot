
*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}/
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${ADD URL}  http://${SERVER}/add_recommendation


*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Home

Register Page Should Be Open
    Title Should Be  Register

Login Page Should Be Open
    Title Should Be  Login

Add Recommendation Page Should Be Open
    Title Should Be  Add_recommendation

Go To Login Page
    Go To  ${LOGIN URL}

Go To Starting Page
    Go To  ${HOME URL}

Go to Registering Page
    Go To  ${REGISTER URL}

Go To Add Recommendation Page
    Go To  ${ADD URL}



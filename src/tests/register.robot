*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

***Test Cases ***
Register With Valid Username And Password
    Set Username  maissi
    Set Password  salasana1234
    Set Password Confirmation  salasana1234
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  salasana1234
    Set Password Confirmation  salasana1234
    Submit Register Credentials
    Register Should Fail With Message  Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki.

Register With Valid Username And Too Short Password
    Set Username  kurpitsa
    Set Password  sala
    Set Password Confirmation  sala
    Submit Register Credentials
    Register Should Fail With Message  Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki.

Register With Valid Username And Password With No Number
    Set Username  kurpitsa
    Set Password  salasana
    Set Password Confirmation  salasana
    Submit Register Credentials
    Register Should Fail With Message  Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki.

Register With Nonmatching Password And Password Confirmation
    Set Username  kurpitsa
    Set Password  salasana1234
    Set Password Confirmation  salasana12345
    Submit Register Credentials
    Register Should Fail With Message  Salasanat eivät täsmää

Login After Failed Registration
    Set Username  kurpitsa
    Set Password  salasana1234
    Set Password Confirmation  salasana12345
    Submit Register Credentials   
    Go To Login Page
    Login Page Should Be Open
    Set Username  kurpitsa
    Set Password  salasana1239
    Submit Login Credentials
    Login Should Fail With Message  Käyttäjänimi tai salasana virheellinen

*** Keywords ***
Go To Register Page
    Go To Registering Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_again  ${password_confirmation}

Submit Register Credentials
    Click Button  Luo uusi tunnus

Submit Login Credentials
    Click Button  Kirjaudu sisään

Register Should Succeed
    Home Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Home Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

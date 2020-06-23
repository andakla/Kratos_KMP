*** Settings ***
Library    ../py_sources/api_business/NetworkSettingsAPI.py    
Library    ../py_sources/api_business/LoginAPI.py    
Library    RequestsLibrary    
Resource    ../ResourceFiles/BussinessKeywords/init.robot

Suite Setup    initialize

*** Variables ***
${DataTest}    Data/test/ListNetworkSetting.json
*** Test Cases ***   
Test case 1 View all the Network Configuration
    
    log to console   ${username}
    ${token}    login    ${username}    ${password}
     
    ${resp}    Get List Network Configuration    ${token} 
    
    Log To Console  logrepo${resp}       
    
    Status Should Be    200    ${resp}   
    
    Verify Response By Json    ${resp}    ${DataTest}
    

Test case 2 Update 1st Network Configuration -hostname
    log to console   ${username}
    ${token}    login    ${username}    ${password}
    
    ${resp}    Update Network Configuration Hostname    0    MN300-125-78    ${token}
    Log To Console  logrepo${resp}       
    
    Status Should Be    200    ${resp}    

    ${respUpdate}    Get Network configuration     0    ${token} 
    
    Status Should Be    200    ${respUpdate}    
    
    Verify Response By Json    ${respUpdate}    ${DataTest}
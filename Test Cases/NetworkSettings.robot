*** Settings ***
Library    ../py_sources/api_business/NetworkSettingsAPI.py    
Library    ../py_sources/api_business/LoginAPI.py    
Library    RequestsLibrary    
Resource    ../ResourceFiles/BussinessKeywords/init.robot


Suite Teardown    Run Keyword    Update Network Configuration Hostname    0    MN300-125-77

*** Variables ***
${DataTest}    Data/test/ListNetworkSetting.json
*** Test Cases ***   
Test case 1 View all the Network Configuration
    
    ${username}  set variable  ${credential}[user]
    ${password}  set variable  ${credential}[pass]
    log to console   ${username}
    ${token}    login    ${username}    ${password}        
    ${resp}    Get List Network configuration    ${token} 
    Log To Console  logrepo${resp}       
    
    Status Should Be    200    ${resp}   
    
    Verify Response By Json    ${DataTest}
    

# Test case 2 Update 1st Network Configuration -hostname

    # ${resp}    Update Network Configuration Hostname    0    MN300-125-78
    # Log To Console  logrepo${resp}       
    
    # Status Should Be    200    ${resp}    
    
    # Sleep    5s    

    # ${respUpdate}    Get Network configuration     0 
    
    # Status Should Be    200    ${respUpdate}    
    
    # Verify Network Configuration Information    /Configuration/NetworkSettings/0    MN300-125-78
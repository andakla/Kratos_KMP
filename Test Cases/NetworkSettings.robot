*** Settings ***
Library    ../py_sources/api_business/NetworkSettingsAPI.py    
Library    ../py_sources/api_business/LoginAPI.py    
Library    RequestsLibrary    
Library    JsonValidator    
Resource    ../ResourceFiles/BussinessKeywords/init.robot

Suite Setup    initialize

*** Variables ***
${DataTest}    Data/test/ListNetworkSetting.json

*** Test Cases ***   
Test case 1 View all the Network Configuration
    [Documentation]    PreReq: RestServer configured properly
    ...    Run the Login scripts to get a Token and save it
    ...    step1: Send a GET request to view Network Configuration
    ...    step 2: Check the Response
    ...    step 3: Parse the reponse Body and check for the values
    ...    Expected:Response code should be 200 Ok and the Response Body will have Network configuration entities
 
    ${token}    login    ${username}    ${password}
     
    ${resp}    Get List Network Configuration    ${token} 
        
    Status Should Be    200    ${resp}   
    
    Verify Response By Json    ${resp}    ${DataTest}

Test case 2 Update 1st Network Configuration -hostname
    [Documentation]    PreReq: RestServer configured properly
    ...    Run the Login scripts to get a Token and save it
    ...    Step1: Send a PUT request to view Network Configuration
    ...    Step 2: Check the Response
    ...    Expected: Response code should be 200 Ok and the Response Body will have Network configuration entities 
    
    ${token}    login    ${username}    ${password}
    
    ${resp}    Update Network Configuration Hostname    0    MN300-125-78    ${token}      
    
    Status Should Be    200    ${resp}    

    ${respUpdate}    Get Network configuration     0    ${token} 
    
    Status Should Be    200    ${respUpdate}    
    
    ${content}    To Json    ${respUpdate.content}
    
    Element Should Exist    ${content}    .hostName:contains("MN300-125-78")
    [Teardown]    Update Network Configuration Hostname    0    MN300-125-77    ${token}
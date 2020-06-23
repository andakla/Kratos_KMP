*** Settings ***
Library    ../py_sources/api_business/NetworkSettingsAPI.py
Library    ../py_sources/api_business/LoginAPI.py
Library    RequestsLibrary    

*** Variables ***
${CONFIGFILE}    data/ServerAPI.json

*** Test Cases ***   
Test case 1
    
   Compare Json    ${CONFIGFILE}
   Compare Json Node        "uri": "/server/server/0"
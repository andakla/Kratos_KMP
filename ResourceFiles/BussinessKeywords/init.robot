

*** Settings ***
Library  BuiltIn
Library  JSONLibrary
Library  RequestsLibrary


*** Keywords ***
initialize
    set global variable  ${BaseURL}  https://10.244.125.77
    set global variable  ${username}    admin
    set global variable  ${password}   Krt123Krt123@#
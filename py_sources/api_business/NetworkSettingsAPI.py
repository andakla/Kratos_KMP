'''
Created on Jun 22, 2020

@author: nhat.phan
'''
import json
from core.api import http
from core.helpers import logger
from utilities import constants
from utilities.api_object_helper import get_endpoint_api, \
    load_data_for_apis


class NetworkSettingsAPI():
    
    def __init__(self):
        self.client= http.target(constants.HOST)
        self._basePath = get_endpoint_api(self)
        self._network_object = load_data_for_apis(self)
        self._response=""
         
    def get_list_network_configuration(self):
        self._response = self.client.get(self._basePath, headers=self._make_header())
        logger.info("respond json: " + json.dumps(self._response.json()))
        return self._response    
     
    
    def verify_response_by_json(self, expected):
        if self._response:
            json_network = self._response.json()
            
                
    def update_network_configuration_hostname(self,number, hostname):
        req_data = { "hostName": hostname}
        req_data = json.dumps(req_data)
        
        headers = self._make_header({'Content-Type': 'application/json' })
        logger.info("Request data: " + req_data)
        self._response = self.client.put(self._basePath +"/"+ number, headers=headers, data=req_data)
        logger.info("respond json updated: " + json.dumps(self._response.json()))
        return self._response
    
    def get_network_configuration(self,id):
        self._response = self.client.get(self._basePath +"/"+ id, headers=self._make_header())
        logger.info("respond json: " + json.dumps(self._response.json()))
        return self._response    
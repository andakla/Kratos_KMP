'''
Created on Jun 22, 2020

@author: nhat.phan
'''
import json

from core.api import http
from core.assertion import Assert
from core.helpers import logger
from utilities import constants
from utilities import utilities
from utilities.api_object_helper import get_endpoint_api, \
    load_data_for_apis

class NetworkSettingsAPI():
    
    def __init__(self):
        self.client= http.target(constants.HOST)
        self._basePath = get_endpoint_api(self)
        self._network_object = load_data_for_apis(self)
        self._response=""
         
    def get_list_network_configuration(self, token):
        self._response = self.client.get(self._basePath, headers= token)
        logger.info("respond json: " + json.dumps(self._response.json()))
        return self._response    
     
    
    def verify_response_by_json(self,src_json, expected_json):
        if self._response:
            b_compare=utilities.compare_json(self, src_json, expected_json)
            Assert.should_be_true(b_compare)
    
    def verify_response_by_node_path(self, expected_json):
        if self._response:
            b_compare=utilities.compare_json(self, self._response.json(), expected_json)
            Assert.should_be_true(b_compare)
     
    def compare_json(self, expected_json):
#         if self._response:
            src={"uri": "/server/server/0",
                 "data":{
                           "ip": "192.168.1.1",
                           "name": "localhost"
                           
                        }
                }
            
            b_compare= utilities.compare_json(self, src, expected_json)
            logger.info("src" +json.dumps(src))
            logger.info("b_compare" +str(b_compare))
            Assert.should_be_true(b_compare)
#     def compare_json_node(self, node):
#             src={"uri": "/server/server/0",
#                  "data":{
#                            "ip": "192.168.1.1",
#                            "name": "localhost"
#                            
#                         }
#                 }
#             
#             b_compare= utilities.compare_json_by_node_path(self, src, node)
#             logger.info("src" +json.dumps(src))
#             logger.info("node" +str(b_compare))
#             Assert.should_be_true(b_compare)                  
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
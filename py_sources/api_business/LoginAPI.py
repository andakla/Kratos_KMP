'''
Created on Jun 17, 2020

@author: nhat.phan
'''

import json

from core.api import http
from core.helpers import logger
from utilities import constants
from utilities.api_object_helper import get_endpoint_api


class LoginAPI():
    
    def __init__(self):
        self.client= http.target(constants.HOST)
        self._basePath = get_endpoint_api(self)

    def login(self,username,password):
        
        userload = 'user=%s&password=%s' % (username, password)
        print(userload)
        res= self.client.post("/rest/Token", data=userload)
        logger.info("api_business.ACCESS_TOKEN: %s", json.dump(res.json()))
        return res.json()
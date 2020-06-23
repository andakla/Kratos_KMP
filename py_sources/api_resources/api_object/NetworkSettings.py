'''
Created on Jun 22, 2020

@author: nhat.phan
'''

class NetworkSettings(object):
    def __init__(self, json):
        self._uri= json['uri']
        self._host_name= json['data']['hostName']
        self._mac_address= json['data']['macAddress']
        self._dns_server_address= json['data']['dnsServerAddress']
        self._ip_address= json['data']['ipAddress']
        self._id= json['data']['id']
        self._interface_name= json['data']['interfaceName']
        self._subnet_mask= json['data']['subnetMask']
        self.defaultGateway= json['data']['defaultGateway']
        self.ntpServerAddress= json['data']['ntpServerAddress']  
    @property
    def uri(self):
        return self._uri
    
    @uri.setter
    def uri(self,m_uri):
        self._uri = m_uri
    
    @property
    def host_name(self):
        return self._host_name
    
    @host_name.setter
    def host_name(self,m_host_name):
        self._uri = m_host_name
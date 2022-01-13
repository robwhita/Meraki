import os
import meraki
from list_orgs_sdk import GetOrgId
from list_networks_SDK import ListNetworks
from list_SSIDs_SDK import Get_SSID_Number

USER = os.environ.get('USERNAME')
token = os.environ.get('PASSWORD')


dashboard = meraki.DashboardAPI(token)


def Enable_SSID(NetID, SSID_Num):
    response = dashboard.wireless.updateNetworkWirelessSsid(NetID , SSID_Num, name='My SSID', enabled=True)
    return response 



if __name__ == '__main__': 
    orgID = GetOrgId()
    NetID = ListNetworks(orgID) 
    SSID_Num = Get_SSID_Number(NetID)
    response = Enable_SSID(NetID, SSID_Num)
    print(response) 



import os
import meraki
from list_orgs_sdk import GetOrgId
from list_networks_SDK import ListNetworks

USER = os.environ.get('USERNAME')
token = os.environ.get('PASSWORD')


dashboard = meraki.DashboardAPI(token)

def Get_SSID_Number(NetID):
    response = dashboard.wireless.getNetworkWirelessSsids(NetID)
    for SSIDs in response: 
        if SSIDs['name'] == 'Unconfigured SSID 2':
            SSID_Num = SSIDs['number']
            return SSID_Num

if __name__ == '__main__': 
    orgID = GetOrgId()
    NetID = ListNetworks(orgID)
    response = Get_SSID_Number(NetID)
    print(response) 
































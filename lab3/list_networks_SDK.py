import os
import meraki
from list_orgs_sdk import GetOrgId
 
USER = os.environ.get('USERNAME')
token = os.environ.get('PASSWORD')

dashboard = meraki.DashboardAPI(token)

def ListNetworks(orgID): 
    response = dashboard.organizations.getOrganizationNetworks(orgID)
    for networks in response:
        if networks['name'] == 'test-network':
            NetID = networks['id']
            return NetID

if __name__ == '__main__': 
    orgID = GetOrgId()
    NetID = ListNetworks(orgID)
    print(NetID) 



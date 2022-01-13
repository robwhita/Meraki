from list_orgs_sdk import GetOrgId
import os
import meraki

USER = os.environ.get('USERNAME')
token = os.environ.get('PASSWORD')


dashboard = meraki.DashboardAPI(token)

def create_network(org_id): 
    response = dashboard.organizations.createOrganizationNetwork(
    org_id, name = "test-network", productTypes=['wireless'])
    return response 

if __name__ == '__main__': 
    orgID = GetOrgId()
    response = create_network(orgID)
    print(response) 

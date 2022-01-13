import os
import meraki

USER = os.environ.get('USERNAME')
token = os.environ.get('PASSWORD')


dashboard = meraki.DashboardAPI(token)


def GetOrgId(): 
    response = dashboard.organizations.getOrganizations()
    for org in response:
        if org['name'] == "DevNet Org":
            org_id = org['id']
            return org_id 

GetOrgId()
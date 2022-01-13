import os
import meraki

USER = os.environ.get('USERNAME')
token = os.environ.get('PASSWORD')

dashboard = meraki.DashboardAPI(token)

name = 'DevNet Org'

response = dashboard.organizations.createOrganization(name)

print(response)



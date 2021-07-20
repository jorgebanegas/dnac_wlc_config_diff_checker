from dnacentersdk import api
import config
import difflib

# Create a DNACenterAPI connection object
dnac = api.DNACenterAPI(username=config.username,
                        password=config.password,
                        base_url=config.base_url,
                        version='2.1.2',
                        verify=False)

# Find all devices that have 'Wireless Controller' in their family
wlcs = dnac.devices.get_device_list(family='Wireless Controller')
for wlc in wlcs['response']:
    print('hostname :',wlc['hostname'], 'device ID :',wlc['id'])
    print('----------------------------------------------------')

golden_wlc_id = input('Enter device ID for the golden wlc : ')
with open("configs/golden_config.txt", "w") as f:
    f.write(dnac.devices.get_device_config_by_id(network_device_id=golden_wlc_id).response)

for wlc in wlcs['response']:
    print('hostname :',wlc['hostname'], 'device ID :',wlc['id'])
    print('----------------------------------------------------')

device_ids = []
res = 1

while(res != '0'):
    res = input('Enter device ID for device you want to compare (0 to stop select) : ')
    if (res == '0'):
        continue
    device_ids.append(res)
    
for device_id in device_ids:
    hostname = dnac.devices.get_device_by_id(id=device_id)['response']['hostname']
    filename = hostname + '.txt'
    with open('configs/'+filename, "w") as f1:
        f1.write(dnac.devices.get_device_config_by_id(network_device_id=device_id).response)

    text1 = open("configs/golden_config.txt").readlines()
    text2 = open('configs/'+filename).readlines()

    with open('diff_check_results/'+filename, "w") as f2:
        for line in difflib.unified_diff(text1, text2):
            f2.write(line + '\n')
from ncclient import manager
import xmltodict
import json
import xml.dom.minidom

m = manager.connect(
    host="ios-xe-mgmt.cisco.com",
    port=10000,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False)

for capability in m.server_capabilities:
    print(capability)

fetched_xml = m.get_config(source='running')
# print(xml.dom.minidom.parseString(str(fetched_xml)).toprettyxml())
fetched_dict = xmltodict.parse(str(fetched_xml))
# print(fetched_dict)
result = json.dumps(fetched_dict, indent=2)
print(result)


m.close_session()

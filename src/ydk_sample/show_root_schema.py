from ydk.path import NetconfSession
from ydk.path import Codec
from ydk.types import EncodingFormat

# Create a NetconfSession instance to connect to the device which supports the YANG 1.1 action-config model
session = NetconfSession(
    address="ios-xe-mgmt.cisco.com",
    port=10000,
    username="developer",
    password="C1sco12345")

# Get the root schema node
root_schema = session.get_root_schema()

print(root_schema.get_path())

# Create and populate the action data
data = root_schema.create_datanode("urn:ietf:params:xml:ns:netconf:base:1.0", "")
# action = action.create_action("action-node")
# action.create_datanode("ip-test", "xyz")
#
# # Invoke the data object containing the action on the session
# data(session)
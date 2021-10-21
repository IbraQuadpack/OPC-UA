  """
    Example : Unknown Server using Subhandler class (Multithreading  mode)
  https://github.com/FreeOpcUa/python-opcua/blob/master/examples/client-example.py
  """
 
  
        # KNOWN SERVER

from opcua import Client
import time

url = "opc.tcp://127.0.0.1:4840"

client = Client(url)

client.connect()
print("Client Connected")

while True:
           Temp = client.get_node("ns=2;i=2")
           Temperature = Temp.get_value()
           print(Temperature)
        
        
        
        #UNKNOWN SERVER
        
        
from opcua import Client
import time

url = "opc.tcp://127.0.0.1:4840"

client = Client(url)


client.connect()
client.load_type_definitions()  # load definition of server specific structures/extension objects
print("Client connected")

# Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
root = client.get_root_node()
print("Root node is: ", root)
objects = client.get_objects_node()
print("Objects node is: ", objects)

# Node objects have methods to read and write node attributes as well as browse or populate address space
print("Children of root are: ", root.get_children())

# get a specific node knowing its node id
#var = client.get_node(ua.NodeId(1002, 2))
#var = client.get_node("ns=3;i=2002")
#var = client.get_node("ns=2;g=1be5ba38-d004-46bd-aa3a-b5b87940c698")
#print(var)
#var.get_data_value() # get value of node as a DataValue object
#var.get_value() # get value of node as a python builtin
#var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
#var.set_value(3.9) # set node value using implicit data type




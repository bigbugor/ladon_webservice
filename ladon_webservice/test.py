__author__ = 'bigbuger'
from suds.client import Client
client = Client('http://localhost:8080/Calculator/soap/description')

# Calculate 34+56
result = client.service.add(34,56)
print result

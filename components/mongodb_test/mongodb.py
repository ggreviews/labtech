#!/usr/bin/env python
import pymongo
import ssl
# https://www.w3schools.com/python/python_mongodb_create_db.asp
# https://www.mongodb.com/download-center/community?jmp=doc

myclient = pymongo.MongoClient(
    "mongodb://localhost:27017/",
#    ssl=True,
#    ssl_cert_reqs=ssl.CERT_REQUIRED,
#    username="<X.509 derived username>",
#    authMechanism="MONGODB-X509",
#    ssl_certfile='/path/to/client.pem',
#    ssl_ca_certs='/path/to/ca.pem'),
)

mydb = myclient["mydatabase"]
print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "local.startup_log" in dblist:
  print("The database exists.")
  
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print(x.inserted_id)

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

#x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids)

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)
print("Update performed\n")


for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

# Exclude address column  
for x in mycol.find({},{ "address": 0 }):
  print(x)  
  

myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x) 
print("\n")  

myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery).limit(1)
for x in mydoc:
  print(x)
print("\n")
  
mydoc = mycol.find().sort("name")
for x in mydoc:
  print(x)
  
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)  
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")
print("\n")

mycol.drop()
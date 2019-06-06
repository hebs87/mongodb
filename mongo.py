# Import pymongo and os
import pymongo
import os

# Set constant for our DB connection stream
MONGODB_URI = os.getenv("MONGO_URI")
# Set constant for DB Cluster name
DBS_NAME = "myTestDB"
# Set constant for DB collection name
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    # try except block - trys the first statement and if it can't do that then it throws an error
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    # Error message if unable to connect
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

# Call function and pass in the connection stream constant - store in variable
conn = mongo_connect(MONGODB_URI)

# Create coll variable, which will store the connection stream, DB and collection names
coll = conn[DBS_NAME][COLLECTION_NAME]

# Create a variable to store the results of a coll.find()
documents = coll.find()

# for loop to iterate through and print each record in the DB
for doc in documents:
    print(doc)
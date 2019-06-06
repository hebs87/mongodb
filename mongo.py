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
    '''
    Function to connect to our connection strem and database
    The try except block runs statments in try if connection is successful,
    or runs statements in except if unsuccessful
    '''
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

'''
TEST CONNECTION
# Create a variable to store the results of a coll.find()
documents = coll.find()

# for loop to iterate through and print each record in the DB
for doc in documents:
    print(doc)
'''

'''
INSERT SINGLE NEW RECORD
# Create new variable with dictionary of key value pairs - fields in quotes and then values
new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'gender': 'm', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}

coll.insert(new_doc)

# Keep the below so we can check that it has worked
# Create a variable to store the results of a coll.find()
documents = coll.find()

# for loop to iterate through and print each record in the DB
for doc in documents:
    print(doc)
'''

'''
INSERT MULTIPLE NEW RECORDS
# Create new variable with array of dictionaries of key value pairs - fields in quotes and then values
new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer',
            'nationality': 'english'},
            {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer',
            'nationality': 'american'}]

coll.insert_many(new_docs)

# Keep the below so we can check that it has worked
# Create a variable to store the results of a coll.find()
documents = coll.find()

# for loop to iterate through and print each record in the DB
for doc in documents:
    print(doc)
'''

'''
FIND SPECIFIC RECORD
# Create a variable to store the results of a coll.find()
documents = coll.find({'first': 'douglas'})

# for loop to iterate through and print each record in the DB
for doc in documents:
    print(doc)
'''

'''
DELETE RECORD
# Create a variable to store the results of a coll.remove()
coll.remove({'first': 'douglas'})

documents = coll.find()

# for loop to iterate through and print each record in the DB
for doc in documents:
    print(doc)
'''

'''
#UPDATE FIRST RECORD THAT IS RETURNED
# Uses the coll.update_one() function, specify the goup to change,
#then set the new value of the field within that group
coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

# Filter the find results to check that our update has worked
documents = coll.find({'nationality': 'american'})

# for loop to iterate through and print each record in the DB
for doc in documents:
    print(doc)
'''

#UPDATE ALL RECORDS THAT ARE RETURNED
# Uses the coll.update_many() function, specify the goup to change,
#then set the new value of the field within that group
coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

# Filter the find results to check that our update has worked
documents = coll.find({'nationality': 'american'})

# for loop to iterate through and print each record in the DB
for doc in documents:
    print(doc)

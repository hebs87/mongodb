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
    1. Function to connect to our connection strem and database
    The try except block runs statments in try if connection is successful,
    or runs statements in except if unsuccessful and prints error message
    '''
    # try except block - trys the first statement and if it can't do that then it throws an error
    try:
        conn = pymongo.MongoClient(url)
        return conn
    # Error message if unable to connect
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    '''
    2. Function to print each option on the page to the end user
    These act as instructions for the end user
    These will include all of the CRUD operations
    '''
    # Blank line to leave some room at the top of the page
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    
    # Input asks user to enter an option (stored in a variable) and returns the input
    option = input("Enter option: ")
    return option

def get_record():
    '''
    9. Helper function to assist us with find, delete and update functions later on
    Code is reusable, so we store it in a separate function so it can be called
    Searches to find, delete and update records are going to be based by name
    '''
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    
    # try except block
    # try contains a variable, which calls the find() method to find records to match input
    # except displays an error if there was an issue accessing the database
    try:
        doc = coll.find({'first': first.lower(), 'last': last.lower()})
    except:
        print("Error accessing database")
    
    # If no documents are returned, an empty variable will be returned
    # If an empty variable is returned (no matches), we will display a message to the user
    if not doc:
        print("")
        print("Error! No results found.")
    
    # Finally, we return the doc variable, which contains the result of the find method
    return doc

def add_record():
    '''
    8. Allow user to add record to the database by completing the necessary fields
    Individual inputs for each field - each in a variable corresponding to the field name
    These inputs will be passed into the dictionary string to pass into the database
    '''
    # Input statements for each field
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")
    
    # Create variable with dictionary to to insert into the database
    # We put the variable name in the values
    # Call the lower method to convert to lowercase
    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob.lower(), 'gender': gender.lower(), 'hair_colour': hair_colour.lower(),
                'occupation': occupation.lower(), 'nationality': nationality.lower(),}
    
    # Create a try expcept block
    # try block inserts the dictionary variable to the database and confirms to user
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")

def main_loop():
    '''
    3. Function to define the main loop, so the options will loop unless the user exits
    '''
    while True:
        # Store the result of the show_menu() function in a variable called option
        option = show_menu()
        if option == "1":
            # print("You have selected option 1") - 7. Have it initially but change once function created
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            # If option 5 is selected, the connection closes and breaks out of the loop
            conn.close()
            break
        else:
            # Message if user enter none of the available options
            print("Invalid option")
        # A blank line to leave a bit of space
        print("")

# 4. Call mongo_connect(url) function and pass in the connection stream constant - store in variable
conn = mongo_connect(MONGODB_URI)
# 5. Create coll variable, which will store the connection stream, DB and collection names
coll = conn[DBS_NAME][COLLECTION_NAME]

# 6. Call our main_loop() function
main_loop()
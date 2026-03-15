import mysql_

# STORE DATA INTO DATABSE 
def store_database(user_choice_table):
    instrument = input("Enter instrument name : ")
    price = int(input("Enter price "))

    query = f"INSERT INTO {user_choice_table} (instrument,price) VALUE (%s, %s)"  # sql query to store value
    values = (instrument,price) # assign two values in a single variable 

    mysql_.mycursor.execute(query,values) # execute sql query
    mysql_.mydb.commit()
    return f"{instrument} details saved successfully"

# ACCESS DATA FROM DATABASE 
def access_data (user_choice_table):
    instrument = input("Enter instrument name : ")
    query = f"SELECT * FROM {user_choice_table} WHERE instrument = %s"
    values = (instrument,)
    mysql_.mycursor.execute(query,values)

    result = mysql_.mycursor.fetchall()
    
    for res in result:
        print(res)
    
    

def func ():
    print("1 for store data in database")
    print("2 for access data into database")
    
    user= int(input("Enter your choice :- "))
    if user == 1:
        user_choice_table = input("which one you want to store\nEnter your choice (gold, wooden, clothes, electronics) - ") 
        print(store_database(user_choice_table))
    elif user == 2:
        user_choice_table = input("which one you want to store\nEnter your choice (gold, wooden, clothes, electronics) - ")
        access_data(user_choice_table)
func()  
 
        

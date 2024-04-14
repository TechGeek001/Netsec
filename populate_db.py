#pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error
import random
import string
import datetime
import hashlib
import sys

# Database connection parameters for initial connection (without specifying the database)
db_config = {
    'user': 'root',
    'password': 'redoubleEFFORT1234',
    'host': '192.168.40.4',
}

# The name of the database you want to drop
database_names = ['new_db', "_archive_db"]

try:
    # Establish a database connection (without specifying the database)
    db_connection = mysql.connector.connect(**db_config)
    cursor = db_connection.cursor()
    print("Successfully connected to the MySQL server")

    # Drop the database
    for database_name in database_names:
        drop_query = f"DROP DATABASE IF EXISTS {database_name};"
        cursor.execute(drop_query)
        print(f"Database '{database_name}' has been dropped.")
        create_query = f"CREATE DATABASE {database_name};"
        cursor.execute(create_query)

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the database connection
    if db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("Database connection is closed")

with open("first_names.txt") as f:
    first_names = [l.strip() for l in f.readlines()]
with open("last_names.txt") as f:
    last_names = [l.strip() for l in f.readlines()]
with open("domains.txt") as f:
    domains = [l.strip() for l in f.readlines()]
date_min = datetime.date(2020, 1, 1)
date_max = datetime.date(2022, 12, 31)
dates = []
current_date = date_min
while current_date <= date_max:
    dates.append(current_date)
    current_date += datetime.timedelta(days = 1)

# Insert 100 dummy users into the table
user_table = {
    0: {
        "first_name": "Kendal",
        "last_name": "Ozzel",
        "name": "Kendal Ozzel",
        "email": "kendal.ozzel@empire.mil",
        "password": "tooCLOSEtoHOTH",
        "password_hash": hashlib.md5(bytes("tooCLOSEtoHOTH".encode("utf-8"))).hexdigest(),
        "account_created": datetime.date(2020, 9, 13),
        "pwd_changed": datetime.date(2020, 9, 13)
    }
}
for i in range(1, 101):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 12))
    email_pattern = random.choice([1, 2, 3, 4])
    match email_pattern:
        case 1:
            email = f"{fname.lower()}{lname.lower()}@{random.choice(domains)}"
        case 2:
            email = f"{fname.lower()}.{lname.lower()}@{random.choice(domains)}"
        case 3:
            email = f"{fname.lower()[0]}{lname.lower()}@{random.choice(domains)}"
        case _:
            email = f"{lname.lower()}@{random.choice(domains)}"
    joined_date = random.choice(dates)
    pwd_changed = joined_date + datetime.timedelta(days = random.randint(0, (date_max - joined_date).days))
    
    user_table[i] = {
        "first_name": fname,
        "last_name": lname,
        "name": f"{fname} {lname}",
        "email": email,
        "password": password,
        "password_hash": hashlib.md5(bytes(password.encode("utf-8"))).hexdigest(),
        "account_created": joined_date,
        "pwd_changed": pwd_changed
    }
    #cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    
    first_names.remove(fname)
    last_names.remove(lname)

users_list = []
users_list.append(sorted([[k, user_table[k]["account_created"]] for k in user_table], key = lambda x:x[1]))
archive_cutoff = datetime.date(2021, 1, 1)
users_list.append(sorted([[k, user_table[k]["account_created"]] for k in user_table if user_table[k]["account_created"] < archive_cutoff], key = lambda x:x[1]))

# Index 0 is "new", index 1 is "archive"
for i in range(2):
    # Remove the dates, don't need them any more
    users_list[i] = [l[0] for l in users_list[i]]
    # Database connection parameters
    db_config = {
        'user': 'root',
        'password': 'redoubleEFFORT1234',
        'host': '192.168.40.4',
        'database': database_names[i],
    }

    try:
        # Establish a database connection
        db_connection = mysql.connector.connect(**db_config)
        cursor = db_connection.cursor()
        print("Successfully connected to the database")

        # Create the 'users' table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(32),
            account_created DATE,
            pwd_changed DATE
        );
        """
        cursor.execute(create_table_query)

        # Now, insert data into the MySQL table
        for j in users_list[i]:
            user = user_table[j]
            insert_query = """
            INSERT INTO users (name, email, password, account_created, pwd_changed)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                user['name'],
                user['email'], 
                user['password_hash' if i == 0 else 'password'],
                user['account_created'], 
                user['pwd_changed']
            ))
        
        # Commit the changes
        db_connection.commit()
        print(f"{cursor.rowcount} records inserted.")
        
    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Database connection is closed")
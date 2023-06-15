# Step 0 - import sqlite3
import sqlite3
import queries as q

# Step1
# Connect to the Database
# triple check spelling of database filename
connection = sqlite3.connect('rpg_db.sqlite3')

#Step2 - Make the cursor
cursor = connection.cursor()

#Step3 - Write a query
#(See queries.py file)

#Step4 - Execute the query on the cursor and fetch the results
# 'pulling the results' from the cursor
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])
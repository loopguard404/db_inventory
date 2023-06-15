#!/usr/bin/env python

import json
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Get a cursor
cur = conn.cursor()

# Execute a query to get the list of hosts
cur.execute("SELECT hostname, ip_address FROM hosts")

# Fetch the results
rows = cur.fetchall()

# Close the cursor and the connection
cur.close()
conn.close()

# Create the inventory dictionary
inventory = {
    "all": {
        "hosts": []
    }
}

# Add the hosts to the inventory
for row in rows:
    inventory["all"]["hosts"].append(row[1])

# Print the inventory in JSON format
print(json.dumps(inventory))

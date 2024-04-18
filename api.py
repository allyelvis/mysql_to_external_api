import mysql.connector
import requests
import json

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)
mycursor = mydb.cursor()

# Fetch data from MySQL
mycursor.execute("SELECT * FROM your_table")
result = mycursor.fetchall()

# Convert to JSON
data = []
for row in result:
    data.append({
        'column1': row[0],
        'column2': row[1],
        # Add more columns as needed
    })

# Convert to JSON string
json_data = json.dumps(data)

# Connect to External API
url = 'https://example.com/api/endpoint'
headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, data=json_data)

# Handle response
if response.status_code == 200:
    print("Data sent successfully!")
else:
    print("Error:", response.text)

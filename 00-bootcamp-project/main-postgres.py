import csv
import configparser

import psycopg2


parser = configparser.ConfigParser()
parser.read("pipeline.conf")
dbname = parser.get("postgres_config", "database")
user = parser.get("postgres_config", "username")
password = parser.get("postgres_config", "password")
host = parser.get("postgres_config", "host")
port = parser.get("postgres_config", "port")

#connect to PostGres
conn_str = f"dbname={dbname} user={user} password={password} host={host} port={port}" #connection string
#f-string allows user to specify variable inside the string (String Substitution)
conn = psycopg2.connect(conn_str) #connect
cursor = conn.cursor() #cursor execution

DATA_FOLDER = "data"

table = "addresses"
header = ["address_id", "address", "zipcode", "state", "country"]
with open(f"{DATA_FOLDER}/addresses.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    query = f"select * from {table}"
    cursor.execute(query)

    results = cursor.fetchall() # เอา Result ทั้งหมดออกมา
    for each in results:
        writer.writerow(each)

table = "order_items"
header = ["order_id", "product_id", "quantity"]
# ลองดึงข้อมูลจากตาราง order_items และเขียนลงไฟล์ CSV
# YOUR CODE HERE
with open(f"{DATA_FOLDER}/order_items.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    query = f"select * from {table}"
    cursor.execute(query)

    results = cursor.fetchall()
    for each in results:
        writer.writerow(each)
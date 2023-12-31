"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/NC_data.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    file = "PatientDB.db"
    conn = sqlite3.connect(file)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS PatientDB")
    c.execute(
        """
    CREATE TABLE PatientDB 
    ("Index","Customer Id","First Name","Last Name",Company,City,Country,"Phone 1","Phone 2",Email,"Subscription Date",Website)"""
    )
    # insert
    c.executemany("INSERT INTO PatientDB VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", payload)

    conn.commit()
    conn.close()
    return "PatientDB.db"

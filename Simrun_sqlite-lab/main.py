"""
ETL-Query script
"""
import fire
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

def main(the_query):
  # Extract
  print("Extracting data...")
  extract()

  # Transform and load
  print("Transforming data...")
  load()

  # Query
  print("Querying data...")
  query(the_query)

if __name__ == "__main__":
  fire.Fire(main)

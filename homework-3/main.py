from model.db_model import Users
from modules.regex_operations import Regex
from modules.jsonfile_operations import Json
from modules.db_operations import Database
import argparse

def main():

    parser = argparse.ArgumentParser() # Create the parser
    parser.add_argument("--jp", type=str, required=True)  # Add --file argument
    parser.add_argument("--dp", type=str, required=True) # Add --db argument
    args = parser.parse_args() # Parse the argument

    json_path = args.jp #Set file as argument
    database_path = args.dp #Set db as argument

    try:
        read_json = Json(json_path) #Calls "dataregex.json"
        database = Database(database_path) # Calls  "dataregex.db"
        user_list = read_json.create_user
        database.create_table() # Create table
        database.bulk_insert(user_list)

    except:
        print("Transaction failed.")


if __name__ == '__main__':
    main()

# HELPER: You can run the following command from terminal.
# python3 main.py --jp "dataregex.json" --dp "dataregex.db"

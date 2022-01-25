from modules.regex_operations import Regex
from model.db_model import Users
import json

class Json():

    def __init__(self, filename):
        self.filename = filename

    def get_json(self):
        """
        This functions reads json file
        """
        with open(self.filename, "r") as json_file:
            data = json.load(json_file)

            return data

    @property
    def create_user(self):
        """
        This functions assigns the information in the json file read to the user.
        """

        json_data = self.get_json()  # Calls data from json file
        rgx = Regex()  # Calls regex methods
        data_list = list()

        for data in json_data:
            user = Users()
            user.email = data["email"]
            user.username = data["username"]
            user.name_surname = data["profile"]["name"]
            user.emailuserlk = rgx.email_validate(user.email,
                                                  user.username)
            user.usernamelk = rgx.username_validate(data["username"], data["profile"][
                "name"])
            dob_raw = data["profile"]["dob"] # dob read data read as row
            dob_raw = dob_raw.split("-") # line is separated by '-'
            user.year_of_birth = dob_raw[0]
            user.month_of_birth = dob_raw[1]
            user.day_of_birth = dob_raw[2]
            user.country = data.get("profile").get("address").split()[-1]  # Getting city information from address
            # information

            data_list.append(user)  # Append created user to the data_list

        return data_list


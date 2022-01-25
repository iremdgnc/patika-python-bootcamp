

class Regex():

    def email_validate(self, email, username):
        """
        This functions checking whether the e-mail contains the username or part of it (at least 3 letters).
        """

        username = username.lower()
        email = email.lower()
        username = username.replace(" ", "")
        for i in range(0, len(username) - 2):
            substring = username[i:i + 3]
            if substring in email:
                return 1
        return 0

    def username_validate(self, username, name_surname):
        """
        This functions it is checked whether it contains a part of the username and the user's name or surname.
        """
        name_surname = name_surname.lower()
        username = username.lower()
        for i in range(0, len(name_surname) - 2):
            substring = name_surname[i:i + 3]
            if substring in username:
                return 1
        return 0


import re

class RegistrationForm:
    
    def __init__(self, Fname, Lname, username, email, password, confirm_password):
        self.Fname = Fname
        self.Lname = Lname
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
    
    def data_exists(self):
        if not self.Fname or not self.Lname or not self.username or not self.email or not self.password or not self.confirm_password:
            return False
        else:
            return True

    def valid_name(self):
        if len(self.username) < 3 or len(self.username) > 20:
            return False
        else:
            return True

    @classmethod
    def valid_email(cls, email):
        cls.email = email
        regex = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        
        if not re.match(regex, cls.email):
            return False
        else:
            return True

    @classmethod
    def valid_password(cls, password):
        cls.password = password
        regex = re.compile(r'[a-zA-Z0-9@_+-.]{3,}$')
        # regex = re.compile(r'^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z](?=.*?[^A-Za-z\s0-9]))')

        if not re.match(regex, cls.password):
            return False
        else:
            return True

    def valid_confirm_password(self):
        if self.password != self.confirm_password:
            return False
        else:
            return True

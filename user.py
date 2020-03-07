from base import Base


class User(Base):

    __slots__ = 'username', 'password', 'groups'

    def __init__(self, username, password, groups=[]):
        super.__init__()
        self.username = username
        self.password = hash(password)
        self.groups = groups

    def __str__(self):
        return "The username is " + str(self.username) + \
            ". \nThe password is " + str(self.password) + \
            ". \nThe user belongs to the group: " + str(self.groups)

    def change_username(self, old, new):
        self.username = new

    def change_password(self, old, new):
        self.password = new

    def password_match(self, attempt):
        return self.password == hash(attempt)

    def load_json_dict(self, json_dict):
        self.username = json_dict["username"]
        self.password = json_dict["password"]
        self.groups = json_dict["groups"]

    def dump_json_dict(self):
        return {"username": self.username,
                "password": self.password,
                "groups": self.groups}

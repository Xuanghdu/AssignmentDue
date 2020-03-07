class User:

    __slots__ = 'user', 'password', 'groups'

    def __init__(self, username, password, groups=set()):
        self.user = username
        self.password = hash(password)
        self.groups = groups

    def __str__(self):
        return "The username is " + str(self.user) + \
            ". \nThe password is " + str(self.password) + \
            ". \nThe user belongs to the group: " + str(self.groups)

    def change_username(self, old, new):
        self.user = new

    def change_password(self, old, new):
        self.password = new

    def password_match(self, attempt):
        return self.password == hash(attempt)

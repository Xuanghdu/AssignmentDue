class User:
    def __init__(self,username,password,groups=None):
        self.user=username
        self.password=password
        self.groups=groups

    def __str__(self):
        return "The username is "+str(self.user)+". \nThe password is"+str(self.password)+". \nThe user belongs to the group"+str(self.groups)

    def change_username(self,old,new):
        self.user=new

    def change_password(self,old,new):
        self.password=new

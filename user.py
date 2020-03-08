# from base import Base
import group

# class User(Base):
class User():

    __slots__ = 'username', 'password', 'groups'

    def __init__(self, username, password, groups=[]):
        # super.__init__()
        self.username = username
        self.password = hash(password)
        self.groups = groups

    def __str__(self):
        return "The username is " + str(self.username) + \
            ". \nThe hashed password is " + str(self.password) + \
            ". \nThe user belongs to the group: " + str(self.groups)

    def change_username(self, old, new):
        self.username = new
        # TODO: main (command & gui to check if the new username is available)

    def change_password(self, old, new):
        if hash(old) == self.password:
            self.password = hash(new)
        else:
            print("Incorrect old password!")

    def check_password(self, attempt):
        return self.password == hash(attempt)

    def enter_group(self, group):
        if group not in self.groups:
            self.groups.append(group)
            group.add_user(self)
        else:
            print("You are already in " + group.groupname)

    def invite(self, user, group):
        if group not in self.groups:
            user.groups.append(group)
            group.add_user(user)
        else:
            print(user.username + " is already in " + group.groupname)

    def add_task(self, group, task):
        # if task not in group.tasks:
            group.add_task(task)
        # else:
            # print(task.taskname + " is already in " + group.groupname)

    def complete_task(self, group, task):
        group.complete_task(task, self)

    def delete_task(self, group, task):
        group.delete_task(task)

    def restore_task(self, group, task):
        group.restore_task(task)

    # def load_json_dict(self, json_dict):
    #     self.username = json_dict["username"]
    #     self.password = json_dict["password"]
    #     self.groups = json_dict["groups"]

    # def dump_json_dict(self):
    #     return {"username": self.username,
    #             "password": self.password,
    #             "groups": self.groups}

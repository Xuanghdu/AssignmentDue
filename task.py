# from base import Base
from datetime import datetime

# class Task(Base):
class Task():

    __slots__ = 'taskname', 'description', 'group', 'due_date', 'add_date', 'divisions', 'timestamp', 'dependencies'

    def __init__(self, taskname, description, group, due_date=[], divisions=[set()], dependencies=[]):
        # super.__init__()
        self.taskname = taskname
        self.description = description
        self.due_date = due_date
        self.group = group
        self.divisions = divisions
        self.dependencies = dependencies
        now = datetime.now()
        self.timestamp = datetime.timestamp()
        self.add_date = now.utctimetuple()[:5]

    def __iter__(self):
        for dep in self.divisions:
            for user in dep:
                yield user

    def add_dependency(self, user1, user2):
        '''(Task, User, User) -> None'''
        index1, index2 = -1, -1
        for i in range(len(self.divisions)):
            if user1 in self.divisions[i]:
                index1 = i
                break
        for i in range(len(self.divisions)):
            if user2 in self.divisions[i]:
                index2 = i
                break
        if index1 >= 0 and index2 >= 0:
            # both users exists in the task
            if index1 == index2:
                # already in the same set
                pass
            else:
                # merge two sets
                self.divisions[index1] = \
                    self.divisions[index1].union(self.divisions[index2])
                del self.divisions[index2]
        elif index1 >= 0:
            # user1 in the task but user2 does not
            self.divisions[index1].add[user2]
        elif index2 >= 0:
            # user2 in the task but user1 does not
            self.divisions[index2].add[user1]
        else:
            # neither user is in the task
            self.divisions.append({user1, user2})

    # Remove???
    def finish_task(self, user):
        '''(Task, User) -> None'''
        index = -1
        for i in range(self.divisions):
            if user in self.divisions[i]:
                index = i
                break
        if index < 0:
            raise Exception('User should not have access of the task')
        del self.divisions[index]

    # def load_json_dict(self, load_json_dict):
    #     self.group = load_json_dict["group"]
    #     self.content = load_json_dict["content"]
    #     self.due_date = load_json_dict["due_date"]
    #     self.divisions = load_json_dict["divisions"]

    # def dump_json_dict(self):
    #     return {"group": self.group,
    #             "content": self.content,
    #             "due_date": self.due_date,
    #             "divisions", self.divisions}

class Group:

    __slots__ = 'groupname', 'tasks', 'users', 'user_to_task', 'trash'

    def __init__(self, groupname, users=[], tasks=[], trash=[]):
        self.groupname = groupname
        self.users = users
        self.tasks = tasks
        self.trash = trash
        # self.user_to_task = dict()

    def add_user(self, user):
        self.users.append(user)

    def create_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task, user):
        # TODO: need rework since should edit task divisions instead of removing the task directly
        # user unused
        self.tasks.remove(task)
        self.trash.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def restore_task(self, task):
        self.trash.remove(task)
        self.tasks.append(task)

    # def update_group(self):
    #     for task in self.tasks:
    #         for user in task.divisions:
    #             if user not in self.user_to_task.keys():
    #                 self.user_to_task[user] = set()
    #             self.user_to_task[user].add(task)


    def __str__(self):
        return "tasks:" + str(self.tasks) + \
             "\nusers:" + str(self.users) # + \
    #   "\nuser_to_task:" + str(self.user_to_task)
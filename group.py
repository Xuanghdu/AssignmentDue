class Group:

    __slots__ = 'groupname', 'tasks', 'users', 'user_to_task', 'completed', \
        'deleted'

    def __init__(self, groupname, users=[], tasks=[]):
        self.groupname = groupname
        self.users = users
        self.tasks = tasks
        self.completed = []
        self.deleted = []
        # self.user_to_task = dict()

    def add_user(self, user):
        self.users.append(user)

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task, user):
        # TODO: need rework since should edit task divisions instead of
        # removing the task directly
        # user unused
        task.complete_task(user)
        if len(task.divisions) == 0:
            self.tasks.remove(task)
            self.completed.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)
        self.deleted.append(task)

    def restore_task(self, task):
        # TODO: cannot restore from completion
        self.deleted.remove(task)
        self.tasks.append(task)

    # def update_group(self):
    #     for task in self.tasks:
    #         for user in task.divisions:
    #             if user not in self.user_to_task.keys():
    #                 self.user_to_task[user] = set()
    #             self.user_to_task[user].add(task)

    def __str__(self):
        return "tasks:" + str(self.tasks) + \
            "\nusers:" + str(self.users)  # + \
    #   "\nuser_to_task:" + str(self.user_to_task)

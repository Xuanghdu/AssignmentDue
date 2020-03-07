class Group:

    __slots__ = 'tasks', 'users', 'user_to_task'

    def __init__(self, tasks=set(), users=set()):
        '''
        params:
            tasks set<task.obj>
            users set<user.obj>
        attributs:
            self.tasks set<task.obj>
            self.users set<task.obj>
            self.user_to_task = <dict>
        '''
        self.tasks = tasks
        self.users = users
        self.user_to_task = dict()

    def add_user(self, user):
        '''
        user.obj -> None
        '''
        self.users.add(user)

    def add_task(self, task):
        '''
        task.obj -> None
        '''
        self.tasks.add(task)

    def update_group(self):
        '''
        update the user_to_task dictionary
        '''
        for task in self.tasks:
            for user in task.stakeholders:
                if user not in self.user_to_task.keys():
                    self.user_to_task[user] = set()
                self.user_to_task[user].add(task)


    def __str__(self):
        return "tasks:" + str(self.tasks) + \
             "\nusers:" + str(self.users) + \
      "\nuser_to_task:" + str(self.user_to_task)
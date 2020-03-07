class Group:
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
        # for task in tasks:
        #     for user in task.stakeholders:
        #         user_to_task


    def __str__(self):
        return "tasks:" + self.tasks + "\n" + "users:" + self.users + "\n" + "user_to_task:"
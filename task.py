class Task:

    __slots__ = 'group', 'content', 'due_date', 'stakeholders'

    def __init__(self, group, content, due_date=None, stakeholders=[]):
        self.group = group
        self.content = content
        self.due_date = due_date
        self.stakeholders = stakeholders

    def add_dependency(self, user1, user2):
        index1, index2 = -1, -1
        for i in range(len(self.stakeholders)):
            if user1 in self.stakeholders[i]:
                index1 = i
                break
        for i in range(len(self.stakeholders)):
            if user2 in self.stakeholders[i]:
                index2 = i
                break
        if index1 >= 0 and index2 >= 0:
            # both users exists in the task
            if index1 == index2:
                # already in the same set
                pass
            else:
                # merge two sets
                set2 = self.stakeholders[index2]
                del self.stakeholders[index2]
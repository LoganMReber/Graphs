class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Person:
    def __init__(self, id):
        self.id = id
        self.parents = []
        self.children = []

    def __repr__(self):
        return f'{self.parents}=>{self.id}=>{self.children}'

    def addChild(self, id):
        self.children.append(id)

    def addParent(self, id):
        self.parents.append(id)


def dfs(people, current, depth=0):

    oldest = -1

    if depth:
        oldest = current

    parents = people[current].parents

    if not parents:
        return (depth, oldest)

    if len(parents) == 1:
        return dfs(people, parents[0], depth+1)
    else:
        cases = [dfs(people, parents[1], depth+1),
                 dfs(people, parents[0], depth+1)]

        if cases[0][0] > cases[1][0]:
            return cases[0]
        else:
            return cases[1]


def earliest_ancestor(ancestors, starting_node):
    people = dict()
    for pair in ancestors:
        if pair[0] not in people:
            people[pair[0]] = Person(pair[0])
        if pair[1] not in people:
            people[pair[1]] = Person(pair[1])
        people[pair[1]].addParent(pair[0])
        people[pair[0]].addChild(pair[1])

    return dfs(people, starting_node)[1]

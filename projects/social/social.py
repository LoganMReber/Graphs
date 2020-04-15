import random


class Queue:
    def __init__(self):
        self.store = []

    def enqueue(self, item):
        self.store.append(item)

    def dequeue(self):
        return self.store.pop(0)

    def size(self):
        return len(self.store)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(num_users):
            self.users[i] = set()
            self.friendships[i] = set()
        limit_friends = avg_friendships * 2
        for i in range(num_users):
            friends_roll = int(random.random()*limit_friends)
            for j in range(friends_roll):
                userRoll = int(random.random()*num_users)
                if userRoll == i:
                    continue
                else:
                    self.friendships[i].add(userRoll)
                    self.friendships[userRoll].add(i)

    def get_all_social_paths(self, user_id):
        visited = {}
        unmapped = Queue()
        unmapped.enqueue([user_id])
        visited[user_id] = True
        while unmapped.size():
            path = unmapped.dequeue()
            target = path[-1]
            if target == user_id:
                path.pop()
            for friend in self.friendships[target]:
                if friend not in visited:
                    newPath = list(path) + [friend]
                    visited[friend] = newPath
                    unmapped.enqueue(newPath)

        del visited[user_id]
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

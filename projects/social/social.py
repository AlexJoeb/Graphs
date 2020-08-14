from collections import deque
import random


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
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        for i in range(0, num_users):
            self.add_user(i)
        
        # Create friendships

        possibles = []
        for uid in self.users:
            for fid in range(uid + 1, self.last_id + 1):
                possibles.append((uid, fid))

        random.shuffle(possibles) # Shuffle the friendship list.

        for indx in range(num_users * avg_friendships // 2):
            friendship = possibles[indx]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Approach: Taking a breadth-first search approach to this so I can incrementally step through friends and keep track of their relations.
        def bfs(user_id):

            queue = deque() # Initialize a queue.
            queue.append([user_id]) # Append the starting friend

            while len(queue):
                path = queue.pop()
                vert = path[-1]
                if vert not in visited:
                    visited[vert] = path
                    
                    for friend in self.friendships[vert]:
                        path_copy = list(path)
                        path_copy.append(friend)
                        q.append(path_copy)
        bfs(user_id)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f'Friendships: {sg.friendships}')
    connections = sg.get_all_social_paths(1)
    print(f"Connections: {connections}")

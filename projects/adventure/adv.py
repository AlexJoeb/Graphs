from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = [] # Final path of traversal that will hit all rooms.
visited = {}  # Already visited rooms.
path = []  # Current path being traversed.
opposites = {
    'n':  's',
    'e':  'w',
    'w':  'e',
    's':  'n'
}

# Append the current room to visited.. since we're here already.
visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) < len(room_graph) - 1: # While there are still rooms that have not been visited.. len(room_graph) subtract one to offset the index.
    if player.current_room.id not in visited:
        # Rooms have been traversed - player no longer in starting room. If the current room is not in visited, add it.
        visited[player.current_room.id] = player.current_room.get_exits()
        # Shuffle the exits.
        random.shuffle(visited[player.current_room.id])
        # Remove the last direction we came from, because we don't wanna go back that way.
        visited[player.current_room.id].remove(path[-1]) 

    while len(visited[player.current_room.id]) < 1: # While there is less than one direction to go.
        last_dir = path.pop() # Get the path of the direction we're coming from.
        traversal_path.append(last_dir) # Add last direction to travel_path.
        player.travel(last_dir) # Backtrack last direction.
    
    next_dir = visited[player.current_room.id].pop(0) # Take the next direct from the front of the list.
    traversal_path.append(next_dir) # Append the move to traversal_path.
    path.append(opposites[next_dir]) # Append opposite direction to current move path.
    player.travel(next_dir) # Travel to next_dir.




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
import pygame, collections, math, random

class SquareGrid:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.walls = []
        self.entities = []
    
    def in_bounds(self, location):
        (x, y) = location
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, location):
        for block in self.walls:
            if block == location:
                return False
        return True

    def clearEntities(self):
        self.entities = []

    def neighbors(self, location):
        (x, y) = location
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
        '''
        if (x + y) % 2 == 0:
            neighbors.reverse()
        '''
        #print(neighbors)
        for neighbor in neighbors:
            
            if not self.in_bounds(neighbor):
                print("removing : " + str(neighbor))
                neighbors.remove(neighbor)
                continue
            if not self.passable(neighbor):
                print("removing : " + str(neighbor))
                neighbors.remove(neighbor)
            
        return neighbors
'''
class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))
'''    
'''
def pathFind(grid, start, goal):
    
    open_list = []
    closed_list = []

    start_node = Node(start, None)
    end_node = Node(goal, None)

    open_list.append(start_node)

    while len(open_list) > 0:
        open_list.sort()

        current_node = open_list.pop(0)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            while current_node != start_node:
                if current_node != end_node:
                    path.append(current_node.position)
                current_node = current_node.parent
            if path == []:
                return None
            return path[-1]
        
        (x, y) = current_node.position

        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for next in neighbors:
            
            if next in grid.walls:
                continue
            
            neighbor = Node(next, current_node)

            if neighbor in closed_list:
                continue

            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - end_node.position[0]) + abs(neighbor.position[1] - end_node.position[1])
            neighbor.f = neighbor.g + neighbor.h

            if(add_to_open(open_list, neighbor)):
                open_list.append(neighbor)
            
    return None

def add_to_open(open_list, neighbor):
    for node in open_list:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True
'''
def findNextMove(start, goal, grid):
    choice = random.randint(1, 2)
    temp = list(grid.neighbors(start))
    if len(temp) == 0:
        print("???")
        return None
    if (start[0] < goal[0] and choice == 1) or (start[1] == goal[1] and choice == 2):
        if grid.in_bounds((start[0] + 1, start[1])) and (start[0] + 1, start[1]) not in grid.walls:
            return (start[0] + 1, start[1])
    elif (start[0] > goal[0] and choice == 1) or (start[1] == goal[1] and choice == 2):
        if grid.in_bounds((start[0] - 1, start[1])) and (start[0] - 1, start[1]) not in grid.walls:
            return (start[0] - 1, start[1])
    elif (start[1] < goal[1] and choice == 2) or (start[0] == goal[0] and choice == 1):
        if grid.in_bounds((start[0], start[1] + 1)) and (start[0], start[1] + 1) not in grid.walls:
            return (start[0], start[1] + 1)
    elif (start[1] > goal[1] and choice == 2) or (start[0] == goal[0] and choice == 1) :
        if grid.in_bounds((start[0], start[1] - 1)) and (start[0], start[1] - 1) not in grid.walls:
            return (start[0], start[1] - 1)
    return temp[0]
    
    

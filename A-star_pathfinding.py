import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class Node:
 
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position

#This function return the path of the search
def return_path(current_node,maze):
    path = []
    coordinates=[]
    no_rows, no_columns = np.shape(maze) #shape da las dimensiones renglon columna
    # here we create the initialized result maze with -1 in every position
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    # Return reversed path as we need to show from start to end path
    path = path[::-1]
    start_value = 0
    # we update the path of start to end found by A-star serch with every step incremented by 1
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        coordinates.append([path[i][0]])
        coordinates.append([path[i][1]])
        start_value += 1
    return result , coordinates
  
    
def search(maze, cost, start, end):

    # Create start and end node with initized values for g, h and f
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both yet_to_visit and visited list
    # in this list we will put all node that are yet_to_visit for exploration. 
    # From here we will find the lowest cost node to expand next
    yet_to_visit_list = []  
    # in this list we will put all node those already explored so that we don't explore it again
    visited_list = [] 
    
    # Add the start node
    yet_to_visit_list.append(start_node)
    
    # Adding a stop condition. This is to avoid any infinite loop and stop 
    # execution after some reasonable number of steps
    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 10

    # what squares do we search . serarch movement is left-right-top-bottom 
    #(4 movements) from every positon

    move  =  [[-1, 0 ], # go up
              [ 0, -1], # go left
              [ 1, 0 ], # go down
              [ 0, 1 ]] # go right


    #find maze has got how many rows and columns 
    no_rows, no_columns = np.shape(maze)
    
    # Loop until you find the end
    
    while len(yet_to_visit_list) > 0:
        
        # Every time any node is referred from yet_to_visit list, counter of limit operation incremented
        outer_iterations += 1    

        
        # Get the current node
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
                
        # if we hit this point return the path such as it may be no solution or 
        # computation cost is too high
        if outer_iterations > max_iterations:
            print ("giving up on pathfinding too many iterations")
            return return_path(current_node,maze)

        # Pop current node out off yet_to_visit list, add to visited list
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        # test if goal is reached or not, if yes then return the path
        if current_node == end_node:
            return return_path(current_node,maze)

        # Generate children from all adjacent squares
        children = []

        for new_position in move: 

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range (check if within maze boundary)
            if (node_position[0] > (no_rows - 1) or 
                node_position[0] < 0 or 
                node_position[1] > (no_columns -1) or 
                node_position[1] < 0):
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            
            # Child is on the visited list (search entire visited list)
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + cost
            ## Heuristic costs calculated here, this is using eucledian distance
            child.h = (((child.position[0] - end_node.position[0]) ** 2) + 
                       ((child.position[1] - end_node.position[1]) ** 2)) 

            child.f = child.g + child.h

            # Child is already in the yet_to_visit list and g cost is already lower
            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                continue

            # Add the child to the yet_to_visit list
            yet_to_visit_list.append(child)


if __name__ == '__main__':

    """
    maze = [[0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    """
    maze = [[0, 1, 1, 0, 0, 0,0,0,0,0],
            [0, 0, 0, 1, 0, 0,0,0,0,0],
            [0, 1, 0, 1, 0, 0,0,0,0,0],
            [0, 1, 0, 0, 1, 0,0,0,0,0],
            [0, 0, 0, 0, 1, 0,0,0,0,0],
            [0, 0, 0, 0, 0, 0,0,0,0,0],
            [0, 0, 0, 0, 0, 0,0,0,0,0],
            [0, 0, 0, 0, 0, 0,0,0,0,0],
            [0, 0, 0, 0, 0, 0,0,0,0,0],]
    
    start = [1, 0] # starting position
    end_obs = [4,5] # ending position
    Real_end=[2,8]
    cost = 1 # cost per movement

    path,coordinates = search(maze,cost, start, end_obs)
    no_rows, no_columns = np.shape(maze) 
    
    def troceo(lisa, n):
         final=list(zip(*[iter(lisa)]*n))
         ren_coordinate = [i[0] for i in final]
         col_coordinate = [i[1] for i in final]
         return ren_coordinate , col_coordinate
     
    ren,col=troceo(coordinates,2)
    no_rows, no_columns = np.shape(maze) 
    obstaculos=[]

    for i in range(no_rows):
        for j in range(no_columns):
            if maze[i][j]==1:
                obstaculos.append(i)
                obstaculos.append(j)
                
    ren_obs,col_obs=troceo(obstaculos,2)      
    
print('\n')    
print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in path]))


L=np.array([[1,-1],
            [0,0]])

def model(x,t):
    
    dx1=-(x[0]-x[2])
    dx2=-(x[1]-x[3]) 
    dx3= 0 
    dx4=0
    xp = [dx1,dx2,dx3,dx4]         
    return xp

# initial condition
x0 = [end_obs[0],end_obs[1],Real_end[0],Real_end[1]]

# time points
t = np.linspace(0,30)

# solve ODE
y = odeint(model,x0,t)

plt.figure()
plt.axhline(y=5, xmin=-1, xmax=0.7 , color='orange')
plt.axvline(x=6, ymin=-0.1, ymax=0.6 , color='orange')
plt.plot(ren,col,color='green')
plt.scatter(ren_obs,col_obs,color='red')
plt.axis([-1, 9, -1, 9])
plt.plot(y[:,0],y[:,1],color='green')
plt.scatter(start[0],start[1],color='blue')
plt.scatter(x0[2],x0[3],color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('A* + Consenso')
plt.grid()
plt.show()



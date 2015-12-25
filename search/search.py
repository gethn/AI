# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

	#Initialise the fringe by expanding Start State
    fringe = util.Stack()
    for newnode in problem.getSuccessors(problem.getStartState()):
        
        #Add total cost to end of successors and add to fringe
        newnode += (newnode[-1],)
        fringe.push(newnode)
    
    #Initialise closed list
    closed = [problem.getStartState()]

    while True:

        #Check if fringe is empty and pop new node
        if fringe.isEmpty(): 
            print "Fringe Empty: No Solution!"
            return None
        node = fringe.pop()

        #Check if node has already been expanded
        if not node[0] in closed:

            #Check if node is Goal State
            if problem.isGoalState(node[0]): 
                return list(node[1:-2])
            
            #Create successors and add to fringe
            for newnode in problem.getSuccessors(node[0]):
                
                #Add path into successors and total cost onto end of successors
                newnode += (node[-1] + newnode[-1],)
                newnode = newnode[0:1] + node[1:-2] + newnode[1:]
                fringe.push(newnode)

            #Add node to closed list
            closed.append(node[0])

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

	#Initialise the fringe by expanding Start State
    fringe = util.Queue()
    for newnode in problem.getSuccessors(problem.getStartState()):
        
        #Add total cost to end of successors and add to fringe
        newnode += (newnode[-1],)
        fringe.push(newnode)
    
    #Initialise closed list
    closed = [problem.getStartState()]

    while True:

        #Check if fringe is empty and pop new node
        if fringe.isEmpty(): 
            print "Fringe Empty: No Solution!"
            return None
        node = fringe.pop()

        #Check if node has already been expanded
        if not node[0] in closed:

            #Check if node is Goal State
            if problem.isGoalState(node[0]): 
                return list(node[1:-2])
            
            #Create successors and add to fringe
            for newnode in problem.getSuccessors(node[0]):
                
                #Add path into successors and total cost onto end of successors
                newnode += (node[-1] + newnode[-1],)
                newnode = newnode[0:1] + node[1:-2] + newnode[1:]
                fringe.push(newnode)

            #Add node to closed list
            closed.append(node[0])

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

	#Initialise the fringe by expanding Start State
    fringe = util.PriorityQueue()
    for newnode in problem.getSuccessors(problem.getStartState()):
        
        #Add total cost to end of successors and add to fringe
        newnode += (newnode[-1],)
        fringe.push(newnode, newnode[-1])
    
    #Initialise closed list
    closed = [problem.getStartState()]

    while True:

        #Check if fringe is empty and pop new node
        if fringe.isEmpty(): 
            print "Fringe Empty: No Solution!"
            return None
        node = fringe.pop()

        #Check if node has already been expanded
        if not node[0] in closed:

            #Check if node is Goal State
            if problem.isGoalState(node[0]): 
                return list(node[1:-2])
            
            #Create successors and add to fringe
            for newnode in problem.getSuccessors(node[0]):
                
                #Add path into successors and total cost onto end of successors
                newnode += (node[-1] + newnode[-1],)
                newnode = newnode[0:1] + node[1:-2] + newnode[1:]
                fringe.push(newnode, newnode[-1])

            #Add node to closed list
            closed.append(node[0])

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

	#Initialise the fringe by expanding Start State
    fringe = util.PriorityQueue()
    for newnode in problem.getSuccessors(problem.getStartState()):
        
        #Add total cost to end of successors and add to fringe
        newnode += (newnode[-1],)
        fringe.push(newnode, newnode[-1] + heuristic(newnode[0], problem))
        
    #Initialise closed list
    closed = [problem.getStartState()]

    while True:

        #Check if fringe is empty and pop new node
        if fringe.isEmpty(): 
            print "Fringe Empty: No Solution!"
            return None
        node = fringe.pop()

        #Check if node has already been expanded
        if not node[0] in closed:

            #Check if node is Goal State
            if problem.isGoalState(node[0]): 
                return list(node[1:-2])
            
            #Create successors and add to fringe
            for newnode in problem.getSuccessors(node[0]):
                
                #Add path into successors and total cost onto end of successors
                newnode += (node[-1] + newnode[-1],)
                newnode = newnode[0:1] + node[1:-2] + newnode[1:]
                fringe.push(newnode, newnode[-1] + heuristic(newnode[0], problem))

            #Add node to closed list
            closed.append(node[0])

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

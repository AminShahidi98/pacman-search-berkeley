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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    #start of my code
    #setting up requirments
    start_state = problem.getStartState()
    fringe =  util.Stack()
    fringe_history = []
    expanded = []
    minimal_expanded = []
    steps = []
    aux_count = 0
    #setting up directions
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    #check if the start position is the Goal
    if problem.isGoalState(problem.getStartState()):
        return []
    
    successors = problem.getSuccessors(start_state)
    for s in successors:
        fringe.push(s)
        fringe_history.append(s[0])
    expanded.append(start_state)
    minimal_expanded.append(start_state)
    #check child parrents
    while True:
        if fringe.isEmpty():
            break
        aux_count = 0
        choice = fringe.pop()
        steps.append(choice[1])
        expanded.append(choice[0])
        #setting up output containig of actions with correct variables
        if problem.isGoalState(choice[0]):
            print(steps)
            for i in steps:
                if i == "South":
                    i = s
                elif i == "North":
                    i = n
                elif i == "West":
                    i == w
                elif i == "East":
                    i == e
            return steps
        successors = problem.getSuccessors(choice[0])
        #check if all the succesors are expanded before or not
        for s in successors:
            if s[0] in expanded:
                aux_count = aux_count + 1
        #go backward when there is no non-expanded successor (we are in a trap)       
        if aux_count == len(successors):
            previous_position = minimal_expanded.pop()
            steps.pop()
            #finding previous state and go to it again
            for s in successors:
                if s[0] == previous_position[0]:
                    fringe.push(previous_position)
                    steps.pop()
                    break
        #continue (we are not in a trap)       
        else:          
            for s in successors: 
                if s[0] in expanded:
                    pass
                else:
                    fringe.push(s)
                    fringe_history.append(s[0])
            minimal_expanded.append(choice)
    #end of my code
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #start of my code
    #setting up the requirments
    fringe = util.Queue()
    node_history = []
    fringe_history = []
    start_state = problem.getStartState()
    print(start_state)
    steps = []
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    #check if the start state is the goal state
    if problem.isGoalState(start_state):
        return []
    #expand the start node 
    successors = problem.getSuccessors(start_state)
    fringe_history.append(start_state)
    #our first pushes to the fringe queue
    for s in successors:
        node_history.append(s[0])
        aux = s
        aux = list(aux)
        aux.append(start_state)
        aux = tuple(aux)
        fringe.push(aux)
        fringe_history.append(aux)
    #main loop   
    while True:
        if fringe.isEmpty():
            break
        state = fringe.pop()
        if state[0] == start_state:
            state = fringe.pop()
        #check if we are in the goal state
        if problem.isGoalState(state[0]):
            the_parent = state[3]
            steps.append(state[1])
            while True:
                for node in fringe_history:
                    if node[0] == the_parent:
                        if node[0] == start_state:
                            steps.reverse()
                            print(steps)
                            return steps
                        else:
                            the_parent = node[3]
                            steps.append(node[1])
        #expand the poped node
        successors = problem.getSuccessors(state[0])
        #print(state[0])
        for child in successors:
            if child[0] not in node_history:
                if child == start_state:
                    pass
                else:
                    node_history.append(child[0])
                    aux = list(child)
                    aux.append(state[0])
                    aux = tuple(aux)
                    #push successors to the fringe wich are note pushed to it in the past
                    fringe.push(aux)
                    if aux not in fringe_history:
                        fringe_history.append(aux)
    #end of my code
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    #start of my code
    #setting up the requirments
    start_state = problem.getStartState()
    explored = []
    priority_fringe = util.PriorityQueue()
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    #check if the start node is the goal
    if problem.isGoalState(start_state):
        return []

    '''
        salam
        we want to store the cost to reach each 
        node on it's record in our priority queue
        we need to add start state to a suitable
        format because wen we get start state using
        getStartState() it's format is different
        from records that we get using getSuccessors()
        man vaqean mitarsam az in ke chon in comment
        ha ro be surate daqiq minevisam shoma fekr
        konid kole code ro az jaii cop zadam :(
    '''

    suitable_start_state_format = (start_state, [] , 0)
    priority_fringe.push(suitable_start_state_format, 0)

    #main loop
    while True:
        if priority_fringe.isEmpty():
            break
        state = priority_fringe.pop()
        #check if the poped node is the goal
        if problem.isGoalState(state[0]):
            print(state[1])
            return state[1]
        if state[0] not in explored:
            explored.append(state[0])
            #get the successors of the poped state:
            successors = problem.getSuccessors(state[0])
            for s in successors:
                #for each pushed node we keep the required cost to reach that
                aux = (s[0] , state[1]+ [s[1]] , s[2]+state[2])
                priority_fringe.push(aux , aux[2])
    #end of my code
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #start of my code
    #setting up requirments
    priority_fringe = util.PriorityQueue()
    explored = []
    start_state = problem.getStartState()
    #check if the start node is the goal or not
    if problem.isGoalState(start_state):
        return []
    '''
        salam
        mesle soale qabl:
        we want to store the cost to reach each 
        node on it's record in our priority queue
        we need to add start state to a suitable
        format because wen we get start state using
        getStartState() it's format is different
        from records that we get using getSuccessors()
    '''
    priority_fringe.push((start_state, [], 0),0)
    #check if the start node is the goal or not
    if problem.isGoalState(start_state):
        return []

    #main loop as always
    while True:
        if priority_fringe.isEmpty():
            break
        state = priority_fringe.pop()
        explored.append((state[0],state[2]))

        if problem.isGoalState(state[0]):
            return state[1]
        #grab successors
        successors = problem.getSuccessors(state[0])
        for s in successors:
            aux_s = (s[0], state[1] + [s[1]], problem.getCostOfActions(state[1] + [s[1]]))
            flag = 0
            for e in explored:
                #if we explored a node not for the first time and we just explored it with with higher cost 
                if (s[0] == e[0]) and (aux_s[2] >= e[1]):
                    flag = 1

            if not flag:
                priority_fringe.push(aux_s, aux_s[2] + heuristic(s[0], problem) )
                explored.append((s[0], aux_s[2]))

    return state[1]
    """
    why state[1] for return?
    because each node (in fact each tuple) that we pop has an list on
    it wich shows the steps to take for reaching
    the node
    """
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

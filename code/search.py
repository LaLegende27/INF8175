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

from custom_types import Direction
from pacman import GameState
from typing import Any, Tuple,List
import util 

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self)->Any:
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state:Any)->bool:
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state:Any)->List[Tuple[Any,Direction,int]]:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions:List[Direction])->int:
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem:SearchProblem)->List[Direction]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem:SearchProblem)->List[Direction]:
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

    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 1 ICI
    '''
    from util import Stack 
    
    L = Stack()
    L.push((problem.getStartState(),[])) # on rajoute la ou il faut aller 
    dejaVisiter = [] #pour eviter des loop infini il faut se rappeler des etats deja visiter. 
    while not L.isEmpty(): # jusqu'a temps quon a pas tout visiter
        state, path = L.pop() #etat courant et le chamin emprunter. 
        if state not in dejaVisiter:
            dejaVisiter.append(state)
            if problem.isGoalState(state): # si on a le bon etat 
                return path
            for (nextState, action, cost) in problem.getSuccessors(state): # il faut voir ceux qui ne sont pas encore visite 
                newPath = path +[action]
                L.push((nextState , newPath)) 
    return []#aucune solution 

    util.raiseNotDefined()


def breadthFirstSearch(problem:SearchProblem)->List[Direction]:
    """Search the shallowest nodes in the search tree first."""


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 2 ICI
    '''
    from util import Queue 
    
    L = Queue()
    L.push((problem.getStartState(),[])) # on rajoute la ou il faut aller 
    dejaVisiter = [] #pour eviter des loop infini il faut se rappeler des etats deja visiter. 
    while not L.isEmpty(): # jusqu'a temps quon a pas tout visiter
        state, path = L.pop() #etat courant et le chamin emprunter. 
        if state not in dejaVisiter:
            dejaVisiter.append(state)
            if problem.isGoalState(state): # si on a le bon etat 
                return path
            for (nextState, action, cost) in problem.getSuccessors(state): # il faut voir ceux qui ne sont pas encore visite 
                newPath = path +[action]
                L.push((nextState , newPath)) 
    return []#aucune solution 


    util.raiseNotDefined()

def uniformCostSearch(problem:SearchProblem)->List[Direction]:
    """Search the node of least total cost first."""


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 3 ICI
    '''
    from util import PriorityQueue 
    
    L = PriorityQueue()
    L.push((problem.getStartState(),[]),0) # on rajoute la ou il faut aller 
    dejaVisiter = [] #pour eviter des loop infini il faut se rappeler des etats deja visiter. 
    while not L.isEmpty(): 
        state, path = L.pop() #etat courant et le chamin emprunter. 
        if state not in dejaVisiter:
            dejaVisiter.append(state)
            if problem.isGoalState(state): # si on a le bon etat 
                return path
            for (nextState, action, cost) in problem.getSuccessors(state): # il faut voir ceux qui ne sont pas encore visite 
                newPath = path +[action]
                newCost = cost + problem.getCostOfActions(path) # on calcule un peu trop car on prend le total et le courant il faudrait faire path
                L.push((nextState , newPath),newCost) 
    return []#aucune solution 

    util.raiseNotDefined()

def nullHeuristic(state:GameState, problem:SearchProblem=None)->List[Direction]:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    return 0

def aStarSearch(problem:SearchProblem, heuristic=nullHeuristic)->List[Direction]:
    """
    Effectue une recherche A* pour trouver le chemin optimal vers l'état objectif.

    L'algorithme de recherche A* utilise à la fois le coût du chemin (g) et une heuristique (h) pour évaluer
    les nœuds et choisir ceux à explorer. Cet algorithme garantit que le chemin trouvé est le plus court si
    l'heuristique est admissible.

    Args:
        problem (SearchProblem): Le problème de recherche à résoudre, qui définit l'état initial,
                                 les états objectifs, les actions possibles et les successeurs.
        heuristic (function, optional): Une fonction heuristique prenant un état et le problème, et qui 
                                        retourne une estimation du coût restant jusqu'à l'état objectif.
                                        Par défaut, c'est la nullHeuristic qui retourne 0 partout.

    Returns:
        List[Direction]: Une liste d'actions qui mène de l'état initial à l'état objectif, ou une liste vide
                         si aucune solution n'est trouvée.

    Raises:
        util.raiseNotDefined: Si la fonction n'est pas implémentée correctement.
    
    Example:
        >>> aStarSearch(problem, manhattanHeuristic)
    """
    from util import PriorityQueue 
    
    L = PriorityQueue() 
    f_s = 0 + heuristic(problem.getStartState(),problem)
    L.push((problem.getStartState(),[]),f_s) 
    dejaVisiter = [] 
    while not L.isEmpty(): 
        state, path = L.pop() 
        if state not in dejaVisiter: 
            dejaVisiter.append(state)
            if problem.isGoalState(state): 
                return path
            for (nextState, action, cost) in problem.getSuccessors(state): 
                newPath = path +[action]
                f_s = problem.getCostOfActions(newPath) +  heuristic(nextState,problem) # cout du noeud + estiamtion des couts futures
                L.update((nextState , newPath),f_s) # si l'etat rajouter est dans le stack deja et qu'on ait calculer une priorite plus haute on change
    return [] 

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

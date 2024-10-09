from player_divercite import PlayerDivercite
from seahorse.game.action import Action
from seahorse.game.game_state import GameState
from game_state_divercite import GameStateDivercite
from seahorse.utils.custom_exceptions import MethodNotImplementedError
#ajout de librairie
import math
from typing import Callable

class MyPlayer(PlayerDivercite):
    """
    Player class for Divercite game that makes random moves.

    Attributes:
        piece_type (str): piece type of the player
    """

    def __init__(self, piece_type: str, name: str = "MyPlayer"):
        """
        Initialize the PlayerDivercite instance.

        Args:
            piece_type (str): Type of the player's game piece
            name (str, optional): Name of the player (default is "bob")
            time_limit (float, optional): the time limit in (s)
        """
        super().__init__(piece_type, name)

    def compute_action(self, current_state: GameState, remaining_time: int = 1e9, **kwargs) -> Action:
        """
        Use the minimax algorithm to choose the best action based on the heuristic evaluation of game states.

        Args:
            current_state (GameState): The current game state.

        Returns:
            Action: The best action as determined by minimax.
        """

        #TODO
        return self.halpha_beta_strategy(current_state, heuristic=self.heuristic_v1)
        raise MethodNotImplementedError()
    
    def halpha_beta_strategy(self, current_state: GameState, heuristic : Callable):

        def max_value(state: GameState, alpha, beta, depth):
            
            if depth == 0 :         
                return (heuristic(state),None) #retourne 0 si final sinon -1 ou +1
            
            v_prime = -math.inf
            best_action = None

            for action in state.generate_possible_heavy_actions() : #genere toutes les actions A OPTMISER 
            
                next_State = action.get_next_game_state() #fonction de transition T:(SxA) = S'
            
                (v, _) = min_value(next_State, alpha , beta, depth-1) # quelle coup va prendre notre adversaire
            
                if v > v_prime : # maj valeur maximum
                    best_action = action
                    v_prime = v
                    alpha = max(alpha,v_prime)
                
                if v_prime >= beta: 
                    return (v_prime,best_action) #le pruning a lieu ici 
             
            return (v_prime,best_action)            
            raise NotImplementedError("The max_value function is not implemented yet.")
        

        def min_value(state: GameState, alpha, beta, depth):
            
            if depth == 0 :         
                return (heuristic(state),None)
            
            v_prime = math.inf

            bestAction = None

            for action in state.generate_possible_heavy_actions() : #genere toutes les actions
            
                next_State = action.get_next_game_state() #fonction de transition T:(SxA) = S'
            
                (v, _) = max_value(next_State, alpha , beta, depth-1) 

                # le calcul doit se faire ici pour ...
                if  v < v_prime : # maj valeur minimum
                    bestAction = action
                    v_prime = v
                    beta = min(beta,v_prime) #update de nos bornes
                
                if v_prime <= alpha: 
                    return (v_prime,bestAction) #le pruning a lieu ici 
             
    
            return (v_prime,bestAction)
            raise NotImplementedError("The min_value function is not implemented yet.")
        

        return max_value(current_state, -math.inf, math.inf, 2)[1]
    
    def heuristic_v1(self, state: GameState):
        
        return 0 if not state.is_done() else state.get_player_score(self)
    
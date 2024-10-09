from player_divercite import PlayerDivercite
from seahorse.game.action import Action
from seahorse.game.game_state import GameState
from game_state_divercite import GameStateDivercite
from seahorse.utils.custom_exceptions import MethodNotImplementedError
# librairie rajouter
import math

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
        def halpha_beta_strategy(currentState: GameState, heuristic):

            def max_value(state: GameState, alpha, beta, depth):
                
                if depth == 0 :         
                    return (heuristic(state),None) #retourne 0 si final sinon -1 ou +1
                
                v_prime = -math.inf
                bestAction = None

                for action in state.generate_possible_heavy_actions() : #genere toutes les actions A OPTMISER 
                
                    next_State = action.get_next_game_state() #fonction de transition T:(SxA) = S'
                
                    (v, _) = min_value(next_State, alpha , beta, depth-1) # quelle coup va prendre notre adversaire
                
                    if v > v_prime : # maj valeur maximum
                        bestAction = action
                        v_prime = v
                        alpha = max(alpha,v_prime)
                    
                    if v_prime >= beta: 
                        return (v_prime,bestAction) #le pruning a lieu ici 
                
                return (v_prime,bestAction)            

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
            return max_value(currentState, -math.inf, math.inf, 4)[1]
        
        def my_heuristic(state: GameState):
            
            ''' 
            retourne 0 si l'etat est final, sinon retourne le score. en a et on essaye de bloquer pour que ce soit statique le plus possible
                
            Args : 
                state (GameState) : l'etat courant du jeu divercite
            
            Returns : 
                un score evaluer par l'heuristique. 

            '''
            
            return 0 if not state.is_done() else  state.get_player_score(self)
        
        return halpha_beta_strategy(current_state, my_heuristic)
        raise MethodNotImplementedError()

import math

class MinimaxAgent:
    def __init__(self, limit):
        self.limit = limit

    def evaluate(self, state):
        # TODO: better evaluated value
        return state.player1.score - state.player2.score

    def get_best_move(self, state):
        best_utility = -math.inf
        best_move = -1

        for move in range(6):
            cloned_state = state.clone()
            success = cloned_state.make_move(move)
            if not success:
                continue

            utility = self.minimax(cloned_state, self.limit-1) 
            if utility > best_utility:
                best_utility = utility
                best_move = move

        return best_move


    def minimax(self, state, depth):
        if depth == 0:
            return self.evaluate(state)

        all_utilities = []
        is_player1_turn = state.is_player1_turn()

        for possible_action in range(6):
            cloned_state = state.clone()
            success = cloned_state.make_move(possible_action)
            if not success:
                continue

            utility = self.minimax(cloned_state, depth-1)
            all_utilities.append(utility)
        
        if is_player1_turn:
            return max(all_utilities)
        else:
            return min(all_utilities)

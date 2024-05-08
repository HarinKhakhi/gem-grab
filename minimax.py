class MinimaxAgent:
    def __init__(self, limit):
        self.limit = limit

    def evaluate(self, state):
        # TODO: better evaluated value
        return state.player1.score

    def get_best_move(self, state):
        best_utility = -1
        best_move = -1

        for move in range(6):
            success = state.make_move(move)
            if not success:
                continue

            utility = self.minimax(state, self.limit-1) 
            if utility > best_utility:
                best_utility = utility
                best_move = move

        return best_move


    def minimax(self, state, depth):
        if depth == 0:
            return self.evaluate(state)

        all_utilities = []
        for possible_action in range(6):
            success = state.make_move(possible_action)
            if not success:
                continue

            utility = self.minimax(state, depth-1)
            all_utilities.append(utility)
        
        if state.is_player1_turn():
            return max(all_utilities)
        else:
            return min(all_utilities)

from game import Game
from minimax import MinimaxAgent

game = Game(5,5)
agent = MinimaxAgent(5)

# game loop: run until the game is over
while not game.is_over():

    # print the game state
    game.print()
   
    # ask for player's move
    if game.is_player1_turn():
        clone_game = game.clone()
        best_move = agent.get_best_move(clone_game)
        print(best_move)
        success = game.make_move(best_move)
        if not success: print('last move was unsuccessfull')
    else:
        move = int(input('Player 2 make your move: '))
        success = game.make_move(move)
        if not success: print('last move was unsuccessfull')

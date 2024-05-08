from game import Game

game = Game(2,2)

# game loop: run until the game is over
while not game.is_over():

    # print the game state
    game.print()
   
    # ask for player's move
    if game.is_player1_turn():
        move = int(input('Player 1 make your move: '))
        success = game.make_move(move)
        if not success: print('last move was unsuccessfull')
    else:
        move = int(input('Player 2 make your move: '))
        success = game.make_move(move)
        if not success: print('last move was unsuccessfull')

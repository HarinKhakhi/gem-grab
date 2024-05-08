import random
from termcolor import colored

from player import Player

DEFAULT_ROWS = 5
DEFAULT_COLS = 5

class Game:
    def __init__(self, rows=DEFAULT_ROWS, cols=DEFAULT_COLS):
        self.rows = rows
        self.cols = cols

        # initialize the board
        self.board = self._initialize_board(rows, cols)

        # initialize blocked_cells grid 
        self.blocked_cells = self._initialize_blocked_cells(rows, cols)

        # initialize the players
        self.player1 = Player('player 1', [0,0]) 
        self.player2 = Player('player 2', [1,1])

        self.current_iteration = 0
    
    def make_move(self, move):
        '''
        tries to perform the given move and returns if the move was successfull
        allowed moves:
            0: up
            1: down
            2: left
            3: right
            4: collect_gem
            5: block_the_cell
        '''

        player = self._get_current_player()
        
        if move == 0:
            new_r = player.position[0] - 1
            new_c = player.position[1]
            bc_value = self.blocked_cells[new_r][new_c]  

            if bc_value != 0 and bc_value != player.name:
                return False

            # update position
            player.position[0] -= 1
    
        elif move == 1:
            new_r = player.position[0] + 1
            new_c = player.position[1]
            bc_value = self.blocked_cells[new_r][new_c]  

            if bc_value != 0 and bc_value != player.name:
                return False

            # update position
            player.position[0] += 1

        elif move == 2:
            new_r = player.position[0]
            new_c = player.position[1] - 1
            bc_value = self.blocked_cells[new_r][new_c]  

            if bc_value != 0 and bc_value != player.name:
                return False

            # update position
            player.position[1] -= 1

        elif move == 3:
            new_r = player.position[0]
            new_c = player.position[1] + 1
            bc_value = self.blocked_cells[new_r][new_c]  

            if bc_value != 0 and bc_value != player.name:
                return False

            # update position
            player.position[1] += 1

        elif move == 4:
            # update player score
            player.score += self._collect_gem(player.position)

        elif move == 5:
            # add blocked cell to the map
            r = player.position[0]
            c = player.position[1]
            self.blocked_cells[r][c] = player.name

        self.current_iteration += 1
    
        return True

    def print(self):
        '''
        prints the status of the game: board and scores
        '''
        
        for rowi in range(self.rows):
            for coli in range(self.cols):
                current_cell = self.board[rowi][coli]
                blocked_player = self.blocked_cells[rowi][coli]

                font_c = 'white'
                bg_c = 'on_black'

                # checking if there is a player1 on cell (rowi, coli)
                if (
                    (rowi == self.player1.position[0] and coli == self.player1.position[1]) or
                    blocked_player == self.player1.name
                ):
                    font_c = 'black'
                    bg_c = 'on_red'

                # checking if there is a player2 on cell (rowi, coli)
                elif (
                    (rowi == self.player2.position[0] and coli == self.player2.position[1]) or
                    blocked_player == self.player2.name
                ):
                    font_c = 'black'
                    bg_c = 'on_blue'
                
                print(colored(current_cell, font_c, bg_c), end=' ')
            print()

        print(colored('player 1', 'black', 'on_red'), 'score: ', self.player1.score)
        print(colored('player 2', 'black', 'on_blue'), 'score: ', self.player2.score)

    def _collect_gem(self, position):
        '''
        collects the gem on the given position: returns the gem value and makes it 0
        '''

        gem_value = self.board[position[0]][position[1]]
        self.board[position[0]][position[1]] = 0
        return gem_value

    def is_player1_turn(self):
        return self.current_iteration % 2 == 0

    def is_player2_turn(self):
        return self.current_iteration % 2 != 0

    def _get_current_player(self):
        if self.is_player1_turn(): return self.player1
        else: return self.player2

    def is_over(self):
        '''
        checks if the game is over or not: if all cell values are non-zero
        '''
        for rowi in range(self.rows):
            for coli in range(self.cols):
                if self.board[rowi][coli] != 0:
                    return False

        return True

    def _initialize_board(self, rows, cols):
        '''
        creates a random board
        '''

        board = []
        for rowi in range(rows):
            row = []
            for coli in range(cols):
                row.append(random.randint(1, 5))
            board.append(row)
        return board

    def _initialize_blocked_cells(self, rows, cols):
        '''
        initizlizes the blocked cell grid
        0: unblocked
        1: blocked
        '''
        blocked_cells = []
        for rowi in range(rows): 
            row = []
            for coli in range(cols):
                row.append(0)
            blocked_cells.append(row)
        return blocked_cells

import math
import random

class Player:
    def __init__(self, letter):
        # Letter for the player either O or X
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):    
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # we are going to check that this is a correct value by trying to cast 
            # to integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if casting to int is ok and there is vailable spot according to that integer value
            except ValueError:
                print('Invalid square. Try again.')
    
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # randomly choose if all spots are available
        else: 
            # get the square based on mimimax algorithm 
            square = self.minimax(game, self.letter)['position']
        return square
    
    # def minimax(self, state, player):
    #     max_player = self.letter # me !!
    #     other_player = 'O' if player == 'X' else 'X' # other player

    #     # first, we want to check that previous move is a winner
    #     # this is the base case we consider
    #     if state.current_winner == other_player:
    #         # we should return position and score because we need to track the score (sum of utilities function)
    #         # for minimax to work 
    #         return {'position' : None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() +1)}
    #     elif not state.empty_squares(): # no empty squares
    #         return {'position': None, 'score' : 0}
        
    #     # initailize some dictionaries for the maximize and minimize rules
    #     if player == max_player:
    #         best = {'position': None, 'score': -math.inf} # maximize should be larger
    #     else:
    #         best = {'postion': None, 'score': math.inf} # each score should minimize

    #     for possible_move in state.available_moves():
    #         # step1 : Make a move, try that spot
    #         state.make_move(possible_move, player)
    #         # step2 : Recurse the minimax to simulate a game after making that move
    #         sim_score = self.minimax(state, other_player)
    #         # step3 : Undo the move to move to next move in the list of available moves
    #         state.board[possible_move] = ' '
    #         state.current_winner = None
    #         sim_score['position'] = possible_move # otherwise this will get messed up in recursion

    #         # step4 : Update the dictionaries if necessary
    #         if player == max_player:
    #             if(sim_score['score'] > best['score']): # Maximize the max_player
    #                 best = sim_score
    #         else:
    #             if(sim_score['score'] < best['score']): # Minimize the other_player
    #                 best = sim_score
    #     return best

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'
        
        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
